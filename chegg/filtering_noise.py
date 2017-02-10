"""
To be done in PYTHON
Given the a starter code:
import matplotlib.pyplot as plt
import math as m
import random as rand
x = [ d * m.pi / 180 for d in range(360*3)]
y = [m.sin(k) for k in x ]
y_noisy = [m.sin(k) + rand.gauss(0, .1) for k in x]

(a) Write a function called filter_noise that takes two parameters: 1) a list y containing the amplitudes of a noisy signal to be ltered; 2) an integer specifying the lter radius r. Your function must lter y with a moving average lter as illustrated above and return the ltered list of signal amplitudes.
When you are computing the average value for the neighbours of the i-th noisy amplitude, you can easily obtain a list of these numbers using slicing on y and the lter radius. Then compute the average of these numbers, and append the result to a new list containing the the ltered signal amplitudes. Your function must work for any r > 0 and r < len(y)/2.
The only tricky part is remembering that you can only do the averaging for indexes between r and len(y) − 1 − r, but that the returned list must be the same length as y. The r amplitudes at either end are just set to zero, as described above. One possible algorithm for this is:
- Let z be the list to be returned; initialize it to a list of r zeros.
Compute the moving average for each index of y between r and len(y) − 1 − r (inclusive), append
each result to z as you compute it.
- Append r more zeros to z.
- Return z.

(b)  In the main program, make a calltoyourfilter_noise function to filter the noisy signal y_noisy (computed for you by the starter code), and obtain the returned list of amplitudes for the ltered signal. Make sure to test your program for a variety of values of r (you can just make hard-coded function calls to do this; there is no need to obtain r using console input); it does not matter what value of r is currently being used in your function call for the nal version of your program that you hand in.
(c)  Plot both the noisy signal and the filtered signal using the matplotlib.pyplot module.Try to make the axes, titles, and labels of the plots look as close to the above plots as possible; the starter code le has some hints as to what functions in matplotlib.pyplot will be useful for this. The actual signals will not match what you see above exactly, since the noisy signal is randomly generated with each program run. See below for hints on how to achieve this with plot(). Remember to import matplotlib.pyplot to get access to the plot() function.

"""

import matplotlib.pyplot as plt
import math as m
import random as rand


def filter_noise(y, r):
    sum = 0
    result = list(0 for x in y)

    for i in range(0, r):
        sum = sum + y[i]
        result[i] = sum / (i + 1)

    for i in range(r, len(y)):
        sum = sum - y[i - r] + y[i]
        result[i] = sum / r

    return result


x = [ d * m.pi / 180 for d in range(360*3)]
y = [m.sin(k) for k in x ]
y_noisy = [m.sin(k) + rand.gauss(0, .1) for k in x]

print(filter_noise(y, ))