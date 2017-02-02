def area(c):
    return (c[2]-c[0])*(c[3]-c[1])

no_of_rectangles = int(input())

rectangles = []

while no_of_rectangles > 0:
    no_of_rectangles -= 1
    r = [int(i) for i in input().split(' ')]
    rectangles.append(r)

rectangles.sort()
areas = []
for i in range(len(rectangles)):
    # print("rectange " , i+1, "area" , area(rectangles[i]))
    areas.append(area(rectangles[i]))


print(areas)