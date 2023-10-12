'''print("How many rows would you like?")
rows = int(input())
print("")
print("How many columns would you like?")
columns = int(input())
print("")
for count in range(0, rows, 1):
    for number in range(0, columns, 1):
        print(":-)", end="")
    print("")
    '''

print("Please enter a sequence")
seq = input()
print()
print("Please enter the character for the marker")
marker = input()
final = 0
done = 0
print()
for count in range(0,len(seq), 1):
    if seq[count] == marker:
        while done == 0:
            if seq[count] == '-':
                final = final + 1
            if seq[count] == marker:
                done = 1
print(f"Distance = {final}")
