import tkinter as tk
from tkinter import messagebox, ttk
import heapq
from collections import Counter

class AlumniPlatform:
    def __init__(self, root):
        self.root = root
        self.root.title("Alumni Association Platform - Futuristic Red HTML Style")
        self.root.geometry("1200x800")
        self.root.configure(bg="#0b0c10")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background='#0b0c10', borderwidth=0)
        style.configure("TNotebook.Tab", background='#1f1f1f', foreground='red', padding=[12, 8], font=('Consolas', 11, 'bold'))
        style.map("TNotebook.Tab",
                  background=[("selected", '#ff1a1a')],
                  foreground=[("selected", 'white')])

        tab_control = ttk.Notebook(self.root)

        self.tabs = {}
        tab_names = ["Register", "Donate", "Networking", "Job Portal", "Directory", "Success Stories", "Event Scheduler", "Feedback"]

        for name in tab_names:
            frame = tk.Frame(tab_control, bg='#121212')
            tab_control.add(frame, text=name)
            self.tabs[name] = frame

        tab_control.pack(expand=1, fill='both')

        self.build_register_tab()
        self.build_donation_tab()
        self.build_network_tab()
        self.build_job_tab()
        self.build_directory_tab()
        self.build_success_tab()
        self.build_events_tab()
        self.build_feedback_tab()

    def themed_label(self, parent, text, size=12):
        return tk.Label(parent, text=text, bg='#121212', fg='red', font=('Segoe UI', size, 'bold'))

    def themed_entry(self, parent):
        return tk.Entry(parent, bg='#1c1c1c', fg='white', insertbackground='white', relief='flat', font=('Consolas', 12), highlightbackground='red', highlightcolor='red', highlightthickness=1)

    def themed_button(self, parent, text, command):
        return tk.Button(parent, text=text, command=command, bg='#ff1a1a', fg='white', activebackground='#b30000', activeforeground='white', relief='flat', font=('Segoe UI', 11, 'bold'), padx=12, pady=6, cursor='hand2')

    def build_register_tab(self):
        frame = self.tabs["Register"]
        for label in ["Name", "Email", "Graduation Year"]:
            self.themed_label(frame, label).pack(pady=5)
            self.themed_entry(frame).pack(pady=5, ipadx=60)
        self.themed_button(frame, "Register", lambda: messagebox.showinfo("Registered", "Registration Successful!"))\
.pack(pady=20)

    def build_donation_tab(self):
        frame = self.tabs["Donate"]
        self.themed_label(frame, "Amount (INR)").pack(pady=10)
        self.themed_entry(frame).pack(pady=5, ipadx=60)
        self.themed_button(frame, "Donate", lambda: messagebox.showinfo("Thank You", "Donation Successful!"))\
.pack(pady=20)

    def build_network_tab(self):
        frame = self.tabs["Networking"]
        graph = {'A': {'B': 2, 'C': 5}, 'B': {'A': 2, 'C': 1, 'D': 4}, 'C': {'A': 5, 'B': 1, 'D': 1}, 'D': {'B': 4, 'C': 1}}
        dist = {node: float('inf') for node in graph}
        dist['A'] = 0
        pq = [(0, 'A')]
        while pq:
            d, u = heapq.heappop(pq)
            for v in graph[u]:
                if dist[v] > d + graph[u][v]:
                    dist[v] = d + graph[u][v]
                    heapq.heappush(pq, (dist[v], v))
        res = "\n".join([f"A to {k}: {v}" for k, v in dist.items()])
        self.themed_label(frame, "Connection Costs from Node A", 14).pack(pady=10)
        tk.Label(frame, text=res, bg='#121212', fg='white', font=('Consolas', 12)).pack(pady=10)

    def build_job_tab(self):
        frame = self.tabs["Job Portal"]
        self.themed_label(frame, "Max Effort Level").pack(pady=10)
        effort_entry = self.themed_entry(frame)
        effort_entry.pack(pady=5, ipadx=60)

        def recommend():
            try:
                max_effort = int(effort_entry.get())
                jobs = [
                    {"title": "Data Analyst", "relevance": 80, "effort": 3},
                    {"title": "Web Dev Intern", "relevance": 60, "effort": 2},
                    {"title": "Software Engineer", "relevance": 90, "effort": 5},
                    {"title": "ML Intern", "relevance": 70, "effort": 4},
                ]
                n = len(jobs)
                dp = [[0] * (max_effort + 1) for _ in range(n + 1)]
                for i in range(1, n + 1):
                    for w in range(max_effort + 1):
                        if jobs[i - 1]['effort'] <= w:
                            dp[i][w] = max(jobs[i - 1]['relevance'] + dp[i - 1][w - jobs[i - 1]['effort']], dp[i - 1][w])
                        else:
                            dp[i][w] = dp[i - 1][w]
                w = max_effort
                selected = []
                for i in range(n, 0, -1):
                    if dp[i][w] != dp[i - 1][w]:
                        selected.append(jobs[i - 1]['title'])
                        w -= jobs[i - 1]['effort']
                messagebox.showinfo("Jobs Recommended", "\n".join(reversed(selected)))
            except:
                messagebox.showerror("Error", "Invalid input")

        self.themed_button(frame, "Recommend Jobs", recommend).pack(pady=20)

    def build_directory_tab(self):
        frame = self.tabs["Directory"]
        self.themed_label(frame, "Search Alumni by Name, Year or Field").pack(pady=10)
        self.themed_entry(frame).pack(pady=5, ipadx=60)
        self.themed_button(frame, "Search", lambda: messagebox.showinfo("Search Results", "John Doe, CSE, 2015\nJane Smith, ECE, 2016")).pack(pady=20)

    def build_success_tab(self):
        frame = self.tabs["Success Stories"]
        self.themed_label(frame, "Top Alumni Success Stories", 14).pack(pady=10)
        text = "1. John - CEO at XYZ\n2. Mary - Author and Speaker\n3. Arjun - Start-up Founder"
        tk.Label(frame, text=text, bg='#121212', fg='white', font=('Segoe UI', 12)).pack(pady=10)

    def build_events_tab(self):
        frame = self.tabs["Event Scheduler"]
        events = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
        events.sort(key=lambda x: x[1])
        res, end = [], 0
        for s, e in events:
            if s >= end:
                res.append(f"Event: {s}-{e}")
                end = e
        self.themed_label(frame, "Scheduled Events (Greedy)", 14).pack(pady=10)
        tk.Label(frame, text="\n".join(res), bg='#121212', fg='white', font=('Segoe UI', 12)).pack(pady=10)

    def build_feedback_tab(self):
        frame = self.tabs["Feedback"]
        self.themed_label(frame, "Your Feedback").pack(pady=10)
        fb_text = tk.Text(frame, height=6, bg='#1c1c1c', fg='white', insertbackground='white', relief='flat', font=('Consolas', 12), highlightbackground='red', highlightcolor='red', highlightthickness=1)
        fb_text.pack(padx=10, pady=5, ipadx=5, ipady=5)
        self.themed_button(frame, "Submit", lambda: messagebox.showinfo("Submitted", "Thank you for your feedback!"))\
.pack(pady=20)

if __name__ == '__main__':
    root = tk.Tk()
    app = AlumniPlatform(root)
    root.mainloop()
