'''
7. Online Game Leaderboard
An online gaming platform stores players' scores.
Write a program to arrange the scores in descending order so that the
leaderboard can be displayed.
'''


n = int(input("Enter the number of players: "))
scores = []

for i in range(n):
    score = int(input(f"Enter score of player {i + 1}: "))
    scores.append(score)

# Optimized bubble sort in descending order
for i in range(len(scores)):
    swapped = False
    for j in range(len(scores) - i - 1):
        if scores[j] < scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]
            swapped = True
    if not swapped:
        break

print("Leaderboard scores in descending order:", scores)
