# components/widgets.py

import tkinter as tk
from tkinter import ttk
from core.theme import *


def btn(parent, text, cmd, color=BLUE, fg="white", **kw):
    b = tk.Button(parent, text=text, command=cmd, bg=color, fg=fg,
                  font=FB, relief="flat", padx=12, pady=5, cursor="hand2", **kw)
    b.bind("<Enter>", lambda e: b.config(bg=BLUE_LT if color == BLUE else color))
    b.bind("<Leave>", lambda e: b.config(bg=color))
    return b


def label(parent, text, font=FB, color=DARK, **kw):
    return tk.Label(parent, text=text, font=font, fg=color, bg=WHITE, **kw)


def sep(parent):
    tk.Frame(parent, bg=BORDER, height=1).pack(fill="x", pady=6)


def field(parent, label_text, row, var, col=0, width=24):
    tk.Label(parent, text=label_text, font=FS, fg=GRAY, bg=WHITE,
             anchor="w").grid(row=row, column=col*2, sticky="w", padx=(0,6), pady=4)
    e = tk.Entry(parent, textvariable=var, font=FB, width=width,
                 relief="solid", bd=1)
    e.grid(row=row, column=col*2+1, sticky="ew", pady=4)
    return e


def dropdown(parent, label_text, row, var, values, col=0, width=22):
    tk.Label(parent, text=label_text, font=FS, fg=GRAY, bg=WHITE,
             anchor="w").grid(row=row, column=col*2, sticky="w", padx=(0,6), pady=4)
    cb = ttk.Combobox(parent, textvariable=var, values=values,
                      state="readonly", font=FB, width=width)
    cb.grid(row=row, column=col*2+1, sticky="ew", pady=4)
    return cb


def make_table(parent, cols, widths, height=15):
    style = ttk.Style()
    style.configure("S.Treeview", rowheight=26, font=FB, background=WHITE,
                    fieldbackground=WHITE, foreground=DARK)
    style.configure("S.Treeview.Heading", font=FBD, background=LIGHT,
                    foreground=DARK, relief="flat")
    style.map("S.Treeview", background=[("selected", BLUE)],
              foreground=[("selected", "white")])

    frame = tk.Frame(parent, bd=1, relief="solid")
    tv = ttk.Treeview(frame, columns=cols, show="headings",
                      style="S.Treeview", height=height)
    sb = ttk.Scrollbar(frame, orient="vertical", command=tv.yview)
    tv.configure(yscrollcommand=sb.set)
    for c, w in zip(cols, widths):
        tv.heading(c, text=c)
        tv.column(c, width=w, anchor="w")
    tv.pack(side="left", fill="both", expand=True)
    sb.pack(side="right", fill="y")
    return frame, tv
