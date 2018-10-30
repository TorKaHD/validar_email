# Verificar Email con Python.

def verificar_correo ():

    import re # Llamamos al módulo llamado "re"

    correo = str (input ("Introduce tu correo electrónico: "))
    print ()

    if re.match ('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.lower()):

        print ("Correo correcto")

    else:

        print ("Correo incorrecto")

verificar_correo ()
