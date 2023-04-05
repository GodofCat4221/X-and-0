pole = ["-","-","-",
        "-","-","-",
        "-","-","-"]

def visual():
    print(pole[0], end=" ")
    print(pole[1], end=" ")
    print(pole[2])

    print(pole[3], end=" ")
    print(pole[4], end=" ")
    print(pole[5])

    print(pole[6], end=" ")
    print(pole[7], end=" ")
    print(pole[8])

Pobeda = [[0,1,2],
          [3,4,5],
          [6,7,8],
          [0,3,6],
          [1,4,7],
          [2,5,8],
          [0,4,8],
          [2,4,6]]

def hod(znak,yacheyka):
    pole[yacheyka] = znak


def result():
    win = ""
    for Y in Pobeda:
        if pole[Y[0]] == "X" and pole[Y[1]] == "X" and pole[Y[2]] == "X":
            win = "игрок за X"
        if pole[Y[0]] == "0" and pole[Y[1]] == "0" and pole[Y[2]] == "0":
            win = "игрок за 0"
    return win

proigral = False
Igrok = True

while proigral == False:
    visual()
    if Igrok == True:
        znak = "X"
        yacheyka = int(input("Игрок X"))
    else:
        znak = "0"
        yacheyka = int(input("Игрок 0"))
    hod(znak,yacheyka)
    win = result()
    if win != "":
        proigral = True
    else:
        proigral = False
    Igrok = not(Igrok)
visual()
print("Победил:", win)
