#egowithm16 tarafından eğlence amaçlı geliştirilmiştir. discord: stirner#4555

import random

ch = ["taş","kağıt","makas"]

cp = random.choice(ch)

tur = 0

bot = 0

oyuncu = 0

print("Oyuna başlamadan önce bilgilendirme:\nOyun büyük küçük harflere duyarlı değildir. İstediğiniz gibi yazabilirsiniz.\n")

while True:

    ch = ["taş", "kağıt", "makas"]

    pl = input("Taş, kağıt, makas.").lower()

    if pl not in ch:
        pl = input("Geçerli bir kelime belirleyiniz.").lower()

    if pl == cp:
        print("Berabere.")
        tur = tur + 1
    elif pl == "taş" and cp == "makas":
        print("Oyuncu kazandı")
        tur = tur + 1
        oyuncu = oyuncu + 1
    elif pl == "taş" and cp == "kağıt":
        print("Bot kazandı")
        tur = tur + 1
        bot = bot + 1
    elif pl == "makas" and cp == "kağıt":
        print("Oyuncu kazandı")
        tur = tur + 1
        oyuncu = oyuncu + 1
    elif pl == "makas" and cp == "taş":
        print("Bot kazandı")
        tur = tur + 1
        bot = bot + 1
    elif pl == "kağıt" and cp == "taş":
        print("Oyuncu kazandı")
        tur = tur + 1
        oyuncu = oyuncu +1
    elif pl == "kağıt" and cp == "makas":
        print("Bot kazandı")
        tur = tur + 1
        bot = bot + 1
    if tur == 3:
        print("Oyun bitti.\n")
        if oyuncu > bot:
            print("Oyunu oyuncu kazandı\n")
        elif oyuncu < bot:
            print("Oyunu bot kazandı\n")
        elif oyuncu == bot:
            print("Oyun berabere bitti\n")
        baştan_başlatma = input("Yeniden oynamak ister misiniz? (E)vet/(H)ayır\n").upper()
        if baştan_başlatma == "E":
            tur = 0
            continue
        elif baştan_başlatma == "H":
            print("Birdahaki sefere görüşürüz!")
            break








