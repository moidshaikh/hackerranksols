class Rectangle:
    def __init__(self, points):
        self.x1 = points[0]
        self.y1 = points[2]
        self.x2 = points[1]
        self.y2 = points[3]
        self.w = self.x2 - self.x1
        self.h = self.y2 - self.y1

    def area(self):
        return self.h * self.w


# print(Rectangle([1,3,5,6]).area())

# no_of_rectangles = int(input())
#
# rectangles = []
#
# while no_of_rectangles > 0:
#     no_of_rectangles -= 1
#     r = [int(i) for i in input().split(' ')]
#     rectangles.append(r)
# rectangles.sort()
# r = rectangles
#
# print("rectangles list:", rectangles)
# # print(r)
# areas = []
#
# for i in range(len(rectangles)-1):

a = Rectangle([1,3,6,5])
b = Rectangle([2,3,7,5])

# SI= max(0, min(XA2, XB2) - Max(XA1, XB1)) * Max(0, Min(YA2, YB2) - Max(YA1, YB1))
# SI= max(0,  min(XA2, XB2) -  Max(XA1, XB1))   * Max(0, Min(YA2, YB2) -  Max(YA1, YB1))
# si = max(0, min(a.x2,b.x2) - max(a.x1, b.x1)) * max(0,min(a.y2,b.y2) - max(a.y1,b.y1))

# x_intersection = min(max(a.x1,a.x2), max(b.x1,b.x2) - max(xmin_a, xmin_b) + 1
x_intersection = min(max(a.x1,a.x2), max(b.x1,b.x2)) - max(min(a.x1,a.x2), min(b.x1,b.x2)) + 1
y_intersection = min(max(a.y1,a.y2), max(b.y1,b.y2)) - max(min(a.y1,a.y2), min(b.y1,b.y2)) + 1

if x_intersection <= 0 or y_intersection <= 0:
    print('0')
else:
    print(x_intersection * y_intersection)