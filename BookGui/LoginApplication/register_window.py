import customtkinter as ctk
from tkinter import messagebox
import db, re

def open_register_window():
    reg_win = ctk.CTkToplevel()
    reg_win.title("Regisztráció")
    reg_win.geometry("420x400")

    frame = ctk.CTkFrame(master=reg_win)
    frame.pack(pady=20, padx=40, fill="both", expand=True)

    ctk.CTkLabel(frame, text="Új felhasználó regisztráció", font=("Arial", 16, "bold")).pack(pady=12)

    entry_fullname = ctk.CTkEntry(master=frame, placeholder_text="Teljes név")
    entry_fullname.pack(pady=8)

    entry_email = ctk.CTkEntry(master=frame, placeholder_text="Email")
    entry_email.pack(pady=8)

    entry_username = ctk.CTkEntry(master=frame, placeholder_text="Felhasználónév")
    entry_username.pack(pady=8)

    entry_password = ctk.CTkEntry(master=frame, placeholder_text="Jelszó", show="*")
    entry_password.pack(pady=8)

    entry_password2 = ctk.CTkEntry(master=frame, placeholder_text="Jelszó megerősítése", show="*")
    entry_password2.pack(pady=8)

    def do_register():
        fullname = entry_fullname.get().strip()
        email = entry_email.get().strip()
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        password2 = entry_password2.get().strip()

        if not fullname or not email or not username or not password:
            messagebox.showwarning("Hiba", "Minden mezőt ki kell tölteni!")
            return

        if password != password2:
            messagebox.showwarning("Hiba", "A két jelszó nem egyezik!")
            return

        if len(password) < 6:
            messagebox.showwarning("Hiba", "A jelszónak legalább 6 karakter hosszúnak kell lennie!")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showwarning("Hiba", "Érvénytelen email formátum!")
            return

        ok, msg = db.register_user(fullname, email, username, password)
        if ok:
            messagebox.showinfo("Siker", msg)
            reg_win.destroy()
        else:
            messagebox.showerror("Hiba", msg)

    ctk.CTkButton(frame, text="Regisztráció", command=do_register).pack(pady=15)
