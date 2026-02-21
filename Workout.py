import tkinter as tk
from tkinter import messagebox

class WorkoutTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Timer")
        self.root.geometry("300x300")
        self.root.resizable(False, False)

        self.work_time = 30      # seconds
        self.rest_time = 10      # seconds
        self.rounds = 3
        self.current_round = 1
        self.is_work = True
        self.time_left = self.work_time

        self.label = tk.Label(root, text="Workout Timer", font=("Arial", 16))
        self.label.pack(pady=10)

        self.round_label = tk.Label(root, text=f"Round: {self.current_round}/{self.rounds}", font=("Arial", 12))
        self.round_label.pack()

        self.timer_label = tk.Label(root, text=str(self.time_left), font=("Arial", 40))
        self.timer_label.pack(pady=20)

        self.status_label = tk.Label(root, text="WORK", font=("Arial", 14), fg="green")
        self.status_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

    def start_timer(self):
        self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.timer_label.config(text=str(self.time_left))
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            if self.is_work:
                self.is_work = False
                self.time_left = self.rest_time
                self.status_label.config(text="REST", fg="red")
            else:
                self.current_round += 1
                if self.current_round > self.rounds:
                    messagebox.showinfo("Done", "Workout Complete!")
                    return
                self.round_label.config(text=f"Round: {self.current_round}/{self.rounds}")
                self.is_work = True
                self.time_left = self.work_time
                self.status_label.config(text="WORK", fg="green")

            self.countdown()

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutTimer(root)
    root.mainloop()
