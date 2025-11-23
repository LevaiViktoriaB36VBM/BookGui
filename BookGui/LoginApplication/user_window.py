import customtkinter as ctk
import db

def open_user_window(username):
    user_win = ctk.CTkToplevel()
    user_win.title("Felhasználók")
    user_win.geometry("500x450")

    frame = ctk.CTkFrame(master=user_win)
    frame.pack(pady=20, padx=40, fill="both", expand=True)

    ctk.CTkLabel(frame, text=f"Bejelentkezve: {username}", font=("Arial", 14, "bold")).pack(pady=10)

    ctk.CTkLabel(frame, text="Felhasználók listája:", font=("Arial", 12)).pack(pady=5)

    textbox = ctk.CTkTextbox(frame, width=400, height=250)
    textbox.pack(pady=10)

    users = db.get_all_users()
    for fullname, email, uname in users:
        textbox.insert("end", f"{fullname} ({uname}) - {email}\n")

    textbox.configure(state="disabled")  
