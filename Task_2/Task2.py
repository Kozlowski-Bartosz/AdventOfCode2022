#This code is very ugly and I could 100% come up with a cleaner solution, but I've been up since every morning so sloppy code it is
file = open("Task2Input", "r")

Matchups = []
Matchups2 = []
player_actions = ["X", "Y", "Z"]  #X - rock, Y - paper, Z - scissors
enemy_actions = ["A", "B", "C"]   #A - rock, B - paper, C - scissors

#Reads matchups and put them into pairs
for line in file:
    for char in line:
        if char in player_actions:
            player_action = char
        elif char in enemy_actions:
            enemy_action = char
        elif char == "\n":
            Matchups.append([player_action, enemy_action])
            Matchups2.append([player_action, enemy_action])

def checkWinner(player_action, enemy_action):
    if player_action == "X" and enemy_action == "A":
        return "Draw"
    elif player_action == "Y" and enemy_action == "B":
        return "Draw"
    elif player_action == "Z" and enemy_action == "C":
        return "Draw"
    elif player_action == "X" and enemy_action == "C":
        return "Player"
    elif player_action == "Y" and enemy_action == "A":
        return "Player"
    elif player_action == "Z" and enemy_action == "B":
        return "Player"
    else:
        return "Enemy"
    
def checkPointsGained(player_action, outcome):
    points = 0
    if player_action == "X":
        points += 1
    elif player_action == "Y":
        points += 2
    elif player_action == "Z":
        points += 3
    
    if outcome == "Draw":
        return points + 3
    elif outcome == "Player":
        return points + 6
    else:
        return points
    
#Second part of the task
#X - lose, Y - draw, Z - win
#X - rock, Y - paper, Z - scissors
def whatToPick(enemy_action, desired_outcome):
    if enemy_action == "A":     #Enemy picked rock
        if desired_outcome == "X":
            return "Z"
        elif desired_outcome == "Y":
            return "X"
        elif desired_outcome == "Z":
            return "Y"
    elif enemy_action == "B":   #Enemy picked paper
        if desired_outcome == "X":
            return "X"
        elif desired_outcome == "Y":
            return "Y"
        elif desired_outcome == "Z":
            return "Z"
    elif enemy_action == "C":   #Enemy picked scissors
        if desired_outcome == "X":
            return "Y"
        elif desired_outcome == "Y":
            return "Z"
        elif desired_outcome == "Z":
            return "X"

totalpoints = 0
for matchup in Matchups:
    matchup.append(checkWinner(matchup[0], matchup[1]))
    matchup.append(checkPointsGained(matchup[0], matchup[2]))
    totalpoints += matchup[3]
print(totalpoints)
    
totalpoints = 0
for matchup in Matchups2:
    matchup.append(whatToPick(matchup[1], matchup[0]))
    matchup.append(checkWinner(matchup[2], matchup[1]))
    matchup.append(checkPointsGained(matchup[2], matchup[3]))
    totalpoints += matchup[4]
print(totalpoints)



