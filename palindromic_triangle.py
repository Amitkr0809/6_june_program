#  palindromic_triangle

def palindromic_triangle(N):
    for row in range(N):
        k=ord("A")
        for col in range(row+1):
            print(chr(k),end=" ")
            k=k+1
        for col in range(k-2,64,-1):
            print(chr(col),end=" ")
        print()

N=int(input("enter Number: "))
palindromic_triangle(N)