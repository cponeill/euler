begin=1
end=100
f=[]
even_nums=[]

def even(x):
        if (x % 2 == 0):
                return x

def answer():
        for y in range(begin,end):
                if i > 2:
                        y=f[i-2]+f[i-3]
                        f.append(even)
                else:
                        f.append(i)


        for l in f:
                if even(l) and l < 4000000:
                        even.append(l)
        print sum(even)


solution(100)
