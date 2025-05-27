from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("choose book")

book1 = PhotoImage(file="shoeh.png")
book2 = PhotoImage(file="hsl.png")
book3 = PhotoImage(file="lnattc.png")
book4 = PhotoImage(file = "tkam.png")
book5 = PhotoImage(file="trok.png")
book6 = PhotoImage(file="tsok.png")

label1 = Label(root, text="Choose a Book")
label1.pack()

label2 = Label(root, image=book1)
label2.pack()






root.mainloop()