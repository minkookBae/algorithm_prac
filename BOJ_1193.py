import sys

X = int(sys.stdin.readline())

# 1줄 : [1/1], 2줄 : [1/2, 2/1] , 3줄 : [3/1, 2/2, 1/3], 4줄 : [1/4, 2/3, 3/2, 4/1], 5줄 : [5/1, 4/2, 3/3, 2/4, 1/5] ...

# n(n-1)/2 <= x 가 되도록 ? n(n-1) <= 2x 
n = 1
while(True):
    if(X==1):
        n = 2
        break
    if(n * (n-1) < 2 * X):
        n += 1
    else:
        break
# n-1 로 이전까지 다 끝남
target_str = ""

temp = int(n*(n-1)/2 - (n-1))
target = X-temp

if((n-1)%2 == 0):
    target_str += "{}/{}".format(target,(n-1)-target+1)
else:
    target_str += "{}/{}".format((n-1)-target + 1,target)

print(target_str)