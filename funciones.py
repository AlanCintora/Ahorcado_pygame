archivo = "Segundo_Parcial\\archivo_palabras.txt"

def cargar_archivo_lista(nombre_archivo):
    lista_palabras = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                palabra = linea.strip()
                if palabra:
                    lista_palabras.append(palabra)
    except Exception as e:
        print("Error al procesar el archivo:", e)
    
    return lista_palabras
        
archivo_final = cargar_archivo_lista(archivo)

print(archivo_final)
