'''print('How many apples should I remove?')
apples = int(input())
removed = 0
while removed != apples and apples >= 0:
    print(f"Removed {removed + 1} apples")
    removed = removed + 1
'''

print('How many bars should be charged?')
bars = int(input())
charged = 0
while charged != bars and bars >= 0:
    print(f'Charging:', '█ ' * (charged + 1))
    charged = charged + 1
