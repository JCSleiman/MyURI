n = int(input())
output = []
for i in range(0,n):

    x, y = input().split(' ')
    x = int(x)
    y = int(y)

    if y == 0:

        output.append('divisao impossivel')

    else:

        div = x/y
        output.append(str(div))

print('\n'.join(output))
