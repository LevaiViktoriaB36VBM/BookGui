import customtkinter as ctk
from tkinter import messagebox
import db
import register_window
import user_window


ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

def login_user():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    result = db.validate_user(username, password)
    if result is None:
        messagebox.showerror("Hiba", "Nincs adatbázis kapcsolat!")
        return
    if result:
        messagebox.showinfo("Siker", f"Üdv, {username}!")
        user_window.open_user_window(username)
    else:
        messagebox.showerror("Hiba", "Helytelen felhasználónév vagy jelszó!")


root = ctk.CTk()
root.title("Bejelentkezés")
root.geometry("400x300")


db_conn = db.get_db_connection()
db_ok = db_conn is not None
if db_conn: db_conn.close()

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Bejelentkezés", font=("Arial", 18, "bold"))
label.pack(pady=12, padx=10)

entry_username = ctk.CTkEntry(master=frame, placeholder_text="Felhasználónév")
entry_username.pack(pady=12, padx=10)

entry_password = ctk.CTkEntry(master=frame, placeholder_text="Jelszó", show="*")
entry_password.pack(pady=12, padx=10)

btn_login = ctk.CTkButton(master=frame, text="Bejelentkezés", command=login_user, state=("normal" if db_ok else "disabled"))
btn_login.pack(pady=12, padx=10)

btn_register = ctk.CTkButton(master=frame, text="Regisztráció", command=register_window.open_register_window, state=("normal" if db_ok else "disabled"))
btn_register.pack(pady=12, padx=10)


if db_ok:
    lbl_status = ctk.CTkLabel(master=frame, text="Adatbázis kapcsolat OK", text_color="green")
else:
    lbl_status = ctk.CTkLabel(master=frame, text="Nincs adatbázis kapcsolat!", text_color="red")
lbl_status.pack(pady=12, padx=10)

root.mainloop()
