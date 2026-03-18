import tkinter as tk
from core.theme import *

PAGES = [
    ("Dashboard",   "dashboard"),
    ("Rooms",       "rooms"),
    ("Students",    "students"),
    ("Fee Records", "fees"),
    ("Complaints",  "complaints"),
    ("Reports",     "reports"),
]


class Sidebar(tk.Frame):
    def __init__(self, parent, on_nav):
        super().__init__(parent, bg=BLUE, width=180)
        self.pack_propagate(False)
        self.on_nav = on_nav
        self._active = None
        self._btns = {}
        self._build()

    def _build(self):
        # App name header
        tk.Label(self, text="Hostel", bg=BLUE, fg="white",
                 font=("Arial", 16, "bold")).pack(pady=(18, 0))
        tk.Label(self, text="Management", bg=BLUE, fg="#cce4ff",
                 font=("Arial", 10)).pack(pady=(0, 4))
        tk.Label(self, text="System", bg=BLUE, fg="#cce4ff",
                 font=("Arial", 10)).pack(pady=(0, 16))
        tk.Frame(self, bg="#4a8fc0", height=1).pack(fill="x", padx=12)

        for label, key in PAGES:
            b = tk.Button(self, text=f"  {label}", bg=BLUE, fg="white",
                          font=("Arial", 11), relief="flat", anchor="w",
                          padx=10, pady=9, cursor="hand2",
                          activebackground="#1a5a9a", activeforeground="white",
                          command=lambda k=key: self.navigate(k))
            b.pack(fill="x", pady=1)
            self._btns[key] = b

        tk.Frame(self, bg="#4a8fc0", height=1).pack(fill="x", padx=12, pady=12)
        tk.Label(self, text="© 2024  Student Project", bg=BLUE,
                 fg="#99c4e8", font=("Arial", 8)).pack(side="bottom", pady=10)

    def navigate(self, key):
        if self._active:
            self._btns[self._active].config(bg=BLUE, fg="white")
        self._active = key
        self._btns[key].config(bg="#1a5a9a", fg="white")
        self.on_nav(key)
