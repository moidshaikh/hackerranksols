'''
#############################################
description in images ohms-law
1 resistance (r1) is in series with 2 resistances in parallel (r2 and r3)
we need to calculate total resistance
###############################################
Solution:
let Rp = r2r3/(r2 + r3)

Total resistance is, r1 + Rp.
Rtotal = r1 + r2r3/(r2 + r3)

The above equation gives total resistance for above given circuit.

A python program for above problem is:

'''

# r1, r2, r3 are 3 given resistances, which are of type float
r1, r2, r3 = list(map(float,input().split()))
# here, total is total resistance of the circuit.
total = r1 + r2*r3/(r2+r3)
# we print total resistance of the circuit rounded off to 2 decimals
print("total resistance is {0:.2f}".format(total))

