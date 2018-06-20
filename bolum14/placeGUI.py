from tkinter import *
gui = Tk()
# Koordinatları verilerek yerleştirme
Button(gui, text="Hassas").place(x=20, y=10)
Entry(gui).place(x=90, y=10)
# Yaklaşık(Relative) yerleştirme
Button(gui, text="Tahmini").\
       place(relx=0.6, rely=0.4, anchor=NE)
gui.mainloop()



