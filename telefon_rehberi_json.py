"""
Telefon rehberi programı python 3.10 üsütnde çalışmaktadır. Öncelikle kayıt ekleyiniz...
"""
import json
rehber_dict = {"kayitli_isim_no":[]}

try:
    with open('telefon_rehberi.json') as f:
        json.load(f)
except:
    with open("telefon_rehberi.json", 'w') as f:
        json.dump(rehber_dict, f, indent=2)


def kayit_ekle():
    try:
        isim = input("Isim giriniz: ")
        tel_no = int(input("Telefon numarasi giriniz: "))    
        with open('telefon_rehberi.json') as f:
            data = json.load(f)                                   
        with open('telefon_rehberi.json', 'w') as f:           
                 
            data["kayitli_isim_no"].append({"isim":isim.title(), "tel":tel_no})           
            json.dump(data, f, indent=2)
    except Exception as e:
        print(e)
    else:
         print("Kayit basariyla eklendi!")

def kayit_listele():
    try:
        with open('telefon_rehberi.json') as f:
            data = json.load(f)
            if len(data["kayitli_isim_no"]) > 0:            
                for i in data["kayitli_isim_no"]:
                    print("Isim: ", i['isim'])
                    print("Tel:", i["tel"],"\n")
            else:
                print("Rehberde kayit yok!")
    except Exception as ex:
        print("Sorun kaynağı.: ", ex)

def kayit_sil():
    list_isimler = []
    try:
        with open('telefon_rehberi.json') as f:
                data = json.load(f)
                data_list = data["kayitli_isim_no"]            
                for i in data_list:                
                    list_isimler.append(i['isim'])
        x = input(f"Silmek istediginiz ismi girin. Kayitli isimler :{list_isimler}")
        if len(data_list) > 0:
            try:
                data_list.remove(next(item for item in data_list if item["isim"] == x.title()))
                print("Kayit basariyla silindi")
            except:
                print("silinecek böyle bir kayit yok!")
        else:
            print("Rehberde kayit yok! Silemezsiniz")
        with open('telefon_rehberi.json', 'w') as f:            
                json.dump(data, f, indent=2)
    except Exception as ex:
        print("Sorun kaynağı.: ", ex)
    
    
    #print(list(filter(lambda person: person['isim'] == x, data_list)))
    
def kayit_ara():
    try:
        aranacak_kelime = input("Aramak istediginiz ismi giriniz:")
        with open('telefon_rehberi.json') as f:
            data = json.load(f)
            data_list = data["kayitli_isim_no"] 
            if len(data_list) > 0:
                try:
                    sonuc = next(item for item in data_list if item["isim"] == aranacak_kelime.title())
                    print(sonuc)
                except:
                    print("Kayit bulunamadi!")
            else:
                print("Rehberde kayit yok!")
    except Exception as ex:
        print("Sorun kaynağı.: ", ex)
#main program:  
try:
    secim = int(input("Yapmak istediginiz islemi seciniz.\n 1- Kayitlari listele\n 2- kayit sil\n 3- Kayit ekle\n 4- Kayit ara\n"))
    match secim: #match komutu 3.10 ve üzerinde çalışır
        case 1:
            kayit_listele()
        case 2:
            kayit_sil()
        case 3:
            kayit_ekle()
        case 4:
            kayit_ara()
        case _:
            print("1 ile 4 arasi bir rakam girin")
except:
    print("Sayi giriniz")
