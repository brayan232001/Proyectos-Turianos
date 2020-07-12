direccion="C:/Users/Brayan Buitrago/Desktop/final/Pruebas/9.Division del trabajo.txt"
def creador_Palabras(direccion):
    #arreglar componentes de la direccion
    nombre_archivo=direccion.split("/")
    longitud=len(nombre_archivo)
    nombre_archivo=nombre_archivo[longitud-1]

    direccion_corta=direccion.split("/")
    direccion_corregida=""
    for i in range(len(direccion_corta)-1):
        
        direccion_corregida+=(f"{direccion_corta[i]}/")

    #funcion
    fname=open(f"{direccion}","r",encoding='utf-8',errors='ignore')

    ignore=["del","de","la","el","los","las","en","con","se","que","un","una","y","a","o","e","lo","para","El""su","por","es","al","como","más","En","La","sus","ha","\n"," "]

    diccionario=dict()
    lista_words=list()

    for line in fname:
        line = line.strip()
        words = line.split(" ")
        for word in words:
            if word in ignore: continue
            diccionario[word]=diccionario.get(word,0)+1
    for k,v in diccionario.items():
            lista_words.append((v,k))
    lista_orden=sorted(lista_words,reverse=True)
        
    f=open(f"archivos_palabras/Palabras_{nombre_archivo}","w+",encoding='utf-8', errors='ignore')
    for k,v in lista_orden:
        f.write(f"{k}) {v}\n")
    f.close()
