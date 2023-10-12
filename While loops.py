'''print('How many apples should I remove?')
apples = int(input())
removed = 0
while removed != apples and apples >= 0:
    print(f"Removed {removed + 1} apples")
    removed = removed + 1


print('How many bars should be charged?')
bars = int(input())
charged = 0
while charged != bars and bars >= 0:
    print(f'Charging:', '█ ' * (charged + 1))
    charged = charged + 1
'''

print("How many numbers should i sum up?")
numbers = int(input())
count = 0
final = 0
while count < numbers:
    print(f"Please enter number {count + 1} of {numbers}")
    final = final + int(input())
    count = count + 1
print(f"The answer is {final}")
