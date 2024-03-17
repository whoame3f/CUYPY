import os
import random
os.system("cls")


n1 = 1
n2 = 4
ranger = random.randint(n1, n2)
# print(ranger)
welcome_message = "Welcome CUYPY Game"


print(f"#"*28)
print(f"#"*11,"💕🐹", "#"*11)
print(f"#"*4, welcome_message, "#"*4)
print(f"#"*11, "❤️❤️‍🔥", "#"*11)
print(f"#"*28)
print()
input_user = input("Masukkan nama anda 🥰: ")

bentuk_goa = "[__]"
goa_kosong = [bentuk_goa] * 4
goa_kopong = ' '.join(goa_kosong)
goa = goa_kosong.copy()
goa[ranger - 1] = "[🐹]"
goax = goa_kosong.copy()
goa_benar = ' '.join(goa)
nama = input_user.upper()


print(f'''
Hallo " {nama} " 😃! Coba perhatikan goa di bawah ini 👇!
{goa_kopong}
''')

pilihan = int(input(f"Menurut kamu di goa mana CUYPY berada 🧐? [1 / 2 / 3 / 4] : "))
confirm = input(f"Apakah anda yakin jawabannya {pilihan} 🫣? [y/n] ")
goax[pilihan - 1] = "[🐹]"
goa_salah = ' '.join(goax)

if confirm == 'n':
    exit()
if confirm == 'y':
    print(f"\n{goa_salah}")
    print(f"Pilihan anda adalah {pilihan}\n")
    
    while pilihan != ranger:
        if pilihan > ranger:
            print(f"{goa_salah}\nMaaf {nama}, anda Kalah!! jawban anda adalah {pilihan}, Sikit lagi lah Bang..😮‍💨\n")
        else:
            print(f"{goa_salah}\nMaaf {nama}, anda Kalah ❌😣!! jawban anda adalah {pilihan}, Sikit lagi lah Bang..\n")
        pilihan = int(input("Coba pilih lagi bang 🤯: "))
    print(f"{goa_benar}\nSelamat {nama}, anda Menang 🏆🎖️!! Posisi CUYPY ada di {ranger}, dan jawban anda adalah {pilihan}\n")
    
    # if pilihan == ranger:
    #     print(f"Selamat {nama}, anda menang🏆!! Posisi CUYPY ada di {ranger}, dan jawban anda adalah {pilihan}\n")
    # else:
    #     print(f"Maaf {nama}, anda salah!! Posisi CUYPY ada di {ranger}, dan jawban anda adalah {pilihan}\n")
        
else:
    print("Your ofside")
    exit()

