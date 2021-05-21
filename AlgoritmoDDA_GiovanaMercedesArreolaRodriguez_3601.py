import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2, color):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    steps = 0

    if(dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)

    xInc = float(dx/steps)
    yInc = float(dy/steps)

    xInc = round(xInc,1)
    yInc = round(yInc,1)

    for i in range(0, int(steps + 1)):
        plt.plot(round(x1),round(y1),color, color="purple")
        x1 += xInc
        y1 += yInc

        print("Valor en X = ", x1)
        print("Valor en Y = ", y1)
    plt.title("Algoritmo DDA")
    plt.ylabel("Eje y")
    plt.xlabel("Eje x")
    plt.grid()  
    plt.show()    

    print()
    print("Valores")
    print("dx = ", dx)
    print("dy = ", dy)
    print("steps = ", steps)
    print("xInc = ", xInc)
    print("yInc = ", yInc)

def main():
    x1 = int(input("Ingresa el valor para x1: "))
    y1 = int(input("Ingresa el valor para y1: "))
    x2 = int(input("Ingresa el valor para x2: "))
    y2 = int(input("Ingresa el valor para y2: "))    
    color = "r."

    DDA(x1, y1, x2, y2, color)

if __name__ == "__main__":
    main()    
    
