print("Ejercicio 2: ¿Quien paga el flete y el seguro?")
print("Nombre: Yareshi Guadalupe Robles Torres")
print("Matricula: 07278887")
print()

# Pedimos los datos del contrato
incoterm = input("Escribe el Incoterm en MAYUSCULA (EXW, FOB, CIF, CIP, DAP): ")
valor = float(input("Valor de la mercancia en dolares: "))
transporte = input("Transporte en MAYUSCULAS (MARITIMO, AEREO,TERRESTRE): ")
fragil = input("¿La mercancia es fregil? (si/no): ")

# Convertimos la respuesta en True o False
es_fragil = fragil == "si"

print()
print("===== RESUMEN DEL CONTRATO =====")

# not + or: si NO es ninguno de los 5 Incoterms, el dato esta mal
if not (incoterm == "EXW" or incoterm == "FOB" or incoterm == "CIF" or incoterm == "CIP" or incoterm == "DAP"):
    print("❌ Incoterm no valido. Revisa que esta en MAYUSCULAS.")
else:
    # or: con EXW o FOB, el flete internacional lo paga el COMPRADOR
    if incoterm == "EXW" or incoterm == "FOB":
        print("🚛 Flete internacional: lo paga el COMPRADOR.")
    else:
        print("🚛 Flete internacional: lo paga el VENDEDOR.")

    # or: con CIF o CIP, el seguro lo contrata el VENDEDOR
    if incoterm == "CIF" or incoterm == "CIP":
        # or: si es fragil O va por barco, el riesgo es mayor
        if es_fragil or transporte == "MARITIMO":
            porcentaje = 2
        else:
            porcentaje = 1
        seguro = valor * porcentaje / 100
        print("✅ Seguro: lo contrata el VENDEDOR.")
        print("Porcentaje del seguro: ", porcentaje, "%", sep="")
        print("Costo estimado del seguro: $", seguro, sep="")
    else:
        print("📦 Seguro: NO lo contrata el vendedor. Lo decide el COMPRADOR")