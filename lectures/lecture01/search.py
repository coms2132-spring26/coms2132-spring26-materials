li = [3, 7, 12, 15, 22, 55] # N elements 
target = 22

#i = 0 
#for x in li:
#    if x == target:
#        break
#    i += 1
#print(i)


# A linear time algorithm T(N) = N, Linear Search 

i = 0 
while li[i] != target and i < len(li): # worst case: N iterations
    i += 1
if i >= len(li): 
    print("not in list")
else: 
    print(i)

#for i,x in enumerate(li):
#    if x == target: 
#        print(i)
#        break
#if i >= len(li):
#    print("not in list") 
    


# A logarithmic time algorithm T(N) = log_2 N, Binary Search
left = 0 
right = len(li)-1
mid = (left + right) // 2

while left <= right and li[mid] != target: 
    if li[mid] < target: 
        left = mid + 1
    elif li[mid] > target: 
        right = mid - 1
    mid = (left + right) // 2
if li[mid] != target: 
    print("Not found")
else: 
    print(mid)



