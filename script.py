# %% [markdown]
# # Analizador de texto.

# %% [markdown]
# ## este programa recibe una cadena de texto e informa la longitud (cantida de caracteres),minuscula,mayusculas y numeros contenidos,ademas debe ser capaz de :
# 
# ### - eliminar espacios en blanco
# ### - convertir todo el texto en minusculas
# ### - convertir todo el exto en mayusculas 
# ### - sustituir una o varias palabras 
# 

# %%
texto = input("ingrese el texto")

# %%


# %%
texto

# %%


# %%


# %%
cadena = input ("Ingrese una cadena")
palabra_reemplazo = input("Ingrese que palabra desea remplazar")
palabra = input("Ingrese la palabra de reemplazo")
cadena_f = cadena.replace(palabra_reemplazo,palabra)
print(cadena)
print(cadena_f)
#jhguiygi6fu7gt
cadena =cadena   
longitud = len(cadena)
print(longitud)
#fghh
cadena =cadena_f
longitud = len(cadena)
print(longitud)

#utgoi7tgo8
mayusculas = cadena.upper()
minusculas = cadena.lower()
print(mayusculas)
print(minusculas)
 

 #gujiuyi
cadena_limpia = cadena_f.strip()
print("Cadena limpia:", cadena_limpia)

# %%
cadena = input("Ingrese una cadena: ")
palabra_reemplazo = input("Ingrese la palabra que desea reemplazar: ")
palabra = input("Ingrese la palabra de reemplazo: ")

cadena_f = cadena.replace(palabra_reemplazo, palabra)

print("Cadena original:", cadena)
print("Cadena modificada:", cadena_f)

longitud_original = len(cadena)
print("Longitud de la cadena original:", longitud_original)

longitud_modificada = len(cadena_f)
print("Longitud de la cadena modificada:", longitud_modificada)

mayusculas = cadena_f.upper()
minusculas = cadena_f.lower()

print("Cadena en mayúsculas:", mayusculas)
print("Cadena en minúsculas:", minusculas)

cadena_limpia = cadena_f.strip()
print("Cadena limpia:", cadena_limpia)

# %%
def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Has seleccionado la Opción 1.")
            # Agrega aquí el código correspondiente a la Opción 1.

        elif opcion == "2":
            print("Has seleccionado la Opción 2.")
            # Agrega aquí el código correspondiente a la Opción 2.

        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")



# %%
def obtener_informacion(cadena):
    cantidad_total = len(cadena)
    cantidad_minusculas = sum(1 for char in cadena if char.islower())
    cantidad_mayusculas = sum(1 for char in cadena if char.isupper())
    cantidad_numericos = sum(1 for char in cadena if char.isdigit())

    print("Información:")
    print(f"Cadena de texto: {cadena}")
    print(f"Cantidad total de caracteres: {cantidad_total}")
    print(f"Cantidad de caracteres en minúscula: {cantidad_minusculas}")
    print(f"Cantidad de caracteres en mayúscula: {cantidad_mayusculas}")
    print(f"Cantidad de caracteres numéricos: {cantidad_numericos}")

def eliminar_espacios(cadena):
    return cadena.replace(" ", "")

def menu():
    cadena = input("Ingrese una cadena de texto: ")

    print("\n1. Mostrar información sobre la cadena")
    print("2. Eliminar espacios en blanco")
    print("3. Salir")

    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "1":
        obtener_informacion(cadena)
    elif opcion == "2":
        cadena_sin_espacios = eliminar_espacios(cadena)
        print(f"\nCadena sin espacios: {cadena_sin_espacios}")
    elif opcion == "3":
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        menu()

menu()

# %%
def obtener_informacion(cadena):
    cantidad_total = len(cadena)
    cantidad_minusculas = sum(1 for char in cadena if char.islower())
    cantidad_mayusculas = sum(1 for char in cadena if char.isupper())
    cantidad_numericos = sum(1 for char in cadena if char.isdigit())

    print("Información:")
    print(f"Cadena de texto: {cadena}")
    print(f"Cantidad total de caracteres: {cantidad_total}")
    print(f"Cantidad de caracteres en minúscula: {cantidad_minusculas}")
    print(f"Cantidad de caracteres en mayúscula: {cantidad_mayusculas}")
    print(f"Cantidad de caracteres numéricos: {cantidad_numericos}")

def eliminar_espacios(cadena):
    return cadena.replace(" ", "")

def mostrar_menu():
    print("Convertir cadena a mayúsculas")

def mostrar_menu():
    print("Convertir cadena a minúsculas")

def sustituir_palabra(cadena):
    palabra_original = input("Ingrese la palabra original: ")
    palabra_nueva = input("Ingrese la palabra nueva: ")
    return cadena.replace(palabra_original, palabra_nueva)


def menu():
    cadena = input("Ingrese una cadena de texto: ")

    print("\n1. Mostrar información sobre la cadena")
    print("2. Eliminar espacios en blanco")
    print("3. Cadena en mayúsculas")
    print("4. Cadena en minúsculas")
    print("5. Sustituir palabra")
    print("6. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        obtener_informacion(cadena)
    elif opcion == "2":
        cadena_sin_espacios = eliminar_espacios(cadena)
        print(f"\nCadena sin espacios: {cadena_sin_espacios}")
    elif opcion == "3":
            if cadena:
                print("Cadena en mayúsculas:", cadena.upper())
    elif opcion == "4":
            if cadena:
                print("Cadena en minúsculas:", cadena.lower())
    elif opcion == "5":
            if cadena:
                cadena = sustituir_palabra(cadena)
                print("Cadena con palabra sustituida:", cadena)
    
    elif opcion == "6":
        print("¡Hasta luego!")

    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
        menu()

menu()


