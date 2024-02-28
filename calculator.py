from tkinter import*

# Giriş kutusuna bir rakam veya işlem simgesi eklemek için yaz() fonksiyonu
def yaz(x):
    # Giriş kutusunun uzunluğunu al
    s = len(giris.get())
    # Giriş kutusunun sonuna x'i ekle
    giris.insert(s, str(x))
    
# İşlem türünü belirlemek için islemler() fonksiyonu
def islemler(x):
    global hesap
    hesap = x  # Global hesap değişkenine x değerini ata (0: Toplama, 1: Çıkarma, 2: Çarpma, 3: Bölme)
    global s1
    s1 = float(giris.get())  # s1 değişkenine giriş kutusundaki değeri float olarak al
    print(hesap)  # Hesap türünü ekrana yazdır
    print(s1)     # s1 değerini ekrana yazdır
    giris.delete(0, "end")  # Giriş kutusunu temizle
    
# İşlemi gerçekleştirmek için hesapla() fonksiyonu
def hesapla():
    global s2
    s2 = float(giris.get())  # s2 değişkenine giriş kutusundaki değeri float olarak al
    print(s2)                 # s2 değerini ekrana yazdır
    global hesap
    sonuc = 0
    # Hesap türüne göre işlem yap
    if(hesap == 0):
        sonuc = s1 + s2
    elif(hesap == 1):
        sonuc = s1 - s2
    elif(hesap == 2):
        sonuc = s1 * s2
    elif(hesap == 3):
        sonuc = s1 / s2
    giris.delete(0, "end")  # Giriş kutusunu temizle
    giris.insert(0, str(sonuc))  # Sonucu giriş kutusuna yaz
    
# Tkinter penceresini oluştur
pencere = Tk()
pencere.title("HESAP MAKINESI")
pencere.geometry("500x500")

# Giriş kutusu oluştur
giris = Entry(font="Verdana 14 bold", width=20, justify=RIGHT)
giris.place(x=80, y=20)

# Rakam butonlarını oluştur
b = []
for i in range(1, 10):
    b.append(Button(text=str(i), font="Verdana 14 bold", width=4, command=lambda x=i: yaz(x)))
sayac = 0
for i in range(0, 3):
    for j in range(0, 3):
        b[sayac].place(x=80+j*70, y=80+i*70)
        sayac += 1

# İşlem butonlarını oluştur
islem = []
for i in range(0, 4):
    islem.append(Button(fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=lambda x=i: islemler(x)))
islem[0]["text"] = "+"
islem[1]["text"] = "-"
islem[2]["text"] = "*"
islem[3]["text"] = "/"

for i in range(0, 4):
    islem[i].place(x=300, y=80+50*i)

# Sıfır butonunu oluştur
sifirb = Button(text=0, font="Verdana 14 bold", width=4, command=lambda x=0: yaz(x))
sifirb.place(x=80, y=280)

# Nokta butonunu oluştur
noktb = Button(text=".", font="Verdana 14 bold", width=4, command=lambda x=".": yaz(x))
noktb.place(x=220, y=280)

# Eşittir butonunu oluştur
esittirb = Button(fg="RED", bg="GRAY", font="Verdana 14 bold", width=4, command=hesapla)
esittirb.place(x=300, y=280)

# Pencereyi göster
pencere.mainloop()
