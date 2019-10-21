q = lambda : list(map(int,input().split()))

S, T, D = q()

time = D / (S*2)
res = time * T
print("%d"%res)