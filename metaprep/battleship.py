"""You're playing Battleship on a grid of cells with RR rows and CC columns. There are 00 or more battleships on the grid, each occupying a single distinct cell. The cell in the iith row from the top and jjth column from the left either contains a battleship (G_{i,j} = 1G 
i,j
​
 =1) or doesn't (G_{i,j} = 0G 
i,j
​
 =0).
You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random from the R*CR∗C possible cells. You're interested in the probability that the cell hit by your shot contains a battleship.
Your task is to implement the function getHitProbability(R, C, G) which returns this probability.
Note: Your return value must have an absolute or relative error of at most 10^{-6}10 
−6
  to be considered correct.
Constraints
1 \le R, C \le 1001≤R,C≤100
0 \le G_{i,j} \le 10≤G 
i,j
​
 ≤1
Sample test case #1
R = 2
C = 3
G = 0 0 1
    1 0 1
Expected Return Value = 0.50000000"""


from typing import List

# Write any import statements here


def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    # Write your code here
    # return sum(list(map(sum,s))) / sum(map(len,s))
    s, c = 0, 0
    for i in range(len(G)):
        s += sum(G[i])
        c += len(G[i])
    return s / c


print(getHitProbability(2, 3, [[0, 0, 1], [1, 0, 1]]))
