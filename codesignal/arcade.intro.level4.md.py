def solution(inputArray):
    res = 1
    prev = inputArray[0]
    
    for i in range(1, len(inputArray)):
        if prev < inputArray[i]:
            prev = inputArray[i]
        elif prev == inputArray[i]:
            res += 1
            inputArray[i] += 1
        else:
            df = abs(prev - inputArray[i])
            res += df
            inputArray[i] += (abs(prev - inputArray[i])+1)
            
    
    return res



print(solution([-1000, 0, -2, 0])==5)