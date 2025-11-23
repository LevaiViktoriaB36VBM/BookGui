Lévai Viktória_B36VBM

Ez a projekt felhasználói regisztrációt és bejelentkezést valósít meg MySQL adatbázis segítségével (XAMPP környezetben). Az alkalmazás modern, letisztult felületet biztosít a customtkinter könyvtár használatával.

Funkciók
Bejelentkezés felhasználónévvel és jelszóval
Új felhasználók regisztrációja (teljes név, email, felhasználónév, jelszó, jelszó megerősítése)
Jelszó titkosítása SHA256 algoritmussal
Email formátum ellenőrzése regisztráció során
Adatbázis kapcsolat ellenőrzése és státusz kijelzése (zöld/piros szöveg)
Ha nincs adatbázis kapcsolat, a bejelentkezés és regisztráció gombok letiltásra kerülnek
Felhasználói lista megjelenítése sikeres belépés után (név, felhasználónév, email)
Modern dark mode felhasználói felület (customtkinter)

Felhasznált Python csomagok
mysql-connector-python – MySQL adatbázis kezeléséhez
customtkinter – modern grafikus felület készítéséhez
tkinter – alap GUI funkciók (pl. messagebox)
hashlib – jelszó hash-eléséhez (SHA256)
re – email cím validáláshoz reguláris kifejezésekkel
