from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Demonitation counter')
root.configure(bg= 'light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open('app.img')
# Resize Image using the resizing()method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(text = "Hey User! Welcome To The Demonication Application."
               bg = 'light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a message box and proceed if OK is clicked
def msg ():
    MsgBox