lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

if (lado1 + lado2 > lado3) or (lado2 + lado3 > lado1):
    print("É um triângulo")
    
    if (lado1 == lado2) and (lado1 == lado3):
        print("É equilátero")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("É isóceles")
    elif (lado1 != lado2) and (lado1 != lado3):
        print("É escaleno")
        
