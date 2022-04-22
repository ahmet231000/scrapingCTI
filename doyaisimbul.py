import requests

def dosyabul(dosya_isim):
    if dosya_isim[(len(dosya_isim)-3):len(dosya_isim)] == "exe":
        url="https://www.exefiles.com/tr/exe/" + dosya_isim[0:(len(dosya_isim)-4)] + "-exe/"
        gelen=requests.get(url)
        if gelen.status_code == 200:
            print(dosya_isim + " dosyası ne işe yarar ? : "+url)
            print("---------------------------------------------------------------")
        
        
        url="https://www.file.net/process/" + dosya_isim + ".html"
        gelen=requests.get(url)
        if gelen.status_code == 200:
            print(dosya_isim + " dosyası ne işe yarar ? : "+url)
            print("---------------------------------------------------------------")
            
            
    elif dosya_isim[(len(dosya_isim)-3):len(dosya_isim)] == "dll":
        url="https://www.exefiles.com/tr/dll/" + dosya_isim[0:(len(dosya_isim)-4)] + "-dll/"
        gelen=requests.get(url)
        if gelen.status_code == 200:
            print(dosya_isim + " dosyası ne işe yarar ? : "+url)
            print("---------------------------------------------------------------")
            
        url="https://www.opendll.com/index.php?search="+dosya_isim
        gelen=requests.get(url)
        if gelen.text.find("No result found for") != -1:
            print(dosya_isim + " dosyası ne işe yarar ? : "+url)
            print("---------------------------------------------------------------")
            
            
        url="https://www.dll.gen.tr/" + dosya_isim="opencl.dll".replace(".dll","")
        gelen=requests.get(url,headers={"User-Agent": "XY"})
        if gelen.status_code == 200:
            print(dosya_isim + " dosyası ne işe yarar ? : "+url)
            print("---------------------------------------------------------------")
