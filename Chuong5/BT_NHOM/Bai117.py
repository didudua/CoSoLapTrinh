def Input(X, Y, XY, XX):
    while True:
        x = input('x=')
        if x == '':
            return X, Y, XY, XX
        y = float(input('y='))
        X.append(float(x))
        Y.append(y)
        XY.append(float(x)*y)
        XX.append(float(x)**2)

def Tinh(X, Y, XY, XX):
    TongX = sum(X)
    TongY = sum(Y)
    TBX = TongX/len(X)
    TBY = TongY/len(Y)
    m = (sum(XY)-(TongX * TongY / len(X))) / (sum(XX) - (TongX ** 2 / len(X)))
    b = TBY-m*TBX
    print(f'y = {round(m,2)}x + {round(b,2)} ')

X = []
Y = []
XY = []
XX = []
X, Y, XY, XX = Input(X, Y, XY, XX)
Tinh(X, Y, XY, XX)
