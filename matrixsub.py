def add(m1, m2):
   new = []
   for i in range(0, len(m1)):
      new.append(m1[i] + m2[i])
   return new

def subtract(m1, m2):
   new = []
   for i in range(0, len(m1)):
      new.append(m1[i] - m2[i])
   return new

# main
m1 = [[9, 2], [2, 5]]
m2 = [[1, 4], [0, 3]]
c = []
for i in range(0, len(m1)):
   c.append(add(m1[i], m2[i]))
print("Add Matrix:")
print(c)

c = []
for i in range(0, len(m1)):
   c.append(subtract(m1[i], m2[i]))
print("Subtract Matrix:")
print(c)
