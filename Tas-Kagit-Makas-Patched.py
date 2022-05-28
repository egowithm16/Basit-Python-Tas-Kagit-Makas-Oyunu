#egowithm16 tarafından eğlence amaçlı geliştirilmiştir. discord: stirner#4555

import random

tur = 0

bot = 0

oyuncu = 0

print("Oyuna başlamadan önce bilgilendirme:\nOyun büyük küçük harflere duyarlı değildir. İstediğiniz gibi yazabilirsiniz.\n")

while True:

    ch = ["taş","kağıt","makas"]

    cp = random.choice(ch)

    pl = ""
    
    while pl not in ch:
        pl = input("Taş, kağıt, makas.").lower()
        if pl in ch:
            continue

    if pl == cp:
        print("Berabere.")
        tur = tur + 1

    elif pl == "taş":
        if cp == "makas":
            print("Oyuncu kazandı")
            tur = tur + 1
            oyuncu = oyuncu + 1
        elif cp == "kağıt":
            print("Bot kazandı")
            tur = tur + 1
            bot = bot + 1

    elif pl == "makas":
        if cp == "kağıt":
            print("Oyuncu kazandı")
            tur = tur + 1
            oyuncu = oyuncu + 1
        elif cp == "taş":
            print("Bot kazandı")
            tur = tur + 1
            bot = bot + 1

    elif pl == "kağıt":
        if cp == "taş":
            print("Oyuncu kazandı")
            tur = tur + 1
            oyuncu = oyuncu +1
        elif cp == "makas":
            print("Bot kazandı")
            tur = tur + 1
            oyuncu = oyuncu + 1

    if tur == 3:
        print("Oyun bitti.\n")

        if oyuncu > bot:
            print("\nOyunu oyuncu kazandı\n")

        elif oyuncu < bot:
            print("\nOyunu bot kazandı\n")

        elif oyuncu == bot:
            print("Tur berabere bitti\n")

        answers = ["E","H"]
        
        baştan_başlatma = input("Yeniden oynamak ister misiniz? (E)vet/(H)ayır\n").upper()

        if baştan_başlatma == "E":
            tur = 0
            oyuncu = 0
            bot = 0
            continue

        elif baştan_başlatma == "H":
            print("Birdahaki sefere görüşürüz.")
            break

        else:
            while baştan_başlatma not in answers:
                baştan_başlatma = input("Yeniden oynamak ister misiniz? (E)vet/(H)ayır\n").upper()
                if baştan_başlatma in answers:
                    if baştan_başlatma == "E":
                        tur = 0
                        bot = 0
                        oyuncu = 0
                        continue
                    elif baştan_başlatma == "H":
                        print("Birdahaki sefere görüşürüz.")
                        break
        if baştan_başlatma == "H":
            break