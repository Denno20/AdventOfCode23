import re

def multiplyPowers(minPowers):
    return minPowers["minR"] * minPowers["minG"] * minPowers["minB"]

def gamePossiblity(counter):
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    return False if counter["red"] > cubes["red"] \
    or counter["green"] > cubes["green"] \
    or counter["blue"] > cubes["blue"] else True


def countColours(colours, counter, minPowers):
    for colour in colours:
        num = re.findall(r'\d+', colour) 
        if "blue" in colour:
            counter["blue"] += int(num[0])

            if int(num[0]) >= minPowers["minB"]:
                minPowers["minB"] = int(num[0]) 

        elif "green" in colour:
            counter["green"] += int(num[0])

            if int(num[0]) >= minPowers["minG"]:
                minPowers["minG"] = int(num[0]) 

        elif "red" in colour:
            counter["red"] += int(num[0])
            
            if int(num[0]) >= minPowers["minR"]:
                minPowers["minR"] = int(num[0]) 

    return counter


def main():
    sumOfIDs = 0
    totalMinPowers = 0

    with open("input.txt", "r") as f:
        games = f.readlines()

    for i in range(0, len(games)):
        currentGame = games[i].removeprefix(f"Game {str(i+1)}: ").strip()
        subsets = currentGame.split(";")
        gamePossible = True
        minPowers = {"minR": 0, "minG": 0, "minB": 0}
        
        for subset in subsets:
            colourCount = {
                "red": 0,"green": 0,"blue": 0
            }

            countColours(subset.strip().split(", "), colourCount, minPowers)
    
            if not gamePossiblity(colourCount):
                gamePossible = False
        
        if gamePossible:
            sumOfIDs += i+1
        
        totalMinPowers += multiplyPowers(minPowers)


    print(f"Sum of IDs of possible games: {sumOfIDs}")
    print(f"The sum of the power of the sets: {totalMinPowers}")

if __name__ == "__main__":
    main()