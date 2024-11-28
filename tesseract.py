# import pytesseract as test

# from PIL import Image

# test.pytesseract.tesseract_cmd = r'C:\Users\BreynerFaridQuilindo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# my_image = Image.open ('prueba.png')
# txt= test.image_to_string(my_image)

# print(txt)

import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image, ImageTk
import pytesseract as test

# Configura la ruta de Tesseract si es necesario
test.pytesseract.tesseract_cmd = r'C:\Users\BreynerFaridQuilindo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def open_image():
    archivo_ruta = filedialog.askopenfilename() #abre el explorador de archivos
    if archivo_ruta:
        img = Image.open(archivo_ruta) #Muestra la imagen
        img.thumbnail((500, 400))  #Tamañao de la imagen que va a mostrar, para redimencionar.
        img = ImageTk.PhotoImage(img) 
        panel.config(image=img)
        panel.image = img
        extraccion_texto(archivo_ruta)

def extraccion_texto(ruta_imagen):
    text = test.image_to_string(Image.open(ruta_imagen), lang='spa')
    # text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, (text))

root = tk.Tk()
root.title("OCR con Tesseract")

frame = tk.Frame(root, bg="white")
frame.pack(fill=tk.BOTH, expand=True)

panel = tk.Label(frame)
panel.pack(pady=10)

btn_open = tk.Button(frame, text="Abrir Imagen", command=open_image)
btn_open.pack(pady=10)

text_box = Text(frame, wrap=tk.WORD, height=10)
text_box.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()