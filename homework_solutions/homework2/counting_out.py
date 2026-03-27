from collections import deque

n = int(input("What is n?"))
k = int(input("What is k?"))

q = deque()

for i in range(1, n+1):
  q.append(i)

while len(q) > 1:

  for i in range(k-1):
    element = q.popleft()
    print(element)
    q.append(element)

  print(q.popleft(), "is out.")

  
print(q.popleft(), "is the winner.")
  

