print("HOSGELDINIZ!...")
kullanici1="Ahmet"
parola1=1234
kullanici2="Zeynep"
parola2=4321
anaparaA=500
anaparaZ=654
def anamenu():
    listesecenek=["1.PARA CEKME","2.PARA YATIRMA" ,"3.PARA TRANSFERI", "4.HESAP BILGILERIM","5.CIKIS"]
    for liste in listesecenek:
        print(liste)


while True:
    try:
        soru1=int(input("GIRIS ICIN 1'e,CIKIS ICIN 2'ye BASINIZ."))
    except:
        print("lutfen sayisal ifade giriniz.")
        continue
    if soru1==1:
        print("Lutfen Sifrenizi Giriniz.")
        break
    elif soru1!=1 and soru1!=2: 
        print("lutfen gecerli rakami tuslayiniz.")
        continue
    else:
        print("cikisiniz gerceklestirildi.")
        continue
    
while True:
    parola=int(input("Sifreniz:"))
    kullanici_adi=input("kullanici adi giriniz:")
    if (kullanici_adi==kullanici1 and parola==parola1):
        print("HOSGELDINIZ AHMET BEY")
        pass
    elif (kullanici_adi==kullanici2 and parola==parola2):
        print("HOSGELDINIZ ZEYNEP HANIM")
        pass
    elif (kullanici_adi!=kullanici1 and parola==parola1 ):
        print("kullanici adiniz yanlis,lutfen tekrar deneyiniz.")
        continue
    elif (kullanici_adi==kullanici2 and parola!=parola2):
        print("yanlis parola.lutfen tekrar deneyiniz.")
        continue
    elif (kullanici_adi==kullanici1 and parola!=parola1 ):
        print("yanlis parola.lutfen tekrar deneyiniz.")
        continue
    elif (kullanici_adi!=kullanici2 and parola==parola2 ):
        print("kullanici adiniz yanlis,lutfen tekrar deneyiniz.")
    else:
        print("bilgileriniz yanlis.lufen tekrar deneyiniz.")
        continue
    while True:
        anamenu()
        secenek=int(input("LUTFEN YAPMAK ISTEDIGINIZ ISLEMI GIRINIZ:"))
        if secenek==1:
            try:
                soru2=int(input("cekmek istediginiz miktari giriniz:"))
            except:
                print("lutfen gecerli bir deger giriniz.")
                continue
            if kullanici1==kullanici_adi and soru2>anaparaA:
                print("yeterli bakiyeniz bulunmamaktadir.")
                continue
            if kullanici2==kullanici_adi and soru2>anaparaZ:
                print("yeterli bakiyeniz bulunmamaktadir.")
                continue

            elif soru2<=anaparaA and kullanici1==kullanici_adi:
                print("lutfen paranizi aliniz.")
                print("hesabinizdan",soru2,"TL kadar para cekilmistir.")
                kalan=anaparaA-soru2
                print("kalan miktar=",kalan,"TL")
            elif soru2<=anaparaZ and kullanici2==kullanici_adi:
                print("lutfen paranizi aliniz.")
                print("hesabinizdan",soru2,"TL kadar para cekilmistir.")
                kalan=anaparaZ-soru2
                print("kalan miktar=",kalan,"TL")
            
        elif secenek==2:
            while True:
                soru4=int(input("yatirmak istediginiz miktari giriniz:"))
                if soru4>0 and kullanici1==kullanici_adi:
                    print(soru4 ," TL hesabiniza eklenmistir.")
                    anaparaA=anaparaA+soru4
                    print("hesabinizdaki para=",anaparaA,"TL")
                    break
                elif soru4>0 and kullanici2==kullanici_adi:
                    print(soru4 ," TL hesabiniza eklenmistir.")
                    anaparaZ=anaparaZ+soru4
                    print("hesabinizdaki para=",anaparaZ,"TL")
                    break
                elif soru4<=0:
                    print("lutfen gecerli bir tutar giriniz.")
                    continue
                
        elif secenek==3:
            while True:
                soru5=int(input("gondermek istediginiz miktari giriniz:"))
                if soru5>anaparaA and kullanici1==kullanici_adi:
                    print("para transferiniz icin yeterli bakiyeniz yoktur.")
                    print("bakiyeniz=",anaparaA)
                    continue
                elif soru5>anaparaZ and kullanici2==kullanici_adi:
                    print("para transferiniz icin yeterli bakiyeniz yoktur.")
                    print("bakiyeniz=",anaparaZ)
                    continue
            
                elif soru5<=anaparaZ and kullanici2==kullanici_adi:
                    print("transfer islemi basari ile gerceklestirildi.")
                    anaparaZ=anaparaZ-soru5
                    print("kalan miktar=",anaparaZ,"TL")
                    break
                elif soru5<=anaparaA and kullanici1==kullanici_adi:
                    print("transfer islemi basari ile gerceklestirildi.")
                    anaparaA=anaparaA-soru5
                    print("kalan miktar=",anaparaA,"TL")
                    break
        elif secenek==4:
            print("_____GENCBANK_____")
            import time
            zaman=time.asctime()
            print(zaman)
            if parola==parola1:
                print("isim Soyisim=ahmet demir")
                print("parola:",parola1)
                print("hesaptaki miktar:",anaparaA,"TL")
            if parola==parola2:
                print("isim soyisim=zeynep esmer")
                print("parola:",parola2)
                print("hesaptaki miktar:",anaparaZ,"TL")
        elif secenek==5:
            print("cikis gerceklestirildi.")
            break
        else:
            print("lutfen gecerli bir ifade giriniz.")
            continue



    