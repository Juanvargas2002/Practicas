#Variable donde se guardan todos los productos del inventario
inventario = {}
#Variable para mantener el while en funcionamiento de gestion de inventario
mantenerfuncionando = True
verificar = True

#metodo para mostrar las opciones disponibles del menu de la tienda
def Menu():
    print("\nGESTOR DE INVENTARIO DE LA BENDICIÓN DE DIOS")
    print("1: Registrar un producto")
    print("2: Consultar un producto")
    print("3: Vender producto")
    print("4: Ver inventario")
    print("5: Salir")
    opcion = input("Elige una opción: ")
    return opcion

#metodo para registrar un producto y si ya esta el producto se puede agregar una cantidad adicional al stock
def registrar():
    print("\n<---| Registrar un producto |--->")
    nombre = input("Nombre del producto: ")

    # Verificación de si el producto existe
    encontrado = False
    for producto in inventario:
        if producto == nombre:
            encontrado = True
            break  # Si encontramos el producto, salimos del bucle

    if encontrado==True:
        print("\n----------------------------------------------------")
        print("El producto ya existe. Puedes actualizar su cantidad.")
        print("\n----------------------------------------------------")

        #aqui se suma al stock la cantidad adicional si intenta registrar un producto que ya existe
        cantidad = int(input("Cantidad adicional: "))
        inventario[nombre]['cantidad'] += cantidad
        print(f"Cantidad actualizada. Ahora hay {inventario[nombre]['cantidad']} unidades de '{nombre}'.")

    else:
        #aqui se agrega un nuevo producto al inventario
        cantidad = int(input("Cantidad inicial: "))
        precio = float(input("Precio por unidad: "))
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print(f"Producto '{nombre}' registrado con éxito.")

def consultar():
    #consultar producto por el nombre 
    print("\n   --- Consultar un producto ---")
    print("\n---------------------------------------")
    nombre = input("Nombre del producto a consultar: ")
    
    # usamos el mismo de arriba para verificar si el producto existe
    encontrado = False
    for producto in inventario:
        if producto == nombre:
            encontrado = True
            break  # Si encontramos el producto, salimos del bucle

    if encontrado==True:
        productoconsultado = inventario[nombre]
        print(f"Producto: {nombre}")
        print(f"Cantidad: {productoconsultado['cantidad']}")
        print(f"Precio por unidad: ${productoconsultado['precio']:.2f}")
    else:
        print("\n-----------------------------------------------------------")
        print(f"El producto '{nombre}' no está registrado en el inventario.")
        print("\n-----------------------------------------------------------")

#metodo para vender productos
def vender():
    print("\n--- Vender un producto ---")
    Inventario()
    nombre = input("Nombre del producto a vender: ")
    # Verificación de si el producto existe con la misma de las dos de arriba
    encontrado = False
    for producto in inventario:
        if producto == nombre:
            encontrado = True
            break  # Si encontramos el producto, salimos del bucle

    if encontrado==True:
        cantidad = int(input("Cantidad a vender: "))
        #se verifica que la cantidad no exeda el stock disponibl, en caso contrario manda un mensaje por el else
        if cantidad <= inventario[nombre]['cantidad']:
            inventario[nombre]['cantidad'] -= cantidad
            total = cantidad * inventario[nombre]['precio']

            print("\n-------------------------------------------")
            print(f"Venta realizada con éxito. Total a cobrar: ${total:.2f}")
            print("\n-------------------------------------------")

            #aqui se elimina el producto si despues de la venta quedan 0 productos, dado que ya no habra disponibles
            if inventario[nombre]['cantidad'] == 0:
                del inventario[nombre]
                print(f"El producto '{nombre}' se ha agotado y ha sido eliminado del inventario.")

        else:
            print("\n-------------------------------------------")
            print("Cantidad insuficiente en el inventario.")
            print("\n-------------------------------------------")

    else:
        print("\n-------------------------------------------")
        print(f"El producto '{nombre}' no está registrado en el inventario.")
        print("\n-------------------------------------------")

#metodo para ver el invetario
def Inventario():

    print("\n-------------------------------------------")
    print("\n        --- Inventario actual ---")
    print("\n-------------------------------------------")
    
    #si inventario no tiene nada entonces muestra este mensaje
    if not inventario:
        print("\n-------------------------")
        print("El inventario está vacío.")
        print("\n------.------------------")
    else:
        #en caso contrario que si tiene algun producto registrado los muestra todos por medio del for
        print(f"{'Producto':<18} |{'Cantidad':<15} |{'Precio':<10}")
        print("-------------------------------------------")
        for nombre, detalles in inventario.items():
            print(f"{nombre:<18} {detalles['cantidad']:<15} ${detalles['precio']:<10.2f}")
        print("\n-------------------------------------------")

#metodo que llama el primero para mostrar las opciones y usa el return para validar la opcion escogida
#se mantiene mostrandose siempre dado que se usa la variable siempre en true, pero se quita al darle salir 
#mediante el break
def gestor():    
    while mantenerfuncionando==True:
        opcion = Menu()
        if opcion == "1":
            registrar()
        elif opcion == "2":
            consultar()
        elif opcion == "3":
            vender()
        elif opcion == "4":
            Inventario()
        elif opcion == "5":
            print("¡Gracias por usar el gestor de inventario de La Bendición de Dios!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

gestor()
