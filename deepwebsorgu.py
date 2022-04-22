import pandas as pd
try:
    oku=pd.read_excel("deepwebveri.xlsx")
    baslik=[]
    link=[]
    del oku["Unnamed: 0"]
    bul=input("Aranacak Kelimeleri Arasında Boşluk Olacak Şekilde Giriniz : ")
    sapma_payi=int(input("Aradığınız Kelimelerden En Az Kaçtanesini İçersin : "))
    a=bul.split()
    for i in range(len(oku)):
        try:
            tutucu=0
            for j in range(len(a)):
                if oku.loc[i,"BASLIKLAR"].lower().find(a[j].lower()) != -1:
                    tutucu+=1
            if tutucu>=sapma_payi:
                baslik.append(oku.loc[i,"BASLIKLAR"])
                link.append(oku.loc[i,"URLLER"])
                print(oku.loc[i,"BASLIKLAR"])
                print(oku.loc[i,"URLLER"])
                print("------------------------------------------")
        except:
            pass
    if len(baslik) != 0: 
        data={"BASLIKLAR":baslik,"URLLER":link}
        data_son=pd.DataFrame(data)
        data_son
        data_son.to_excel("deepweb_bulunmus_veri.xlsx",encoding='utf-8-sig')
        print('Bulunan Veriler "deepweb_bulunmus_veri.xlsx" Dosyasına Kayıt Edildi.')
    else:
        print("Herhangibir Veri Bulunamamıştır.")
except FileNotFoundError:
    print("Dosya Bulunamadı.")
except:
    print("Deepweb Sotguna Bilinmeyen Bir Hata Oluştu..!!")
