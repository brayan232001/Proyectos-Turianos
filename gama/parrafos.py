def buscador(list_lecturas,list_palabras):
    palabras=list_palabras.copy()
    lista=list_lecturas.copy()

    parrafos_finales=list()

    def contador(numero,numero_ciclo):
        var1=len(lista)
        var2=len(palabras)
        
        veces=list()
        veces2=list()   
        if numero == 0:
            #opcion cero
            for i in range(var1):
                veces.append(i)
            total=veces*len(palabras)
            #print(total)
            return total
        elif numero == 1:
            #opcion uno
            for ii in range(var2):
                veces2.append(ii)
            veces2=veces2*len(lista)
            veces2=sorted(veces2)
            regresar=list()
            regresar.insert(0,veces2[numero_ciclo])
            x=numero_ciclo
            #print(veces2)
            return [veces2[x]]
        
    ciclo_n=0
    for i in contador(0,0):
        f=open(lista[i],encoding='utf-8', errors='ignore')
        
        nombre_archivo=lista[i].split("/")
        longitud=len(nombre_archivo)
        nombre_archivo=nombre_archivo[longitud-1]

        #print("ciclo",ciclo_n)
        lineas=list()
        puntos=list()
        for line in f:
            line=line.rstrip()
            lineas.append(line)
        for ii in range(len(lineas)):
            words=lineas[ii].split(" ")
            for word in words:
                for iii in contador(1,ciclo_n):
                    if word == palabras[iii]:
                        puntos.append(ii)
                    else:break
        #for n in puntos:
            #print()
            #print(f"<--------------- {lista[i]} linea {n-2} / linea {n+5}------------------------>")
            #print()
            #for nn in range(n-2,n+5):
                #print(lineas[nn])
        #print ("\n/////////////////////////////////////////////////////////////////////////////\n")
        usadas=list()
        for n in puntos:
            parrafos_finales.append(f"\n\n<-----------{nombre_archivo} - {palabras[iii]} linea {n-2} / linea {n+5}----------->\n")
            for nn in range(n-2,n+5):
                    if nn<0:nn=0
                    elif nn>=len(lineas):nn=len(lineas)-1
                    if nn in usadas:continue
                    usadas.append(nn)
                    parrafos_finales.append(f"\n{lineas[nn]}")
        
        ciclo_n=ciclo_n+1
#Creador de archivos con párrafos    
    nombre_archivo_final=""
    for a in range(len(palabras)):
        nombre_archivo_final=nombre_archivo_final+(palabras[a]+"_")
    f=open(f"archivos_parrafos/Párrafos_{nombre_archivo_final}.txt","w+",encoding='utf-8', errors='ignore')
    for line in parrafos_finales:
        f.write(line)
    f.close()   