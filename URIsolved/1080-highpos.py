#Read 100 integer numbers. Print the highest read value and the input position.
highest = 0
for i in range(0, 100):


    a = int(input())
    if a > highest:
        highest = a
        pos = i+1

print(highest)
print(pos)
