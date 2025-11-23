import mysql.connector
import hashlib

def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",      
            password="",
            database="teszt_db"
        )
    except mysql.connector.Error:
        return None

def hash_password(password):
    
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(fullname, email, username, password):
    conn = get_db_connection()
    if conn is None:
        return False, "Nincs adatbázis kapcsolat!"

    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (fullname, email, username, password) VALUES (%s, %s, %s, %s)",
            (fullname, email, username, hash_password(password))
        )
        conn.commit()
        return True, "Sikeres regisztráció!"
    except mysql.connector.IntegrityError:
        return False, "Ez az email vagy felhasználónév már létezik!"
    finally:
        cursor.close()
        conn.close()

def validate_user(username, password):
    conn = get_db_connection()
    if conn is None:
        return None

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                   (username, hash_password(password)))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_all_users():
    conn = get_db_connection()
    if conn is None:
        return []

    cursor = conn.cursor()
    cursor.execute("SELECT fullname, email, username FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
