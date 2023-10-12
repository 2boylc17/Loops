'''print("How many mountains should be displayed?")
num = int(input())
for count in range(num):
    print("        __")
    print("       /   \_")
    print("      / ^    \ ")
    print("     / ^      \_")
    print("   _/ ^ ^     ^ \ ")
    print("  / ^      ^     \ ")

print("How far are we from the target?")
distance = int(input())
counter = distance
for count in range(0, distance, 1):
    print(f"{counter} steps remaining")
    counter = counter - 1
print("Target found")


print("Please enter a word to reverse")
user_word = input()
new_word = ''
for count in range(len(user_word)):
    new_word = (new_word + user_word[len(user_word) - count - 1])
print(new_word)
'''