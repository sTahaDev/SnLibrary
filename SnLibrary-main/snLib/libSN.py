"""
Python Kütüphanesi
Yapımcı: Taha Şahin
Başlangıç Tarihi: 9.01.23

Sürüm: 1.0
"""

import time
import os
import tkinter as tk

class snCompailer():
    def __init__(self) -> None:
        self.form = tk.Tk()
        self.form.title("Pencere")
        self.pencereOlustu = False
        pass
    def dosyaokuma(self):
        with open("main.sn") as dosya:
            read = dosya.readlines()
        return read
    
    def compileEtme(self):
        
        metods = self.dosyaokuma()
        
        if metods[0] == 'sn main(){\n':
            print("Kod Derleniyor\n---------------")
            for i in metods:
                if "//" in i:
                    i = ""
                # yazdir işlemi
                if 'yazdir("' in i:
                    i = i.replace("\n","")
                    yazi = i.replace('yazdir("','')
                    yazi = yazi.replace('")','')
                    yazi = yazi.replace("    ", "")
                    print(yazi)
                pass
                #input işlemi
                if 'verigirisi("' in i:
                    i = i.replace("\n","")
                    i = i.replace('verigirisi("','')
                    i = i.replace('")','')
                    i = i.replace("    ", "")
                    verigirisi = i
                    self.veriGirisiDegeri = input(f"{verigirisi}--> ")
                    
                    
                    pass
                if "<Pencere>" in i:
                    i = i.replace("\n","")
                    i.replace("<Pencere>","")
                    self.olusturPencere()
                if "<Yazi>" in i:
                    i = i.replace("\n","")
                    i = i.replace("<Yazi>"," ")
                    if "</Yazi>" in i:
                        i = i.replace("</Yazi>","")
                        self.olusturYazi(i)
                        
      
        else:
            print("Bir Hata Oluştu!")

    def olusturPencere(self):
        
        self.form.mainloop()
        self.pencereOlustu = True
        pass
    def olusturYazi(self,Etiket):
        if Etiket == "":
            Etiket = "Deger Girilmedi"
        etiket = tk.Label(self.form,text=Etiket)
        etiket.pack()
    def deistirBoyut(self,Uzunluk,En):
        self.form.geometry(f"{Uzunluk}x{En}")



    
        



