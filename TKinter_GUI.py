import tkinter as tk

class ButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Der ultimative Button")
        self.root.geometry("300x250")
        self.klicks = 0
        self.language = "DE"

        self.label = tk.Label(root, text="Servus!", font=("Arial", 12))
        self.label.pack(pady=10)

        # Startfarbe festlegen
        self.button = tk.Button(root, text="Klick mich!", command=self.klick, bg="#f0f0f0")
        self.button.pack(pady=10, ipadx=10, ipady=5)

        self.button1 = tk.Button(root, text="Sprache ändern", command=self.andern)
        self.button1.pack(pady=10)

    def update_button_color(self):
        """Berechnet einen Farbverlauf von Grau nach Rot basierend auf den Klicks."""
        # Je näher an 100, desto kleiner werden die Grün- und Blau-Anteile
        # Rot bleibt hoch (255), Grün/Blau sinken von ~240 auf 0
        intensity = int(240 - (self.klicks * 2.4)) 
        if intensity < 0: intensity = 0
        
        # Farbe im Hex-Format #RRGGBB
        color = f"#ff{intensity:02x}{intensity:02x}"
        self.button.config(bg=color, activebackground=color)

    def klick(self):
        self.klicks += 1
        self.label.config(text=f"Button {self.klicks} geklickt")
        
        # Farbe anpassen
        if self.klicks <= 100:
            self.update_button_color()

        if self.klicks == 100:
            self.explode()

    def explode(self):
        """Lässt das Fenster 'auseinandergehen' und zeigt BOOM an."""
        # Alle Widgets entfernen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Fensterhintergrund auf Schwarz ändern
        self.root.config(bg="black")
        
        # Fenster vergrößern für den Effekt
        self.root.geometry("500x400")
        
        # Riesen BOOM Label
        boom_label = tk.Label(
            self.root, 
            text="💥 BOOM! 💥", 
            fg="red", 
            bg="black", 
            font=("Helvetica", 50, "bold")
        )
        boom_label.pack(expand=True)
        
        print("BOOM! Das Fenster ist explodiert.")

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
gui = ButtonApp(root)
root.mainloop()