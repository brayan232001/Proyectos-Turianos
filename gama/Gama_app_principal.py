from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext
from apertura_archivo import creador_Palabras
from parrafos import buscador

raiz=Tk()
raiz.title("Gama")
raiz.geometry("800x500")
raiz.resizable(0,0)
raiz.iconbitmap('Pruebas/mariposa.ico')
color_fondo="#0c211c"

frame_fondo=PhotoImage(file="Pruebas/fondo.png")


frame=Label(raiz)
frame.config(image=frame_fondo,width=800,height=500)
frame.pack(fill=BOTH,expand=True)
#-------------------------App interna
#-------------------------Extras
#image_fondo=PhotoImage(file="imagenes/fondo.png")
button_back=PhotoImage(file="Pruebas/button_back.png")
menu_buscador_boton=PhotoImage(file="Pruebas/button_buscador.png")
menu_parrafo_boton=PhotoImage(file="Pruebas/button_parrafo.png")
menu_button_archivo=PhotoImage(file="Pruebas/button_archivo.png")
menu_button_iniciar=PhotoImage(file="Pruebas/button_iniciar.png")
menu_button_insertar=PhotoImage(file="Pruebas/button_insertar.png")
menu_button_lecturas=PhotoImage(file="Pruebas/button_lecturas.png")
menu_button_subtitulo2=PhotoImage(file="Pruebas/subtitulo2.png")
menu_titulo=PhotoImage(file="Pruebas/titulo.png")
menu_titulo2=PhotoImage(file="Pruebas/titulo2.png")
menu_titulo3=PhotoImage(file="Pruebas/titulo3.png")
#___limpar pantalla
def clear():
    lista = frame.grid_slaves()
    for l in lista:
        l.destroy()

#___cambia el menu que se ve en pantalla
def vista(num):
    opcion=num
    if opcion == 1:
        clear()
        menu()
    elif opcion ==2:
        if buscador_lecturas["status"]=="no":
            menu_buscador()
        elif buscador_lecturas["status"]=="cambiar":
            menu_buscador_cuatro()
        else:
            menu_buscador_tres()
    elif opcion ==3:
        clear()
        menu_parrafos()
    elif opcion ==4:
        clear()
        menu_parrafos_buscador()

#___Funcion para seleccionar un archivo
buscador_lecturas={"status":"no","lectura":"¡--No hay un archivo con palabras disponible--!"}
def buscadorSeleccionarLectura():
    buscador_lecturas["status"]="no"
    filename = askopenfilename()
    buscador_lecturas["lectura"]=filename
    buscador_lecturas["status"]="si"
    creador_Palabras(buscador_lecturas["lectura"])
    print(filename)
    vista(2)
#-------------------------Titulo
def encabezado(imagen):
    back=Button(frame)
    back.config( bd=0, bg=color_fondo, command=lambda:vista(1), image=button_back)
    back.grid(row=0,column=0)
    titulo=Label(frame)
    titulo.config(bg=color_fondo, image=imagen, width=700)
    titulo.grid(row=0,column=1,columnspan=5,pady=50)



#___________Menu 3 del buscador de palabras
def menu_buscador_tres():
    clear()
    lectura=buscador_lecturas['lectura']
    lectura=lectura.split("/")
    lecturaN=len(lectura)
    lectura=lectura[lecturaN-1]
    encabezado(menu_titulo2)

    buscador_lecturas["status"]="cambiar"
    #Scrolled text
    texto_palabras=scrolledtext.ScrolledText(frame)
    texto_palabras.config(width=40,height=20)
    texto_palabras.grid(row=2,column=3)
    texto_palabras.insert(INSERT,'Veces / Palabra\n')
    archivo=open(f"archivos_palabras/Palabras_{lectura}","r",encoding='utf-8',errors='ignore')
    for line in archivo:
        try:
            line = line.rstrip()
        except:
            continue
        texto_palabras.insert(INSERT,f'{line}\n')
    archivo.close()
    

#__________Menu 4 dle buscador de palabras
def menu_buscador_cuatro():
    clear()
    lectura=buscador_lecturas['lectura']
    lectura=lectura.split("/")
    lecturaN=len(lectura)
    lectura=lectura[lecturaN-1]
    encabezado(menu_titulo2)

    pregunta=Label(frame)
    pregunta.config(font=("Helvetica",10),text="¿Deseas crear una lista nueva?")
    pregunta.grid(row=1,column=3)

    botonSi=Button(frame)
    botonSi.config(width="10", height="7", text="Si", bd=0, command=menu_buscador)
    botonSi.grid(row=2,column=2)

    botonNo=Button(frame)
    botonNo.config(width="10", height="7", text="No", bd=0, command=menu_buscador_tres)
    botonNo.grid(row=2,column=4)


#___________Menu del buscador de palabras mas usadas
def menu_buscador():
    clear()
    encabezado(menu_titulo2)

    boton_lectura=Button(frame)
    boton_lectura.config(bg=color_fondo, image=menu_button_archivo, bd=0)
    boton_lectura.config(command=buscadorSeleccionarLectura)
    boton_lectura.grid(row=1,column=3)

    label_lecture=Label(frame)
    label_lecture.config(image=menu_button_subtitulo2, bg=color_fondo)
    label_lecture.grid(row=2,column=3,pady=10)

#___________Menu del creador de parrafos
#-----seleccionar lecturas
lista_de_lecturas=StringVar()
list_lecturas=list()
def seleccionar_Lecturas():
    textoflat=""
    filename=askopenfilename(multiple=True)
    for name in filename:
        list_lecturas.append(name)
        name=name.split("/")
        nameN=len(name)
        name=name[nameN-1]
        textoflat+=(f"{name}\n")
    lista_de_lecturas.set(textoflat)
    print(list_lecturas)
#----- seleccionar palabras
lista_de_palabras=StringVar()
list_palabras=list()
def seleccionar_palabras(entry):
    text_plain=""
    word = entry.get()
    list_palabras.append(word)
    for i in list_palabras:
        text_plain+=(f"{i}\n")
    lista_de_palabras.set(f"{text_plain}")
    entry.delete(0,"end")
#-----menu Creador de parrafos
nombre_archivo_final=""

def limpiar():
    for i in list_palabras:
        list_palabras.remove(i)
        lista_de_palabras.set("")
    for j in list_lecturas:
        list_lecturas.remove(j)
        lista_de_lecturas.set("")

def menu_parrafos_buscador():
    clear()
    encabezado(menu_titulo3)

    texto_palabras=scrolledtext.ScrolledText(frame)
    texto_palabras.config(width=60,height=20)
    texto_palabras.grid(row=2,column=2,columnspan=3)

    buscador(list_lecturas,list_palabras)
    for a in range(len(list_palabras)):
        global nombre_archivo_final
        nombre_archivo_final += (list_palabras[a]+"_")

    archivo=open(f"archivos_parrafos/Párrafos_{nombre_archivo_final}.txt","r",encoding='utf-8',errors='ignore')
    for line in archivo:
        try:
            line = line.rstrip()
        except:
            continue
        texto_palabras.insert(INSERT,f'{line}\n')
    archivo.close()
    limpiar()
    
#---- menu
def menu_parrafos():
    clear()
    encabezado(menu_titulo3)

    #columna 2--------------
    lista_lecturas=Label(frame)
    lista_lecturas.config(anchor="nw",justify="left",textvariable=lista_de_lecturas,width=25,height=10,bg="white")
    lista_lecturas.grid(row=1,rowspan=2,column=3,sticky="W")
    boton_lecturas=Button(frame)
    boton_lecturas.config(bd=0,bg=color_fondo,command=seleccionar_Lecturas, image=menu_button_lecturas)
    boton_lecturas.grid(row=3,column=3,sticky="W")

    #columna 3--------------

    lista_palabras=Label(frame)
    lista_palabras.config(anchor="nw",justify="left",textvariable=lista_de_palabras,width=20,height=6)
    lista_palabras.grid(row=1, column=5,sticky="N")
    boton_palabras_ingresar=Button(frame)
    boton_palabras_ingresar.config(bd=0,bg=color_fondo,image=menu_button_insertar,command=lambda: seleccionar_palabras(entry_palabras))
    boton_palabras_ingresar.grid(row=2,column=5,sticky="NE",padx=20)
    entry_palabras=Entry(frame)
    entry_palabras.config(justify="left",width=10)
    entry_palabras.grid(row=2,column=5,sticky="NW",pady=5,padx=20)

    boton_buscador=Button(frame)
    boton_buscador.config(bg=color_fondo, image=menu_button_iniciar, bd=0, activebackground="#395FA8", command=lambda:vista(4))
    boton_buscador.grid(row=3,column=5,stick="S")

    #----------columna 1
    lectura=buscador_lecturas['lectura']
    lectura=lectura.split("/")
    lecturaN=len(lectura)
    lectura=lectura[lecturaN-1]
    encabezado

    texto_palabras=scrolledtext.ScrolledText(frame)
    texto_palabras.config(width=25,height=15)
    texto_palabras.grid(row=1, rowspan=3 ,column=1,sticky="W")
    texto_palabras.insert(INSERT,(f"Palabras mas usadas en '{lectura}'\n\n"))
    try:
        archivo=open(f"archivos_palabras/Palabras_{lectura}","r",encoding='utf-8',errors='ignore')
    except:
        archivo=""
    for line in archivo:
        try:
            line = line.rstrip()
        except:
            continue
        texto_palabras.insert(INSERT,f'{line}\n')
    try:
        archivo.close()
    except:pass


#____________Menu principal
def menu():
    clear()
    encabezado(menu_titulo)

    #--------------------------botones menu1
    boton_palabras=Button(frame)
    #boton_palabras.config(width="15",height="11", bg="#4783F5", text="Palabras más\n usadas", bd=0, font=("Helvetica", 11), activebackground="#395FA8")
    
    boton_palabras.config(image=menu_buscador_boton,bg=color_fondo,activebackground="#3144A8",bd=0, command=lambda:vista(2))
    boton_palabras.grid(row=1, column=2)
    
    boton_buscador=Button(frame)
    boton_buscador.config(image=menu_parrafo_boton, bg=color_fondo, bd=0, command=lambda:vista(3))
    boton_buscador.grid(row=1, column=4)

vista(1)
raiz.mainloop()