import tkinter as tk

class Button:
    def __init__(self, root):
        self.root = root
        self.klicks = 0
        self.language = "DE"

        self.label = tk.Label(root, text="Servus!")
        self.label.pack()

        self.button = tk.Button(root, text="Klick mich!", command=self.klick)
        self.button.pack(pady=10)

        self.button1 = tk.Button(root, text="Sprache ändern", command=self.andern)
        self.button1.pack(pady=10)

    def klick(self):
        self.klicks += 1
        self.label.config(text=f"Button {self.klicks} geklickt")
        if self.klicks == 100:
            print("BOOM!")

    def andern(self):
        if self.language == "DE":
            self.label.config(text="Dil degistirildi")
            self.button.config(text="Tikla!")
            self.button1.config(text="Dil degistir")
            self.language = "TR"
        else:
            self.label.config(text="Sprache geändert")
            self.button.config(text="Klick mich!")
            self.button1.config(text="Sprache ändern")
            self.language = "DE"


root = tk.Tk()
root.title("Button")
gui = Button(root)
root.mainloop()