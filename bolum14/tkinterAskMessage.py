import tkinter.messagebox as msj
isEvet= msj.askretrycancel\
        (title="Retry Cancel",message="Tekrar dene- İptal?")

print(isEvet)

msj.showerror(title="Error", message="Hata!")
