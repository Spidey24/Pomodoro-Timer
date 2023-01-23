import tkinter as tk
from PIL import ImageTk,Image 
import winsound


class Pomodoro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x300')
        self.root.resizable(False,False)
        self.root.title("Pomodoro Timer")
        self.pomodoro_time = 1500 # Pomodoro duration in seconds
        self.break_time = 300 # Short break duration in seconds
        self.time_left = self.pomodoro_time
        self.timer_running = False
        self.pomodoros_completed = 0
        self.create_widgets()



    def create_widgets(self):
        # Create a background image
        self.bg_image = ImageTk.PhotoImage(Image.open("bgimg.jpg"))
        self.bg_label = tk.Label(self.root, image=self.bg_image,bg='grey')
        self.bg_label.place(relheight=1,relwidth=1)
        #Create time labels
        self.time_label = tk.Label(self.root, text="25:00", font=("Ubuntu bold", 24),justify='center')
        self.root.wm_attributes('-transparentcolor','grey')
        self.time_label.pack(pady=40)

        self.pomodoro_label = tk.Label(self.root, text="Pomodoro",font=("Helvetica", 16))
        self.pomodoro_label.pack()

        self.break_label = tk.Label(self.root, text="Break", font=("Helvetica", 16))
        self.break_label.pack_forget()

        self.pomodoros_completed_label = tk.Label(self.root, text="Pomodoros completed=> 0", font=("Arial italic", 16),)
        self.pomodoros_completed_label.pack()

        self.start_button = tk.Button(self.root, text="Start",width=7,command=self.start,bg='lightgreen')
        self.start_button.pack(padx=10,pady=10)

        self.reset_button = tk.Button(self.root, text="Reset",width=7, command=self.reset,bg='orange')
        self.reset_button.pack(padx=20)
        
    def start(self):
        if not self.timer_running:
            self.timer_running = True
            self.countdown()

    def reset(self):
        self.time_left = self.pomodoro_time
        self.timer_running = False
        self.pomodoros_completed = 0
        self.pomodoros_completed_label.config(text="Pomodoros completed: 0")
        self.time_label.config(text="25:00")
        self.pomodoro_label.pack()
        self.break_label.pack_forget()

    def countdown(self):
        if self.time_left > 0:
            minutes, seconds = divmod(self.time_left, 60)
            time_string = "{:02}:{:02}".format(minutes, seconds)
            self.time_label.config(text=time_string)
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.timer_running = False
            winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)
        if self.time_left == 0:
            if self.pomodoro_label.winfo_ismapped():
                self.pomodoros_completed += 1
                self.pomodoros_completed_label.config(text=f"Pomodoros completed: {self.pomodoros_completed}")
                self.time_left = self.break_time
                self.pomodoro_label.pack_forget()
                self.break_label.pack()
            else:
                self.time_left = self.pomodoro_time
                self.pomodoro_label.pack()
                self.break_label.pack_forget()

pomodoro = Pomodoro()
pomodoro.root.mainloop()
