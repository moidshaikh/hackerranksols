def solution(args):
    # your code here
    res = []
    temp = []

    for i in range(len(args)-1):
        # if args[i] + 1 == args[i+1]:
        print(temp)
        if (args[i] + 1 == args[i+1]):
            temp.append(args[i])
        else:
            if temp[-1] == args[i] - 1:
                temp.append(args[i])
            else:
                res.append(args[i])
            
            if len(temp) > 3:
                res.append(f"{temp[0]}-{temp[-1]}")
            else:
                for j in temp:
                    res.append(j)
            temp = []

    return res


print(solution([1,2,3,43, 44,55]))

# assert solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) == '-6,-3-1,3-5,7-11,14,15,17-20'

# assert solution([-3,-2,-1,2,10,15,16,18,19,20]) == '-3--1,2,10,15,16,18-20'