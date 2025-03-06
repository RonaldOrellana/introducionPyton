# voy a comprar pan 
presupuesto = 1
valorpan = 0.5
valorcafe = 0.5
#> es unicamente mayor al numero sin incluir el numero de inicio
#>= si se incluye el valor del elemento.

if presupuesto > valorpan + valorcafe:
    print("pansito con cafe")

if presupuesto > valorpan:
    print("no me alcanza para el pan")

valorNaranja = valorcafe

if valorcafe == valorNaranja:
    print("igual")

else:
    print("el valor es diferente ")

    if not False :
        print("solo saldre si es verdad")

        v1 = (4+7+15+8) > 15+4+5/2 #parentesisi
        # /
        # >
        print("respuesta " , v1)

        v2 = (1+2 +7 **2)/10 <= 42 *7  # lo que esta en parentesis se ejecuta primero
                                       # potencia 
        # *
        # /
        # +
        print("respuesta " , v2) 

#(7 == 7) // (2 > 5)

v4 = (7 == 7) and (2 > 5)
print('v4 = (7==7) or 2 > 5', v4)

#FOR
# V + F = V
# 1 true 
# 0 false
# 1 + 0 = 1

#!(4 <= 4) && (6 != 3)
v5 = not (4 <= 4) and (6 != 3)
print('v5 = not (4 <= 4) and not (6 != 3)', v5)

#and *
# 1
# 0
# 1 * 0 = 0
# 1 * 1 = 1

v6 = (10 >= 10) and (5 < 2)
print('v6 = (10 >= 10) and (5 < 2)', v6)

# 1 * 0 = 0
# 1 * 1 = 1
# 0 * 0 = 0
# 0 * 1 = 0
# 0 * 0 = 0

# (8 != 9) && (3 <= 3)

v7 = (8 != 9) and (3 <= 3)
print('v7 = (8 != 9) and (3 <= 3)', v7)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0

#!(6 == 6) || (2 > 1)

v8 = not (6 == 6) or (2 > 1)
print('v8 = not (6 == 6) or (2 > 1)', v8)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0

#(15 > 7) && !(4 < 2)

v9 = (15 > 7) and not (4 < 2)
print('v9 = (15 > 7) and not (4 < 2)', v9)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0

#(3 * 2 == 6) && (9 / 3 == 3) 

v10 = (3 * 2 == 6) and (9 / 3 == 3)
print('v10 = (3 * 2 == 6) and (9 / 3 == 3)', v10)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0

#!(12 > 8) && (5 != 4)

v11 = not (12 > 8) and (5 != 4)
print('v11 = not (12 > 8) and (5 != 4)', v11)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0
# 0 * 1 = 0
# 0 * 0 = 0

#(2 + 2 == 4) || !(1 > 0)

v12 = (2 + 2 == 4) or not (1 > 0)
print('v12 = (2 + 2 == 4) or not (1 > 0)', v12)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0
# 1 * 0 = 1

#(9 % 3 == 0) && (7 - 4 != 2)

v13 = (9 % 3 == 0) and (7 - 4 != 2)
print('v13 = (9 % 3 == 0) and (7 - 4 != 2)', v13)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0

#(5 > 2) || (6 < 1) && (8 == 8)

v14 = (5 > 2) or (6 < 1) and (8 == 8) 
print('v14 = (5 > 2) or (6 < 1) and (8 == 8)', v14)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0
# 1 * 0 = 0

#!(4 * 2 == 8) || (10 / 2 == 5)

v15 = not (4 * 2 == 8) or (10 / 2 == 5)
print('v15 = not (4 * 2 == 8) or (10 / 2 == 5)', v15)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0
# 1 * 0 = 0

#(14 >= 7) && !(3 == 3)

v16 = (14 >= 7) and not (3 == 3)
print('v16 = (14 >= 7) and not (3 == 3)', v16)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0
#$ 1 * 0 = 0

#(14 >= 7) && !(3 == 3)

v17 = (14 >= 7) and not (3 == 3)   
print('v17 = (14 >= 7) and not (3 == 3)', v17)

# 1 * 1 = 1
# 0 * 1 = 0
# 0 * 0 = 0
# 1 * 0 = 0