import tkinter as tk
import time

class Error(tk.Toplevel):
    def __init__(self, message):
        tk.Toplevel.__init__(self)
        tk.Label(self, text=message).grid(row=0, column=0)
        tk.Button(self, command=self.destroy, text="OK").grid(row=1, column=0)
        self.lift()  # Puts Window on top
        self.grab_set()  # Prevents other Tkinter windows from being used


def showerror(string):
    Error(string)


if __name__ == '__main__':
    w = tk.Tk()
    print("what should i remind you about?")
    text = str(input())

    print("In how many minutes?")
    local_time = float(input())

    local_time = local_time * 60

    time.sleep(local_time)
    showerror(text)
    w.mainloop()