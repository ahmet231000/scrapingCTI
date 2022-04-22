from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def bul(liste,deger):
    for i in range(len(liste)):
        if liste[i] == deger:
            return True
    return False



def deep_web_guncelle(sayfa_no):
    print("Veri Kontrolü Sağlanıyor...")
    yeni_giris=0
    try:
        oku=pd.read_excel("deepwebveri.xlsx")
        print("Güncelleme İşlemi Başladı..!!!")
        yeni_giris=1
    except FileNotFoundError:
        Print("Dosya Bulunamadı!!!\nTüm Veriler İndiriliyor.")
        sayfa_no=999999
        
    listeler=["collapseobj_forumbit_1",
              "collapseobj_forumbit_129",
              "collapseobj_forumbit_75",
              "collapseobj_forumbit_91",
              "collapseobj_forumbit_148",
              "collapseobj_forumbit_154",
              "collapseobj_forumbit_37",
              "collapseobj_forumbit_59",]
    
    
    driver_yolu="C:\\Users\\Ahmet\\Desktop\\chromedriver.exe"
    browser = webdriver.Chrome(driver_yolu)
    browser.get("https://www.darbeturk.net/")
    
    #a=browser.find_element_by_id("collapseobj_forumbit_1")
    url=[]
    for liste_ad in listeler:
        veri=browser.find_element_by_id(liste_ad)
        elems = veri.find_elements_by_tag_name('a')
        for elem in elems:
            href = elem.get_attribute('href')
            if href is not None:
                url.append(href)
        
    for i in url:
        if i.find(".html") != -1:
            url.remove(i)
        
    for i in url:
        if i.find(".html") != -1:
            url.remove(i)
        
        
        
    rakamlar="0123456789"
    
    temiz_url=[]
    
    for i in url:
        for rakam in rakamlar:
            i=i.replace(rakam,"")
        i=i.replace("-","",1)
        if i == "https://www.darbeturk.net/d-islemler/":
            i="https://www.darbeturk.net/3d-islemler/"
        if i == "https://www.darbeturk.net/iptv-mu-link/":
            i="https://www.darbeturk.net/iptv-m3u-link/"
        if i == "https://www.darbeturk.net/mp-istek/":
            i="https://www.darbeturk.net/mp3-istek/"
        if i == "https://www.darbeturk.net/metin/":
            i="https://www.darbeturk.net/metin2/"
        temiz_url.append(i)
    

    basliklar=[]
    baslik_linkleri=[]
    
    
    
    
    for urller in temiz_url:#temiz_url
    
        for say in range(1,(int(sayfa_no)+1)):
            try:
                git=urller+"index"+str(say)+".html"
                print(git)
                browser.get(git)
                time.sleep(2)
                if browser.current_url != git and say != 1:
                    break
                
                
                
                a=browser.find_element_by_id("threadslist")
    
                des=a.find_elements_by_tag_name("tr")
                tut=0
                for i in des:
                    try:
                #    print(tut)
                #    tut=tut+1
                        tut=i.find_element_by_tag_name('a')
                        basliklar.append(tut.text)
                        baslik_linkleri.append(tut.get_attribute('href'))
                    except:
                        pass
            except:
                pass
    
    
    if yeni_giris == 0:
        data={"BASLIKLAR":basliklar,"URLLER":baslik_linkleri}
        data_son=pd.DataFrame(data)
        data_son
        data_son.to_excel("deepwebveri.xlsx",encoding='utf-8-sig')
    elif yeni_giris == 1:
        yeni_baslik=[]
        yeni_link=[]
        toplam=0
        for i in range(len(oku)):
            yeni_baslik.append(oku.loc[i,"BASLIKLAR"])
            yeni_link.append(oku.loc[i,"URLLER"])
        for i in range(len(basliklar)):
            if bul(yeni_baslik,basliklar[i]) == False:
                toplam+=1
                yeni_baslik.append(basliklar[i])
                yeni_link.append(baslik_linkleri[i])
        data={"BASLIKLAR":yeni_baslik,"URLLER":yeni_link}
        data_son=pd.DataFrame(data)
        data_son
        data_son.to_excel("deepwebveri.xlsx",encoding='utf-8-sig')
        print("Toplam Güncellenen Veri Sayısı : "+str(toplam))
        
    else:
        print("Bilinmeyen Bir Hata Oluştu.")
    browser.quit()







