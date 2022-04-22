# -*- coding: utf-8 -*-


#global_import
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import winsound
duration = 1000  # milliseconds
freq = 440  # Hz




driver_yolu="C:\\Users\\Ahmet\\Desktop\\chromedriver.exe"
browser = webdriver.Chrome(driver_yolu)
takip_say=int(input("Kaç adet coin takip edeceksiniz : "))
liste=[]
deger=[]
karsilastir=[]
for i in range(takip_say):
    tut=input("takip etmek istediğiniz " + str(i+1) + ". url adresi : ")
    tut2=input("Uyarı verilecek değer : ")
    deger.append(tut2)
    liste.append(tut)
a=1

for i in range(takip_say):
    browser.get(liste[i])
    time.sleep(5)
    fiyat=float(browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]").text)
    if float(deger[i])>fiyat:
        karsilastir.append("b")
    elif float(deger[i])<fiyat:
        karsilastir.append("k")
    else:
        print("eşit deger var tekrar deneyiniz hata kod : 1")
        break
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[i+1])
    

    
for i in range(takip_say):
    time.sleep(2)
    browser.refresh()
    browser.switch_to.window(browser.window_handles[i+1])
browser.close()

while a==1:
    print(1)
    for i in range(takip_say):
        print(2)
        if takip_say !=1:
            print(3)
            browser.switch_to.window(browser.window_handles[i])
        print(4)
        fiyat2=float(browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]").text)
        time.sleep()
        print(5)
        if karsilastir[i] == "b":
            print(6)
            if float(deger[i])>fiyat2:
                print(8)
                print("İstenilen Değere Ulaştı !!! : " + fiyat)
                print(liste[i])
                winsound.Beep(freq, duration)
        elif karsilastir[i] == "k":
            print(7)
            if float(deger[i])<fiyat2:
                print(9)
                print("İstenilen Değere Ulaştı !!! : " + fiyat)
                print(liste[i])
                winsound.Beep(freq, duration)
        else:
            print("Bilinmeyen hata oluştu hata kod : 2")
            break




#
#
#
#deger=float(browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]").text)
#a=1
#while a==1:
#    deger=float(browser.find_element_by_xpath("/html/body/div[2]/div[6]/div/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]").text)
#    print(deger)
#    time.sleep(1)
#    if deger>90:
#        break
#
#
#
#browser.execute_script("window.open('');") #yeni ekleme
#driver.switch_to.window(driver.window_handles[2]) #değişme