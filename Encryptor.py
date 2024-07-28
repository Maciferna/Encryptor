#!/data/data/com.termux/files/usr/bin/env python3

def encriptar(mensaje, clave):
    mensaje_encriptado = ""
    for i in range(len(mensaje)):
        char = mensaje[i]
        if char == ' ':
            mensaje_encriptado += ' '  # Mantener los espacios sin encriptar
            continue
        clave_char = clave[i % len(clave)]
        mensaje_encriptado += chr((ord(char) + ord(clave_char)) % 256)
    return mensaje_encriptado

def desencriptar(mensaje_encriptado, clave):
    mensaje_original = ""
    for i in range(len(mensaje_encriptado)):
        char = mensaje_encriptado[i]
        if char == ' ':
            mensaje_original += ' '  # Mantener los espacios sin encriptar
            continue
        clave_char = clave[i % len(clave)]
        mensaje_original += chr((ord(char) - ord(clave_char)) % 256)
    return mensaje_original

while True:
    accion = input("Desea Encriptar, Desencriptar o Salir?(E/D/S): ").upper()
    if accion == "E":
        mensaje = input("Escriba su mensaje aquí: ")
        clave = input("Escriba aquí la clave: ")
        mensaje_encriptado = encriptar(mensaje, clave)
        print("Mensaje encriptado:", mensaje_encriptado)
    elif accion == "D":
        mensaje_encriptado = input("Escriba el mensaje encriptado aquí: ")
        clave = input("Escriba aquí la clave: ")
        mensaje_original = desencriptar(mensaje_encriptado, clave)
        print("Mensaje desencriptado:", mensaje_original)
    elif accion == "S":
        break
    else:
        print("Por favor, ingrese una opción válida (E/D/S).")
