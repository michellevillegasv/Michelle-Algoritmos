amount = int(input("Please enter the Total: "))
iva = float(input("IVA: %"))
def invoice(amount, iva):
    total = amount * (iva/100)
    return total
print("****INVOICE****")
print(f"MONTO NETO: {amount}\n IVA: {iva}% \n TOTAL: {invoice(amount, iva)}")
