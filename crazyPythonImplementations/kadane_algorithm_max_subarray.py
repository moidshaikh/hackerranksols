def maximumSubarraySum_brute(arr):
    # time: O(n*n) mem: O(n)
    n = len(arr)
    maxSum = -1e8

    for i in range(n):
        currSum = 0
        for j in range(i, n):
            currSum = currSum + arr[j]
            if currSum > maxSum:
                maxSum = currSum

    return maxSum


def maximumSubarraySum(arr):
    # time: O(n) mem: O(1)
    n = len(arr)
    maxSum = -1e8
    currSum = 0

    for i in range(0, n):
        currSum = currSum + arr[i]
        if currSum > maxSum:
            maxSum = currSum
        if currSum < 0:
            currSum = 0

    return maxSum


if __name__ == "__main__":
    # Your code goes here
    a = [1, 3, 8, -2, 6, -8, 5]
    print(maximumSubarraySum_brute(a))
    print(maximumSubarraySum(a))
