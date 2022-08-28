# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath


x,y = '-1-5j'.split('+')
y = y[:-1]

print(abs(complex(float(x), float(y))))
print(cmath.phase(complex(float(x), float(y))))
