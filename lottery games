import random
game = []
result = []
num = int(input("how many games do you want? "))
while len(result) < num:
    while len(game) < 6:
        n = random.randint(1, 60)
        if n not in game:
            game.append(n)
    game.sort()
    result.append(game[:])
    game.clear()
print(result)
