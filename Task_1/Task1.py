file = open("Task1Input", "r")

elves = []
elf_no = 0
cal_count = 0

for line in file:
    if(line != "\n"):
        cal_count += int(line)
    else:
        elf_no += 1
        elves.append((elf_no, cal_count))
        cal_count = 0    
    
sorted_elves = elves.sort(key=lambda x: x[1])

print("Top elf is: elf #", elves[-1][0], " with ", elves[-1][1], " calories")

total_cal = 0
for elf in elves[-3:]:
    total_cal += elf[1]
print("Top 3 elves have a total of ", total_cal, " calories")