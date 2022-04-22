#global_import
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import json




###############################################################################

def telnosorgu(tel):
    #import requests
    #from bs4 import BeautifulSoup
    url="http://www.nosorgulama.com/tel/"+tel
    gelen=requests.get(url)
    haber=BeautifulSoup(gelen.content,"html.parser")
    global y_sayisi,tehlikeli_bildirimi,supheli,guvenli,belirsiz
    try:
        y_sayisi=haber.find_all("span",{"id":"countyorum"})[0].text
    except:
        y_sayisi="0"
    tehlikeli_bildirimi=len(haber.find_all("span",{"class":"tehlikeli"}))
    
    url="https://www.suphelinumara.com/numara/"+tel
    gelen=requests.get(url)
    haber2=BeautifulSoup(gelen.content,"html.parser")
    supheli=haber2.find_all("a",{"class":"btn btn-md danger rounded"})[0].text.replace(" Şüpheli (","").replace(")","")
    guvenli=haber2.find_all("a",{"class":"btn btn-md success rounded"})[0].text.replace("Güvenli (","").replace(")","")
    belirsiz=haber2.find_all("a",{"btn btn-md dker rounded"})[0].text.replace("Belirsiz (","").replace(")","")
    suphelino_yorum=haber2.find_all("div",{"class":"box-header text-center"})[0].text.replace("\nNumara hakkında yorum yap (","").replace(")\n","")
    
    try:
        print("\n\nİlgili telefon numarası www.nosorgulama.com üzerinde "+y_sayisi+" kere yorumlanmıştır.\n"+haber.find_all("div",{"class":"total-rating star1"})[0].text.split()[3]+" kişi tarafından değerlendirilmiş olup aldığı puan : "+haber.find_all("div",{"class":"total-rating star1"})[0].text.split()[1]+"/5")
    except:
        try:
            print("\n\nİlgili telefon numarası nosorgulama.com üzerinde "+y_sayisi+" kere yorumlanmıştır.\n"+haber.find_all("div",{"class":"total-rating star2"})[0].text.split()[3]+" kişi tarafından değerlendirilmiş olup aldığı puan : "+haber.find_all("div",{"class":"total-rating star2"})[0].text.split()[1]+"/5")
        except:
            print("\n\nİlgili telefon numarası nosourgula.com üzerinde "+y_sayisi+" kere yorumlanmıştır.\n0 kişi tarafından değerlendirilmiş olup aldığı puan : 0")
    print("\nİlgili telefon numarası www.suphelinumara.com üzerinde " + suphelino_yorum +" kere yorumlanmıştır.\nŞüpheli:"+supheli+" Güvenli:"+guvenli+" Belirsiz:"+belirsiz+" Olarak bildirilmiştir.")

###############################################################################




def tip_bul(ip):
    url_bulucu=["www",":",",","http","com",";","org",".tr",".net"]
    tut = 0
    asd="0123456789"
    if len(ip) == 11 and ip[0] == "0":
        for i in ip:
            if asd.find(i) != -1:
                tut+=1
    if tut==11:
        girilen_tip="tel"
        return girilen_tip
    else:
        tut=0
        for i in ip:
            if i == ".":
                tut = tut + 1
            #elif i == ":" or i == "," or i == "http" or i == "www" or i == "com" or i == ";" or i == "org" or i == ".tr" or i == ".net" or i == ".gov":
            else:
                for j in url_bulucu:
                    if ip.find(j) != -1:
                        tut = tut - 1
        
        if tut == 3:
            girilen_tip="ip"
            return girilen_tip
        else:
            tut=0
            for i in ip:
                if i == "." or i == ":" or i == "," or i == "http" or i == "www" or i == "com" or i == ";" or i == "org" or i == ".tr" or i == ".net" or i == ".gov":
                    tut = tut - 1
            if tut == 0:
                girilen_tip = "hash"
                return girilen_tip
            else:
                girilen_tip = "url"
                return girilen_tip


###############################################################################

def dosyabul(dosya_isim):
    try:
        if dosya_isim[(len(dosya_isim)-3):len(dosya_isim)] == "exe":
            url="https://www.exefiles.com/tr/exe/" + dosya_isim[0:(len(dosya_isim)-4)] + "-exe/"
            gelen=requests.get(url)
            if gelen.status_code == 200:
                print("---------------------------------------------------------------")
                print(dosya_isim + " dosyası ne işe yarar ? : "+url)
                
            
            
            url="https://www.file.net/process/" + dosya_isim + ".html"
            gelen=requests.get(url)
            if gelen.status_code == 200:
                print("---------------------------------------------------------------")
                print(dosya_isim + " dosyası ne işe yarar ? : "+url)
                
                
                
        elif dosya_isim[(len(dosya_isim)-3):len(dosya_isim)] == "dll":
            url="https://www.exefiles.com/tr/dll/" + dosya_isim[0:(len(dosya_isim)-4)] + "-dll/"
            gelen=requests.get(url)
            if gelen.status_code == 200:
                print("---------------------------------------------------------------")
                print(dosya_isim + " dosyası ne işe yarar ? : "+url)
                
                
            url="https://www.opendll.com/index.php?search="+dosya_isim
            gelen=requests.get(url)
            if gelen.text.find("No result found for") != -1:
                print("---------------------------------------------------------------")
                print(dosya_isim + " dosyası ne işe yarar ? : "+url)
                
                
                
            url="https://www.dll.gen.tr/" + dosya_isim.replace(".dll","")
            gelen=requests.get(url,headers={"User-Agent": "XY"})
            if gelen.status_code == 200:
                print("---------------------------------------------------------------")
                print(dosya_isim + " dosyası ne işe yarar ? : "+url)
                
    except:
        pass


###############################################################################



def host_sorgu(ip):
    try:
        url="https://ipinfo.io/"+ip
        gelen=requests.get(url)
        data=json.loads(gelen.text)
        whois=data["org"][(data["org"].find(" ")+1):]+" - "+ data["timezone"]
        print("Whois Kaydı : "+whois)
        return whois
    except:
        pass








###############################################################################
                
def ibm_ip(ip):
    browser.get("https://exchange.xforce.ibmcloud.com/ip/"+ip)

    try:
        a=browser.find_element_by_class_name("instantresultwrapper")
        while a.find_element_by_class_name("scorebackgroundfilter.numtitle").text == "Unknown":
            time.sleep(1)
        print("IBM Risk Skoru : "+a.find_element_by_class_name("scorebackgroundfilter.numtitle").text)
        return a.find_element_by_class_name("scorebackgroundfilter.numtitle").text

    except:
        try:
            time.sleep(3)
            a=browser.find_element_by_class_name("instantresultwrapper")
            while a.find_element_by_class_name("scorebackgroundfilter.numtitle").text == "Unknown":
                time.sleep(1)
            print("IBM Risk Skoru : "+a.find_element_by_class_name("scorebackgroundfilter.numtitle").text)
            return a.find_element_by_class_name("scorebackgroundfilter.numtitle").text
        except:
            pass





def abuse_ip(ip):
    abuse="0"
    url="https://www.abuseipdb.com/check/"+ip
    gelen=requests.get(url)
    haber=BeautifulSoup(gelen.content,"html.parser")
    try:
        for i in haber.find_all("div",{"class":"well"}):
            for j in i.find_all("p"):
                for k in j.find_all("b"):
                    abuse=k.text
    except:
        abuse=0
        
    try:
        print("AbuseIPDB Skoru : "+abuse.replace("%",""))
        return abuse.replace("%","")
    except:
        print("AbuseIPDB Skoru : 0")
        return "0"
def github_ip(ip):
    url="https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt"
    
    gelen=requests.get(url)
    haber=BeautifulSoup(gelen.content,"html.parser")
    if haber.text.find(ip)==-1:
        print("Github Risk Skoru : 0")
        return "0"
    else:
        deneme=haber.text.split()
        for i in range(len(deneme)):
            if deneme[i]==ip:
                print("Github Risk Skoru : "+(deneme[i+1]))
                return deneme[i+1]
def virustotal_ip(ip):
    def expand_shadow_element(element):
        shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    browser.get("https://www.virustotal.com/gui/ip-address/"+ip+"/detection")
    root1 = browser.find_element_by_tag_name('ip-address-view')
    shadow_root1 = expand_shadow_element(root1)

    root2 = shadow_root1.find_element_by_css_selector('vt-ui-main-generic-report')
    shadow_root2 = expand_shadow_element(root2)

    root3 = shadow_root2.find_element_by_css_selector('vt-ui-detections-widget')
    shadow_root3 = expand_shadow_element(root3)

    print("Virustotal Risk Skoru : "+shadow_root3.find_element_by_class_name("positives").text)
    return shadow_root3.find_element_by_class_name("positives").text
###############################################################################
    
def ibm_hash(ip):
    browser.get("https://exchange.xforce.ibmcloud.com/malware/"+ip)

    try:
        a=browser.find_element_by_class_name("instantresultwrapper")
        print("IBM Risk Skoru : "+a.find_element_by_class_name("scorebackgroundfilter.numtitle").text)
        return a.find_element_by_class_name("scorebackgroundfilter.numtitle").text
    except:
        time.sleep(5)
        try:
            a=browser.find_element_by_class_name("instantresultwrapper")
            print("IBM Risk Skoru : "+a.find_element_by_class_name("scorebackgroundfilter.numtitle").text)
            return a.find_element_by_class_name("scorebackgroundfilter.numtitle").text
        except:
            pass

def virustotal_hash(ip):
    try:
        
        def expand_shadow_element(element):
            shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
            return shadow_root
    
        browser.get("https://www.virustotal.com/gui/file/"+ip+"/detection")
        time.sleep(2)
        root1 = browser.find_element_by_tag_name('file-view')
        shadow_root1 = expand_shadow_element(root1)
    
        root2 = shadow_root1.find_element_by_css_selector('vt-ui-main-generic-report')
        shadow_root2 = expand_shadow_element(root2)
    
        root3 = shadow_root2.find_element_by_css_selector('vt-ui-detections-widget')
        shadow_root3 = expand_shadow_element(root3)
    
    
        print("Virustotal Risk Skoru : "+shadow_root3.find_element_by_class_name("positives").text)
        return shadow_root3.find_element_by_class_name("positives").text
    except:
        pass
    

    
def virustotal_hash_dosya_ismi(ip):
    try:
        def expand_shadow_element(element):
            shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
            return shadow_root
    
        root1 = browser.find_element_by_tag_name('file-view')
        shadow_root1 = expand_shadow_element(root1)
    
        root2 = shadow_root1.find_element_by_css_selector('vt-ui-main-generic-report')
        shadow_root2 = expand_shadow_element(root2)
        
        root3 = shadow_root2.find_element_by_css_selector('header')
        shadow_root3 = expand_shadow_element(root3)
        
        isim=root3.text
        isim=isim.split("\n")[6]
    
        print("Dosya İsmi : "+isim)
        return isim
    except:
        pass
    
###############################################################################
    
def ibm_url(ip):
    browser.get("https://exchange.xforce.ibmcloud.com/url/"+ip)

    try:
        a=browser.find_element_by_class_name("instantresultwrapper")
        print("IBM Risk Skoru : "+a.find_element_by_class_name("scorebackgroundfilter.numtitle").text)
        return a.find_element_by_class_name("scorebackgroundfilter.numtitle").text
    except:
        try:
            a=browser.find_element_by_class_name("instantresultwrapper")
            print("IBM Risk Skoru : "+a.find_element_by_class_name("scorebackgroundfilter.numtitle").text)
            return a.find_element_by_class_name("scorebackgroundfilter.numtitle").text
        except:
            pass



def abuse_url(ip):
    abuse="0"
    url="https://www.abuseipdb.com/check/"+ip
    gelen=requests.get(url)
    haber=BeautifulSoup(gelen.content,"html.parser")
    try:
        for i in haber.find_all("div",{"class":"well"}):
            for j in i.find_all("p"):
                for k in j.find_all("b"):
                    abuse=k.text
    except:
        abuse=0
    
    print("AbuseIPDB Skoru : "+abuse.replace("%",""))
    return abuse.replace("%","")
    
    
    
    
def virustotal_url(ip):
    def expand_shadow_element(element):
        shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    browser.get("https://www.virustotal.com/gui/domain/"+ip+"/detection")
    try:
        root1 = browser.find_element_by_tag_name('domain-view')
        shadow_root1 = expand_shadow_element(root1)

        root2 = shadow_root1.find_element_by_css_selector('vt-ui-main-generic-report')
        shadow_root2 = expand_shadow_element(root2)
        
        root3 = shadow_root2.find_element_by_css_selector('vt-ui-detections-widget')
        shadow_root3 = expand_shadow_element(root3)
    except:
        ip=ip.replace(":","%253A").replace("/","%252F")
        browser.get("https://www.virustotal.com/gui/search/"+ip)
        root1 = browser.find_element_by_tag_name('url-view')
        shadow_root1 = expand_shadow_element(root1)

        root2 = shadow_root1.find_element_by_css_selector('vt-ui-main-generic-report')
        shadow_root2 = expand_shadow_element(root2)
        
        root3 = shadow_root2.find_element_by_css_selector('vt-ui-detections-widget')
        shadow_root3 = expand_shadow_element(root3)
    print("Virustotal Risk Skoru : "+shadow_root3.find_element_by_class_name("positives").text)
    return shadow_root3.find_element_by_class_name("positives").text
    
###############################################################################
    
    
    
    
    
###############################################################################





###############################################################################02162270877

giris=input("Hash/Url/Ip/Domain/Telefon Numarası sorgulmak için 1'e Basınız.\nDeepWeb Sorgusu İçin 2'ye Basın\nToplu Sorgu İçin 3'e Basınız\nIP Bildirmek İçin 4'e Basınız\nSeçenek : ")

if giris =="2":
    secenek=input("Sorgu Yapmak için 1'e Basınız.\nGüncellemek İçin 2'ye Basınız. \nSeçenek : ")
    if secenek == "1":
        print("Lütfen Bekleyin Veriler Yükleniyor...")
        import deepwebsorgu
    elif secenek == "2":
        print("Güncelleme hazırlanıyor.")
        import deepweb
        sayfa_no=int(input("Güncellemek İstediğiniz Sayfayı Giriniz : "))
        deepweb.deep_web_guncelle(sayfa_no)
    else:
        print("Yanlış Tuşlama Yaptınız !!!")
###############################################################################   
elif giris == "1":
    ip=str(input("IP Adresi, Hash, Url veya Telefon Numarası(0555xx) giriniz: "))
    girilen_tip = tip_bul(ip)
    if girilen_tip != "tel":
        driver_yolu="C:\\Users\\Ahmet\\Desktop\\chromedriver.exe"
        browser = webdriver.Chrome(driver_yolu)
    
###############################################################################  
    if girilen_tip == "ip":
        host_sorgu(ip)
        ibm_ip(ip)
        abuse_ip(ip)
        github_ip(ip)
        virustotal_ip(ip)
        import ipkaydet
        ipkaydet.ip_sorgula(ip)
        browser.quit()
    
###############################################################################
    
    elif girilen_tip == "hash":
    
        ibm_hash(ip)
        virustotal_hash(ip)
        tut=virustotal_hash_dosya_ismi(ip)
        dosyabul(tut)
        browser.quit()
    
###############################################################################
        
    
    elif girilen_tip == "url":
    
        
        ibm_url(ip)
        abuse_url(ip)
        virustotal_url(ip)
        browser.quit()
        
###############################################################################
        
    
    elif girilen_tip == "tel":
    
        global y_sayisi,tehlikeli_bildirimi,supheli,guvenli,belirsiz
        telnosorgu(ip)
    
    


elif giris=="3":
    tip=input("IP sorgusu için 1'e basınız\nHash sorgusu için 2'ye basınız\nURL/Domain sorgusu için 3'e basınız\nSeçenek : ")
    dosya_ismi=input("Excel Dosyasının İsmini Giriniz(ör: IP.xlsx) : ")
    try:
        oku=pd.read_excel(dosya_ismi,names=["Veri"])
        driver_yolu="C:\\Users\\Ahmet\\Desktop\\chromedriver.exe"
        browser = webdriver.Chrome(driver_yolu)
        if tip == "1":
            toplu_ip=[]
            toplu_ip_host=[]
            toplu_ip_vt=[]
            toplu_ip_ibm=[]
            toplu_ip_abuse=[]
            toplu_ip_github=[]
            for i in range(len(oku)):
                toplu_ip_host.append(host_sorgu(oku.loc[i,"Veri"]))
                toplu_ip_abuse.append(abuse_ip(oku.loc[i,"Veri"]))
                toplu_ip_github.append(github_ip(oku.loc[i,"Veri"]))
                toplu_ip_ibm.append(ibm_ip(oku.loc[i,"Veri"]))
                toplu_ip_vt.append(virustotal_ip(oku.loc[i,"Veri"]))
                toplu_ip.append(oku.loc[i,"Veri"])
            data={"IP ADRESLERİ":toplu_ip,"Whois Bilgileri":toplu_ip_host,"Virus Total":toplu_ip_vt,"IBM X-Force":toplu_ip_ibm,"AbuseIPDB":toplu_ip_abuse,"Github":toplu_ip_github}
            data_son=pd.DataFrame(data)
            data_son
            data_son.to_excel("IP_SORGU.xlsx",encoding='utf-8-sig')
            print('Sonuçlar "IP_SORGU.xlsx" Dosyasına Kaydedildi.')
        elif tip == "2":
            toplu_hash=[]
            toplu_hash_ibm=[]
            toplu_hash_vt=[]
            toplu_hash_vt_isim=[]
            for i in range(len(oku)):
                toplu_hash.append(oku.loc[i,"Veri"])
                toplu_hash_ibm.append(ibm_hash(oku.loc[i,"Veri"]))
                toplu_hash_vt.append(virustotal_hash(oku.loc[i,"Veri"]))
                toplu_hash_vt_isim.append(virustotal_hash_dosya_ismi(oku.loc[i,"Veri"]))
                
            data={"HASH":toplu_hash,"IBM X-Force":toplu_hash_ibm,"Virus Total":toplu_hash_vt,"Dosya İsmi":toplu_hash_vt_isim}
            data_son=pd.DataFrame(data)
            data_son
            data_son.to_excel("HASH_SORGU.xlsx",encoding='utf-8-sig')
            print('Sonuçlar "HASH_SORGU.xlsx" Dosyasına Kaydedildi.')
        elif tip == "3":
            toplu_url=[]
            toplu_url_vt=[]
            toplu_url_ibm=[]
            toplu_url_abuse=[]
            for i in range(len(oku)):
                toplu_url_abuse.append(abuse_url(oku.loc[i,"Veri"]))
                toplu_url_ibm.append(ibm_url(oku.loc[i,"Veri"]))
                toplu_url_vt.append(virustotal_url(oku.loc[i,"Veri"]))
                toplu_url.append(oku.loc[i,"Veri"])
            data={"URL/DOMAIN":toplu_url,"Virus Total":toplu_url_vt,"IBM X-Force":toplu_url_ibm,"AbuseIPDB":toplu_url_abuse}
            data_son=pd.DataFrame(data)
            data_son
            data_son.to_excel("URL_DOMAIN_SORGU.xlsx",encoding='utf-8-sig')
            print('Sonuçlar "URL_DOMAIN_SORGU.xlsx" Dosyasına Kaydedildi.')
        else:
            print("HATALI TUŞLAMA YAPTINIZ..!!!")
    except FileNotFoundError:
        print("Dosya Bulunamadı..!!!")
#    except:
#        print("Bilinmeyen Bir Hata Oluştu.!!")
    
    
elif giris=="4":
    ip=input("IP Adresi Giriniz : ")
    if tip_bul(ip) == "ip":
        skor=input("Risk Skoru Giriniz(0-10) : ")
        import ipkaydet
        ipkaydet.ekle(ip,skor)
    else:
        print("Lütfen IP Adresi Giriniz..!!")
    
    
    
else:
    print("Yanlış Tuşlama Yaptınız !!!")
    
