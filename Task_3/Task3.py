file = open("Task3Input", "r")

def assignValue(x):
    if x.islower():     #1-26
        return ord(x) - 96
    elif x.isupper():   #27-52
        return ord(x) - 38

priority_sum = 0

for line in file:
    length = len(line) - 1
    split_point = length // 2
    output = ""
    i = 0
    for char in line:
        i += 1
        if i < split_point:
            found = line.find(char, split_point, length)
            if found != -1:
                output = char
                priority_sum += assignValue(output)
                print(output)
                print(assignValue(output))
                break
        else:
            break
    

print(priority_sum)


    