# una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuando debera pagar finalmente por su compra

prod1 = float(input("Ingrese el valor de 1er Producto: $"))
prod2 = float(input("Ingrese el valor de 2do Producto: $"))

pagar = (prod1 + prod2) * 0.15 
descuento = prod1 + prod2 - pagar

print (f"Importe a pagar con descuento del 15%: ${descuento:.2f}")