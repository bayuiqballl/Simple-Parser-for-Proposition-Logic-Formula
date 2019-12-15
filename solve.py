Dict = ['pqrs','not', 'and', 'or', 'xor', 'if','then', 'iff', '(', ')']
i = 0
error = False
output = []
input = input("Input String: ")
input = input.lower() + '~'
while i<len(input) and error == False:
    if (input[i] == 'p' or input[i] == 'q' or input[i] == 'r' or input[i] == 's'):
        output.append('1')
        i = i + 1
    elif input[i] == 'i' and input[i+1] == 'f':
        i = i + 1
        if input[i+1] == 'f':
            output.append('8')
            i = i + 2
        else:
            output.append('6')
            i = i + 1
    elif input[i] == ' ' or input[i] =='~':
        i = i + 1
    else:
        found = False
        j = 0
        while j < len(Dict) and found == False:
            if input[i] == Dict[j][0]:
                Temp = j
                i = i + 1
                j = 1
                count = 1
                while j < len(Dict[Temp]):
                    if input[i] == Dict[Temp][j]:
                        count = count + 1
                    j = j + 1
                    i = i + 1
                if count == len(Dict[Temp]):
                    if Temp+1 == 11 :
                        Temp = 9
                    output.append(str(Temp+1))
                    found = True
                else:
                    output.append('error')
                    found = True
                    error = True
            j = j + 1
        if found == False:
            output.append('error')
            error = True

print(output)

i = 0
error = False
Valid = False
stack = []
stack.append(' ')
stack.append('Z')
output.append(' ')
#print(output)
while i < len(output) and error == False:
    print("STATE:", stack)
    print(output[i])
    if stack[len(stack)-1] == output[i]:
        stack.pop()
        i = i + 1
    elif stack[len(stack)-1] == 'Z' and output[i] == '9':
        stack.pop()
        stack.append('Z')
        stack.append('10')
        stack.append('Z')
        stack.append('9')
    elif stack[len(stack)-1] == 'Z' and output[i] == '2':
        stack.pop()
        stack.append('Y')
        stack.append('V')
    elif stack[len(stack)-1] == 'Z' and output[i] == '10':
        stack.pop()
    elif stack[len(stack)-1] == 'Z' and (output[i] == '3' or output[i] == '4' or output[i] == '5' or output[i] == '8'):
        stack.pop()
        stack.append('Z')
        stack.append('Y')
        stack.append('V')
    elif stack[len(stack)-1] == 'Z' and output[i] == '6':
        stack.pop()
        stack.append('Z')
        stack.append('Y')
        stack.append('7')
        stack.append('Y')
        stack.append('6')
    elif stack[len(stack)-1] == 'Z' and output[i] == '7':
        stack.pop()
    elif stack[len(stack)-1] == 'Z' and output[i] == '1' and output[i+1] != 1:
        stack.pop()
        stack.append('Z')
        stack.append('Y')
    elif stack[len(stack)-1] == 'Z' and stack[len(stack)-2] == 'Z':
        stack.pop()
    elif stack[len(stack)-1] == 'Y' and output[i] == '1':
        stack.pop()
        stack.append('1')
    elif stack[len(stack)-1] == 'Y' and output[i] == '9':
        stack.pop()
        stack.append('Z')
        stack.append('10')
        stack.append('Z')
        stack.append('9')
    elif stack[len(stack)-1] == 'Y' and output[i] == '2':
        stack.pop()
        stack.append('Y')
        stack.append('V')
    elif stack[len(stack)-1] == 'V' and output[i] == '3':
        stack.pop()
        stack.append('3')
    elif stack[len(stack)-1] == 'V' and output[i] == '4':
        stack.pop()
        stack.append('4')
    elif stack[len(stack)-1] == 'V' and output[i] == '5':
        stack.pop()
        stack.append('5')
    elif stack[len(stack)-1] == 'V' and output[i] == '8':
        stack.pop()
        stack.append('8')
    elif stack[len(stack)-1] == 'V' and output[i] == '2':
        stack.pop()
        stack.append('2')
    elif output[i] == 'error':
        error = True
    elif output[i] == ' ':
        stack.pop()
        stack.pop()
        error = True
    else:
        error = True


#print(stack)
if len(stack) == 0:
    print("VALID")
else:
    print("NOT VALID")
