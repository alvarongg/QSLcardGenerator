import tkinter as tk
from tkinter import filedialog
import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
path_foto = ''


def Generador_Imagenes( dia,
                        mes,
                        anio,
                        licencia,
                        hora,
                        mhz,
                        rst,
                        mod,
                        qsl
                        ):
    global path_foto
     
    img = Image.open(path_foto.name)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Roboto-Regular.ttf", 40)
    #font = ImageFont.truetype("radio_stars.ttf", 40)
    #font = ImageFont.truetype(font='Arial', size=16, index=0, encoding='')
    #draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((130,900),licencia,(0,0,0),font=font)
    draw.text((380,900),dia,(0,0,0),font=font)
    draw.text((470,900),mes,(0,0,0),font=font)
    draw.text((550,900),anio,(0,0,0),font=font)
    draw.text((700,900),hora,(0,0,0),font=font)
    draw.text((900,900),mhz,(0,0,0),font=font)
    draw.text((1160, 900),rst,(0,0,0),font=font)
    draw.text((1300,900),mod,(0,0,0),font=font)
    draw.text((1470,900),qsl,(0,0,0),font=font)
    img.save(licencia+'_'+anio+'_'+mes+'_'+dia+'_'+hora+'_'+'qsl_9_Julio.jpg')


def getExcel ():
    global df
    global dia
    global mes
    global anio
    global licencia
    global hora
    global mhz
    global rst
    global mod
    global qsl
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    shape = df.shape
    cantidad = shape[0]
    print(cantidad)
    print(df)
    print(df.iloc[5,3])
    for i in range(0,cantidad):
        dia = str(df.iloc[i,9])
        mes =  str(df.iloc[i,10])
        anio =  str(df.iloc[i,11])
        licencia = str(df.iloc[i,3])
        hora =  str(df.iloc[i,4])
        mhz =  str(df.iloc[i,5])
        rst =  str(df.iloc[i,6])
        mod =  str(df.iloc[i,7])
        qsl =  str(df.iloc[i,8])
        print(dia+''+mes+''+anio+''+licencia+''+hora+''+mhz+''+rst+''+mod+''+qsl)
        Generador_Imagenes(dia,mes,anio,licencia,hora,mhz,rst,mod,qsl)


def getImage ():
        global path_foto
        path_foto = filedialog.askopenfile()
        print(path_foto.name)


root= tk.Tk()
root.title("Generador de tarjetas QSL")

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()
    
browseButton_Excel = tk.Button(text='Paso 2: Importar Base_QSL', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
browseButton_Mail = tk.Button(text='Paso 1:Cargar nueva imagen', command=getImage, bg='green', fg='white', font=('helvetica', 12, 'bold'))

canvas1.create_window(150, 150, window=browseButton_Mail)
canvas1.create_window(150, 200, window=browseButton_Excel)





root.mainloop()
