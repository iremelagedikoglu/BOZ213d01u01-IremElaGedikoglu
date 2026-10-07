
import random
import time
import msvcrt
import tkinter as tk

print("================================")
print("        MINI SEFER")
print("================================")
print()
print("Düşmanı yen ve hayatta kal!")
print()

# OYUNCU
max_hp = 100
hp = 100

max_energy = 3
energy = 3

potions = 2
score = 0
defending = False

# RASTGELE DÜŞMAN
names = [
    "Demir Gardiyan",
    "Karanlık Canavar",
    "Kayıp Asker",
    "Taş Muhafız",
    "Çürümüş Şövalye"
]

enemy_name = random.choice(names)
enemy_max_hp = random.randint(80, 120)
enemy_hp = enemy_max_hp
enemy_attack = random.randint(12, 22)

print("Düşman:", enemy_name)
print("Can:", enemy_hp)
print("Saldırı:", enemy_attack)
print()


def get_action_from_form(current_hp, current_energy, current_potions, enemy_name, enemy_hp):
    root = tk.Tk()
    root.title("Mini Sefer - Hamle Seçim Formu")
    root.geometry("380x360")
    root.resizable(False, False)

    selected_action = {"value": ""}

    def submit(event=None):
        val = entry.get().strip()
        if val in ["1", "2", "3", "4"]:
            selected_action["value"] = val
            root.destroy()
        else:
            lbl_error.config(text="Lütfen geçerli bir hamle girin (1, 2, 3 veya 4)!", fg="red")

    # Form Başlığı ve Bilgi Alanı
    lbl_title = tk.Label(root, text="HAMLE SEÇİMİ", font=("Arial", 13, "bold"))
    lbl_title.pack(pady=6)

    status_text = (
        f"Oyuncu Can: {current_hp} | Enerji: {current_energy} | İksir: {current_potions}\n"
        f"Düşman: {enemy_name} (Can: {enemy_hp})"
    )
    lbl_status = tk.Label(root, text=status_text, font=("Arial", 9), fg="#333333", justify="center")
    lbl_status.pack(pady=4)

    # Seçenekler Rehberi
    options_text = (
        "1  →  Temel Saldırı (0 Enerji - 20 Hasar)\n"
        "2  →  Ağır Saldırı (2 Enerji - 35 Hasar)\n"
        "3  →  İksir Kullan (1 Enerji - +30 Can)\n"
        "4  →  Savun (Hasarı Yarıya İndir)"
    )
    lbl_options = tk.Label(root, text=options_text, font=("Arial", 9, "bold"), justify="left", relief="groove", bd=2, padx=10, pady=8)
    lbl_options.pack(pady=8)

    # Form Giriş Alanı
    lbl_prompt = tk.Label(root, text="Hamle Numaranızı Girin (1-4):", font=("Arial", 10))
    lbl_prompt.pack(pady=2)

    entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
    entry.pack(pady=4)
    entry.focus()
    entry.bind("<Return>", submit)

    lbl_error = tk.Label(root, text="", font=("Arial", 8))
    lbl_error.pack(pady=2)

    # Form Onay Butonu
    btn_submit = tk.Button(root, text="Hamleyi Onayla (Enter)", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=submit, padx=10, pady=4)
    btn_submit.pack(pady=6)

    root.mainloop()
    return selected_action["value"]


def show_stats():
    print("--------------------------------")
    print("CAN:", hp, "/", max_hp)
    print("ENERJİ:", energy, "/", max_energy)
    print("İKSİR:", potions)
    print("SKOR:", score)
    print("--------------------------------")


def basic_attack():
    global enemy_hp

    damage = 20
    enemy_hp -= damage

    if enemy_hp < 0:
        enemy_hp = 0

    print("Temel Saldırı!")
    print("Hasar:", damage)


def heavy_attack():
    global enemy_hp
    global energy

    if energy < 2:
        print("Yeterli enerjin yok!")
        return False

    damage = 35
    enemy_hp -= damage
    energy -= 2

    if enemy_hp < 0:
        enemy_hp = 0

    print("AĞIR SALDIRI!")
    print("Hasar:", damage)
    print("Enerji -2")

    return True


def heal():
    global hp
    global energy
    global potions

    if potions <= 0:
        print("Hiç iksirin kalmadı!")
        return False

    if energy < 1:
        print("Yeterli enerjin yok!")
        return False

    hp += 30

    if hp > max_hp:
        hp = max_hp

    potions -= 1
    energy -= 1

    print("İksir kullandın.")
    print("30 can yenilendi.")
    print("Enerji -1")

    return True


def enemy_attack_phase():
    global hp
    global energy
    global defending
    global enemy_hp
    global score

    print()
    print(enemy_name, "saldırıyor!")
    print("Doğru zamanda BOŞLUK tuşuna bas!")
    print()

    total_steps = 20
    pressed = False
    position = 0

    for i in range(total_steps):

        bar = ""

        for j in range(total_steps):
            if j <= i:
                bar += "█"
            else:
                bar += "░"

        if i < 10:
            zone = "PARRY"
        elif i < 18:
            zone = "KAÇIŞ"
        else:
            zone = "VURULMA"

        print("\r[" + bar + "] " + zone, end="")

        start = time.time()

        while time.time() - start < 0.12:

            if msvcrt.kbhit():
                key = msvcrt.getch()

                if key == b" ":
                    pressed = True
                    position = i
                    break

        if pressed:
            break

    print()

    # OYUNCU BOŞLUĞA BASTI
    if pressed:

        # PARRY
        if position < 10:
            print()
            print("!!! MÜKEMMEL PARRY !!!")
            print("Karşı saldırı!")

            counter = 20
            enemy_hp -= counter
            score += 15

            if enemy_hp < 0:
                enemy_hp = 0

            print("Karşı saldırı hasarı:", counter)

        # KAÇIŞ
        elif position < 18:
            print()
            print("KAÇIŞ!")

            if energy > 0:
                energy -= 1
                print("Saldırıdan kaçtın.")
                print("Enerji -1")
            else:
                print("Enerjin yok!")
                print("Kaçış başarısız!")

                damage = enemy_attack

                if defending:
                    damage = damage // 2

                hp -= damage
                print("Hasar:", damage)

        # ÇOK GEÇ
        else:
            print()
            print("ÇOK GEÇ!")

            damage = enemy_attack

            if defending:
                damage = damage // 2
                print("SAVUNMA hasarı azalttı!")

            hp -= damage
            print("Hasar:", damage)

    # OYUNCU BASMADI
    else:
        print()
        print("Zamanında tepki veremedin!")

        damage = enemy_attack

        if defending:
            damage = damage // 2
            print("SAVUNMA hasarı azalttı!")

        hp -= damage
        print("Hasar:", damage)

    if hp < 0:
        hp = 0

    defending = False


# ANA OYUN DÖNGÜSÜ

while hp > 0 and enemy_hp > 0:

    show_stats()

    print()
    print("DÜŞMAN:", enemy_name)
    print("DÜŞMAN CANI:", enemy_hp, "/", enemy_max_hp)
    print()

    # Standart input() yerine form girişi tetiklenir:
    action = get_action_from_form(hp, energy, potions, enemy_name, enemy_hp)

    # TEMEL SALDIRI
    if action == "1":
        basic_attack()

    # AĞIR SALDIRI
    elif action == "2":
        if not heavy_attack():
            continue

    # İKSİR
    elif action == "3":
        if not heal():
            continue

    # SAVUNMA
    elif action == "4":
        defending = True
        print("Savunma pozisyonu aldın.")

    else:
        print("Geçersiz seçim!")
        continue

    # DÜŞMAN ÖLDÜ MÜ?
    if enemy_hp <= 0:
        break

    # DÜŞMAN TURU
    enemy_attack_phase()

    # ENERJİ YENİLEME
    if energy < max_energy:
        energy += 1

    print()


# OYUN SONU

print()
print("================================")

if hp <= 0:
    print("          ÖLDÜN")
    print("================================")
    print("Son Skor:", score)

else:
    print("       DÜŞMAN YENİLDİ!")
    print("================================")
    print()
    print("Yendiğin düşman:", enemy_name)
    print("Son Skor:", score)
    print("Kalan Can:", hp)
    print()
    print("           ZAFER!")
