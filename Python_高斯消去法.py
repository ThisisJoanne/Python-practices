A = []
subA = []
for i in range(0,3):
    for j in range(0,3):
        while True:
            try:
                a=input("請輸入矩陣A的第{}列的第{}個值:".format(i+1, j+1).split())
                if a.isdigit:
                    subA.append(eval(a))
                    break
            except:
                print("請輸入數字")
                continue
    A.append(subA)
    subA = []

B = []
for i in range(0,1):
    for j in range(0,3):
        while True:
            try:
                b=input("請輸入矩陣B的第{}列的第{}個值:".format(i+1, j+1).split())
                if b.isdigit:
                    B.append(eval(b))
                    break
            except:
                print("請輸入數字")
                continue
def gauss(A,B):
    while True:    
        if A[0][0]!=0:
            d = A[0][0]
            for i in range(0, len(A[0])):
                A[0][i]= A[0][i]/d
            B[0]= B[0]/d
            for row in range(1, len(A)):
                if A[row][0] != 0: 
                    d = A[row][0]
                    for i in range(0, len(A[row])):
                        A[row][i]= A[row][i]-d*A[0][i]
                    B[row]= B[row] - d*B[0]
            break
        elif A[1][0]!=0:
            d = A[1][0]
            for i in range(0, len(A[1])):
                A[1][i]= A[1][i]/d
            B[1]= B[1]/d
            for row in range(0, len(A)):
                if row!=1:
                    if A[row][0] != 0: 
                        d = A[row][0]
                        for i in range(0, len(A[row])):
                            A[row][i]= A[row][i]-d*A[1][i]
                        B[row]= B[row] - d*B[1]
            break
        elif A[2][0]!=0:
            d = A[2][0]
            for i in range(0, len(A[2])):
                A[2][i]= A[2][i]/d
            B[2]= B[2]/d
            for row in range(0, 2):
                if A[row][0] != 0: 
                    d = A[row][0]
                    for i in range(0, len(A[row])):
                        A[row][i]= A[row][i]-d*A[1][i]
                    B[row]= B[row] - d*B[1]
            break
        else:
            break

    while True:    
        if (A[0][0]==0) and (A[0][1]!=0):
            d = A[0][1]
            for i in range(0, len(A[0])):
                A[0][i]= A[0][i]/d
            B[0]= B[0]/d
            for row in range(1, len(A)):
                if A[row][1] != 0: 
                    d = A[row][1]
                    for i in range(0, len(A[row])):
                        A[row][i]= A[row][i]-d*A[0][i]
                    B[row]= B[row] - d*B[0]
            break
        elif (A[1][0]==0 and A[1][1]!=0):
            d = A[1][1]
            for i in range(0, len(A[1])):
                A[1][i]= A[1][i]/d
            B[1]= B[1]/d
            for row in range(0, len(A)):
                if row!=1:
                    if A[row][1] != 0: 
                        d = A[row][1]
                        for i in range(0, len(A[row])):
                            A[row][i]= A[row][i]-d*A[1][i]
                        B[row]= B[row] - d*B[1]
            break
        elif (A[2][0]==0 and A[2][1]!=0):
            d = A[2][1]
            for i in range(0, len(A[2])):
                A[2][i]= A[2][i]/d
            B[2]= B[2]/d
            for row in range(0, 2):
                if A[row][1] != 0: 
                    d = A[row][1]
                    for i in range(0, len(A[row])):
                        A[row][i]= A[row][i]-d*A[2][i]
                    B[row]= B[row] - d*B[2]
            break
        else:
            break

    while True:    
        if (A[0][0]==0 and A[0][1]==0):
            if A[0][2]!=0:
                d = A[0][2]
                for i in range(0, len(A[0])):
                    A[0][i]= A[0][i]/d
                B[0]= B[0]/d
                for row in range(1, len(A)):
                    if A[row][2] != 0: 
                        d = A[row][2]
                        for i in range(0, len(A[row])):
                            A[row][i]= A[row][i]-d*A[0][i]
                        B[row]= B[row] - d*B[0]
                break
            elif A[0][2]==0: #########
                break
        elif (A[1][0]==0 and A[1][1]==0):
            if A[1][2]!=0:
                d = A[1][2]
                for i in range(0, len(A[1])):
                    A[1][i]= A[1][i]/d
                B[1]= B[1]/d
                for row in range(0, len(A)):
                    if row!=1:
                        if A[row][2] != 0: 
                            d = A[row][2]
                            for i in range(0, len(A[row])):
                                A[row][i]= A[row][i]-d*A[1][i]
                            B[row]= B[row] - d*B[1]
                break
            elif A[1][2]==0: #########
                break
        elif (A[2][0]==0 and A[2][1]==0):
            if A[2][2]!=0:
                d = A[2][2]
                for i in range(0, len(A[2])):
                        A[2][i]= A[2][i]/d
                B[2]= B[2]/d
                for row in range(0, 2):
                    if A[row][2] != 0: 
                        d = A[row][2]
                        for i in range(0, len(A[row])):
                            A[row][i]= A[row][i]-d*A[2][i]
                        B[row]= B[row] - d*B[2]
                break
            elif A[2][2]==0: #########
                break
        else:
            break
            
    for row in range (0,3):
        if (A[row][0]==A[row][1]==A[row][2])and(A[row][2]==0):
            if B[row]==0:
                return "此方程式為無限多組解"
                break
            elif B[row]!=0:
                return "此方程式為無解"
                break
        elif row==2:
            return B
            break
        else:
            continue
                        
X=gauss(A, B)
if X is not list:
    print(X) 
else:
    print("三元一次方程式的解:X1 = {0:8.2f}, x2={1:8.2f}, x3={2:8.2f}".format(X[0][0],X[0][1],X[0][2]))