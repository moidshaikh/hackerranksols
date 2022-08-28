# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

no_of_shoes = int(input())
sizes = list(map(int, input().split()))
money = 0
stock = Counter(sizes)
# no_of_customers = int(input())
# customer_demand = []
# for _ in range(no_of_customers):
#     customer_demand.append(input().split())

for i in range(int(input())):
    x, y = list(map(int, input().split()))
    if stock[x]:
        money += y
        stock[x] -= 1
print(money)
    
