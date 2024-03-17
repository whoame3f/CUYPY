import os
import random
os.system("cls")


n1 = 1
n2 = 4
ranger = random.randint(n1 , n2)


bentuk_goa = "[_]"
goa_kosong = [bentuk_goa] * 4
goa = goa_kosong.copy()
goa[ranger - 1] = "[o.o]"
jadi = ' '.join(goa)
print(type(jadi))
print(jadi)