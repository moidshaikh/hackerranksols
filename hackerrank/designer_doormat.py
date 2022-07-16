# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int,input().split())

# 3, 9, 15, 21, 27, 33
# 1, 3, 05, 07, 09, 11

li = list(range(1,n,2)) + [n] + list(range(n-2,-1,-2))
for i in li:
    if i==n:
        print("WELCOME".center(m, '-'))
    else:
        print((".|."*i).center(m, '-'))