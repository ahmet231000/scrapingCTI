class deneme():
    def__init__(self,tel):
        self.tel=tel
    def telnosorgu(tel,self):
        #import requests
        #from bs4 import BeautifulSoup
        url="http://www.nosorgulama.com/tel/"+self.tel
        gelen=requests.get(url)
        haber=BeautifulSoup(gelen.content,"html.parser")
        #global y_sayisi
        y_sayisi=haber.find_all("span",{"id":"countyorum"})[0].text
        #global tehlikeli_bildirimi
        tehlikeli_bildirimi=len(haber.find_all("span",{"class":"tehlikeli"}))