salariobase = int(input("Ingrese el salario base del empleado: "))
aportesalud = salariobase * 0.04
aportepension = salariobase * 0.04
descuentototal = aportesalud + aportepension
salarioneto = salariobase - descuentototal
print("Aporte a salud:", aportesalud)
print("Aporte a pensión:", aportepension)
print("Total de descuentos:", descuentototal)
print("Salario neto a pagar:", salarioneto)
