import random
mina = " ◙ "
nada = "   "
marca = " □ "
while True:
  dificultad = input("Ingrese la dificultad (facil-0, medio-1, dificil-2, random-3): ")
  if not(dificultad.isdecimal() == False or int(dificultad) <0 or int(dificultad) >3):
    if dificultad == "3":
      dificultad = random.choice([0,1,2])
    dificultad = int(dificultad)
    break
  print("valor no valido, vuelva a ingresa la dificultad")
  print("")
ancho = 10*(dificultad+1) - dificultad*(dificultad+1)
largo = 8 + 6*dificultad
columna_1 = []
tablero = []
for i in range(largo):
  for i in range(ancho):
    columna_1 += [" ■ "]
  tablero += [columna_1]
  columna_1 = []
columna = []
tablero_juego = []
for i in range(largo):
  for i in range(ancho):
    columna += [nada]
  tablero_juego += [columna]
  columna = []
num_minas = int((dificultad+1)*(dificultad+3)*(dificultad+2)*9/6 + (dificultad+1)**2)
print(num_minas)
valor = 0
print(" ")
s = 0

for i in range(largo):
  for j in range(ancho):
    print("|{:<3}|".format(valor) , end='')
    valor+=1
  print(" ")
print("""esta es la guia para legir un recuadro
""")
for i in range(largo):
  for j in range(ancho):
    print(tablero[i][j], end='')
  print()

while True:
  d = True
  while True:
    decision = input("¿que quieres hacer? (marcar mina = 0, desvelar cuadro = 1): ")
    if not(decision.isdecimal() == False or (int(decision) not in range(2))):
      decision = int(decision)
      break
    else:
      print("Valor no valido")
  while True:
    jugada = input("Elige la pocion del cuadro: ")
    if jugada.isdecimal() == False or int(jugada) not in range(ancho*largo):
      print("Valor ingresado no valido")
    else:
      jugada = int(jugada)
      x,y = jugada//ancho, jugada % ancho
      break
  if decision == 1:
    while s == 0:
      count= 0
      while count < num_minas:
        c = False
        reemplazar = random.choice(range(ancho*largo))
        X = reemplazar//ancho
        Y = reemplazar%ancho
        count +=1
        for ix in range(-1, 2):
          for iy in range(-1, 2):
            if (X == (x+ix) and Y == (y+iy)) or tablero_juego[X][Y]==mina:
              c = True
              break
          if c:
            count -=1
            break
        else:
          tablero_juego[X][Y]= mina
      for i in range(largo):
        for j in range(ancho):
          numer = 0
          for ix in range(-1, 2):
            for iy in range(-1, 2):
              if (-1<j+iy <ancho and -1<i+ix <largo):
                if tablero_juego[i+ix][j+iy] == mina:
                  numer += 1
          if tablero_juego[i][j] == nada and numer != 0:
            tablero_juego[i][j] = " "+str(numer)+" "
      s =1
    if tablero[x][y] == marca:
      print("ESTE CUADRO ESTA MARCADO, SELECCIONE OTRO")
      d = False
    elif tablero_juego[x][y] == nada:
      control = 1
      lista_1 = [x*ancho + y]
      lista_2 = []
      while control != 0 :
        for item in lista_1:
          if item not in lista_2:
            lista_2.append(item)
        control = 0
        for i in range(len(lista_2)):
          x = lista_2[i]//ancho
          y = lista_2[i] % ancho
          for ix in range(-1, 2):
            for iy in range(-1, 2):
              if (-1<y+iy <ancho and -1<x+ix <largo):
                if (tablero_juego[ix+x][y+iy] == nada) and (((ix+x)*ancho+iy+y) not in lista_2):
                  lista_1 += [(ix+x)*ancho+iy+y]
                  control += 1
      print(lista_2)

      for i in range(len(lista_2)):
        n = lista_2[i]//ancho
        m = lista_2[i] % ancho
        for ix in range(-1, 2):
          for iy in range(-1, 2):
            if (-1<m+iy <ancho and -1<n+ix <largo):
              tablero[ix+n][m+iy] = tablero_juego[ix+n][m+iy]

    elif tablero_juego[x][y] != mina and tablero_juego[x][y] != nada:
      tablero[x][y] = tablero_juego[x][y]
    else:
      print("GAME OVER")
      break
  elif decision == 0:
    if tablero[x][y] != " ■ ":
      print("NO SE PUEDE MARCA ESTE ESPACION")
    else:
      tablero[x][y] = marca
  if d:
    for i in range(largo):
      for j in range(ancho):
        print(tablero_juego[i][j], end='')
      print()
    print()
    print()
    for i in range(largo):
      for j in range(ancho):
        print(tablero[i][j], end='')
      print()
