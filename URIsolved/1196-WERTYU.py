"We're gonna take the left character "
line1 = ['1','2','3','4','5','6','7','8','9','0','-','=']
line2 = ['W','E','R','T','Y','U','I','O','P','[',']', "\\"]
line3 = ['S','D','F','G','H','J','K','L',';',"'"]
line4 = ['X','C','V','B','N','M',",",".",'/']
text = str(input())
output = []
lines=''
"""for letra in text:"""
for letra in text:
    if letra == "1":
        output.append('`')
    elif letra == 'W':
        output.appnd('Q')
    elif letra == 'S':
        output.append('A')
    elif letra == 'X':
        output.append('Z')
    elif letra == ' ':
        output.append(' ')
    if letra != '1' and letra != 'W' and letra != 'S' and letra != 'X':
        if letra in line1:
            x = letra
            y = line1.index(x)
            output.append(line1[y-1])

        elif letra in line2:
            x = letra
            y = line2.index(x)
            output.append(line2[y-1])

        elif letra in line3:
            x = letra
            y = line3.index(x)
            output.append(line3[y-1])

        elif letra in line4:
            x = letra
            y = line4.index(x)
            output.append(line4[y-1])

    """if letra == len(text):
            output.append('\n')"""
    """lines+=input()+"""
print(''.join(output))
