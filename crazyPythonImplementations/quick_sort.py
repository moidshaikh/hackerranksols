from typing import List
import random
def quick_sort(li: List) -> List:
  l = len(li)
  if l <= 1:
    return li
  else:
    pivot = li.pop()
  
  higher, lower = [], []
  for i in li:
    if i > pivot:
      higher.append(i)
    else:
      lower.append(i)
  return quick_sort(lower) + [pivot] + quick_sort(higher)


print(quick_sort([3,2,1]))
print(quick_sort([3,6,8,13,53,6,8,5,4,23,23,65,23,7,3,2,3,2,1]))
print(quick_sort([3,2,3,4,36,65,3,23,12,6,4,34,12,4,1]))

