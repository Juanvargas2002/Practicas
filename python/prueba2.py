# Inventario de la tienda, se empieza vacío
inventario = {}

# Mantiene el programa corriendo
seguir = True

# Mostrar menú de opciones
def menu():
    print("\nGESTOR DE INVENTARIO DE LA BENDICIÓN DE DIOS")
    print("1: Agregar un producto")
    print("2: Ver un producto")
    print("3: Vender producto")
    print("4: Ver inventario")
    print("5: Salir")
    opcion = input("¿Qué opción eliges? ")
    return opcion

# Registrar un producto, si ya existe agrega más stock
def agregarProducto():
    print("\n>>> Agregar un producto <<<")
    nombre = input("¿Cómo se llama el producto? ")
    
    if nombre in inventario:
        print("\n¡Este producto ya existe! Solo agregaremos más cantidad.")
        cantidad = int(input("¿Cuántos más quieres agregar? "))
        inventario[nombre]['cantidad'] += cantidad
        print(f"Ahora tienes {inventario[nombre]['cantidad']} de '{nombre}'.")
    else:
        cantidad = int(input("¿Cuántos tienes para empezar? "))
        precio = float(input("¿A cuánto lo vendes? "))
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print(f"El producto '{nombre}' se agregó correctamente.")

# Consultar un producto por nombre
def verProducto():
    print("\n>>> Consultar un producto <<<")
    nombre = input("¿Qué producto quieres ver? ")
    
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"Producto: {nombre}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: ${producto['precio']:.2f}")
    else:
        print("\nEste producto no está en el inventario.")

# Vender un producto, actualiza la cantidad o elimina si ya no hay
def venderProducto():
    print("\n>>> Vender un producto <<<")
    verInventario()
    nombre = input("¿Qué producto vas a vender? ")
    
    if nombre in inventario:
        cantidad = int(input("¿Cuántos vas a vender? "))
        
        if cantidad <= inventario[nombre]['cantidad']:
            inventario[nombre]['cantidad'] -= cantidad
            total = cantidad * inventario[nombre]['precio']
            print(f"Venta exitosa. Total: ${total:.2f}")
            
            if inventario[nombre]['cantidad'] == 0:
                del inventario[nombre]
                print(f"El producto '{nombre}' se agotó y se eliminó del inventario.")
        else:
            print("No tienes suficiente cantidad de este producto.")
    else:
        print("Este producto no está en el inventario.")

# Ver todos los productos en el inventario
def verInventario():
    print("\n>>> Inventario <<<")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for nombre, detalles in inventario.items():
            print(f"{nombre}: {detalles['cantidad']} en stock - ${detalles['precio']:.2f} cada uno")

# Controla todo el flujo del programa
def gestor():
    while seguir:
        opcion = menu()
        if opcion == "1":
            agregarProducto()
        elif opcion == "2":
            verProducto()
        elif opcion == "3":
            venderProducto()
        elif opcion == "4":
            verInventario()
        elif opcion == "5":
            print("¡Hasta luego! Gracias por usar el gestor.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

gestor()
