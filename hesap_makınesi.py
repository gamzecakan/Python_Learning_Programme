#tkinter modülünü içe aktarıyoruz, bu modülle grafiksel kullanıcı arayüzü (GUI) oluşturacağız.
from tkinter import *
"""
button_click(item): Kullanıcının bir düğmeye tıklaması durumunda çalışacak fonksiyon. Tıklanan düğmenin değerini ifadeye ekler.
button_clear(): Temizleme düğmesine tıklandığında çalışacak fonksiyon. Giriş ifadesini sıfırlar.
button_equal(): Eşittir düğmesine tıklandığında çalışacak fonksiyon. İfadeyi değerlendirir ve sonucu gösterir.
"""
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

expression = ""

root = Tk()
root.title("Calculator")

#Giriş alanını oluşturuyoruz. Bu alanda hesaplamaların gösterileceği metin bulunacak.
input_text = StringVar()
input_field = Entry(root, textvariable=input_text)
input_field.grid(row=0, columnspan=4, ipadx=70)

"""
Hesap makinesindeki düğmeleri oluşturuyoruz. 
Düğmelerin değerlerini bir listede tutuyoruz ve bu değerlere göre düğmeleri oluşturuyoruz. 
Düğmeler "7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "C", "0", "=", "+" şeklinde olacak.
"""

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
"""
Düğmeleri satır ve sütunlarına göre düzenleyerek ekrana yerleştiriyoruz. 
"=" ve "C" düğmeleri özel durumlar olduğu için ayrı işlemler yapıyoruz.
"""
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        Button(root, text=button, padx=15, pady=15, command=lambda: button_equal()).grid(row=row_val, column=col_val)
    elif button == 'C':
        Button(root, text=button, padx=15, pady=15, command=lambda: button_clear()).grid(row=row_val, column=col_val)
    else:
        Button(root, text=button, padx=15, pady=15, command=lambda x=button: button_click(x)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
# Tkinter penceresini görüntülemek için mainloop() yöntemini kullanıyoruz.
root.mainloop()
