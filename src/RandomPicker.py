import random
import tkinter as tk
from tkinter import ttk

class DraftPickerApp:
    def __init__(self, root, players):
        self.root = root
        self.players = players
        self.current_pick = 0
        
        random.shuffle(self.players)

        # Configure root window
        self.root.title("Draft Picker")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f0f0')

        # Create and style widgets
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        self.style.configure("TLabel", font=("Helvetica", 14), padding=10, background='#f0f0f0')
        self.style.configure("TListbox", font=("Helvetica", 12), padding=10)

        self.label = ttk.Label(root, text="Press the button to assign draft pick.")
        self.label.pack(pady=20)

        self.button = ttk.Button(root, text="Assign Draft Pick", command=self.assign_pick)
        self.button.pack(pady=20)

        self.listbox_frame = ttk.Frame(root)
        self.listbox_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.listbox_label = ttk.Label(self.listbox_frame, text="Draft Order:")
        self.listbox_label.pack(anchor=tk.NW, pady=5)

        self.listbox = tk.Listbox(self.listbox_frame, font=("Helvetica", 12), width=30, height=15)
        self.listbox.pack(fill=tk.BOTH, expand=True)

    def assign_pick(self):
        if self.current_pick < len(self.players):
            player = self.players[self.current_pick]
            self.current_pick += 1
            self.label.config(text=f"{player} is assigned draft pick {self.current_pick}")
            self.listbox.insert(tk.END, f"Pick {self.current_pick}: {player}")
        else:
            self.label.config(text="All draft picks have been assigned.")
            self.button.config(state=tk.DISABLED)

if __name__ == "__main__":
    players = [
        "John Bummit",
        "Fat Kermit",
        "Alexin6",
        "RennaJeetz",
        "G3offry",
        "HughJass",
        "Spaciee",
        "ElonsDick",
        "DGTL Crunchwrap",
        "AMMAR"
    ]

    root = tk.Tk()
    app = DraftPickerApp(root, players)
    root.mainloop()
