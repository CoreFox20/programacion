#fibonacci sucession

def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    
    return fibo(n-1) + fibo(n-2)
    
def i_fibo(n):
    i = 1
    n0 = 0
    n1 = 1
    while i < n:
        f = n0 + n1
        n0 = n1
        n1 = f
        i += 1
    return f

if __name__ == "__main__":
    n = int(input(">>>"))
    print(fibo(n))
    print(i_fibo(n))