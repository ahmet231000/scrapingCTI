import pandas as pd


def ekle(ip,skor):
    try:
        oku=pd.read_excel("bildirilmis_ip.xlsx")
        del oku["Unnamed: 0"]
        df = pd.DataFrame({'IPLER': [ip], 'SKOR': [skor]})
        oku=oku.append(df, ignore_index=True)
        oku.to_excel("bildirilmis_ip.xlsx",encoding='utf-8-sig')
        print("IP Adresi Başarılı Bir Şekilde Listeye Eklendi.")
    
    except FileNotFoundError:
        df = pd.DataFrame({'IPLER': [ip], 'SKOR': [skor]})
        df.to_excel("bildirilmis_ip.xlsx",encoding='utf-8-sig')
        print("Yeni Liste Oluşturularak IP Adresi Başarılı Bir Şekilde Listeye Eklendi.")
        
    except:
        print("İp Kaydetme Sırasında Bilinmeyen Bir Hata Oluştu..!!\nbakınız:ipkaydet.py")
        
def ip_sorgula(ip):
    try:
        oku=pd.read_excel("bildirilmis_ip.xlsx")
        del oku["Unnamed: 0"]
        for i in range(len(oku)):
            try:
                if oku.loc[i,"IPLER"].find(ip) != -1:
                    print("Liste Risk Skoru : "+str(oku.loc[i,"SKOR"]))
            except:
                pass
        
    except FileNotFoundError:
        pass
    except:
        print("İp Listesinden Sorgulama Sırasında Bilinmeyen Bir Hata Oluştu..!!\nbakınız:ipkaydet.py")
        