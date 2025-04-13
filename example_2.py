# Imprimir las filas dónde el apellido empiece con B

def read_lines(file_name):
    try:
        # Abrimos el archivo "informacion.txt" en modo lectura ('r')
        with open(file_name, "r", encoding="utf-8") as file:
            # Leemos todas las líneas en una lista
            lines = file.readlines()
            # Iteramos línea por línea
            for line_number, line in enumerate(lines, start=1):
                # Eliminamos espacios en blanco al inicio y al final de la línea (incluye el salto de línea '\n')
                clean_line = line.strip()
                # Omitimos la cabecera (si es la primera línea)
                if line_number == 1:
                    continue
                # los datos están separados por ;
                columns = clean_line.split(";")
                #Eliminar espacios en blanco
                last_name = columns[1].strip()
                # Imprimimos el número de línea y su contenido si empieza con b
                if last_name.startswith("B"):
                    print(f"Línea {line_number}: {clean_line}")
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no fue encontrado")

#Llamar a la función
read_lines("informacion.txt")