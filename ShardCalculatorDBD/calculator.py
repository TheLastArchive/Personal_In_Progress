
class User:

    def __init__(self):
        
        self.userLevel = 0
        self.userShards = 0
        self.targetShards = 0
    

def getUserInput():

        try: 
            user.userLevel = int(input("Enter your player level: "))
            user.userShards = int(input("Enter the amount of shards you have: "))
            user.targetShards = int(input("Enter the amount of shards you want: "))
            if user.targetShards - user.userShards <= 0:
                exit("You can't unearn shards retard")
            else: user.targetShards -= user.userShards    

        except ValueError:
            exit("Invalid input, retard")


def getLevelKey(shardsPerLevel):
    """Uses the userLevel to find which key to handle
    the calculations with"""

    for key in shardsPerLevel:
        if user.userLevel in range(int(shardsPerLevel[key].split("-")[0]), 
        int(shardsPerLevel[key].split("-")[1]) + 1):
            return key


#TODO
def calculate():
    """Handles the calculation"""

    hourEstimate = user.targetShards / 260

    shardsPerLevel = {0: "1-1",
                      50: "2-2",
                      65: "3-3",
                      85: "4-6",
                      150: "7-14",
                      195: "15-24",
                      235: "25-34",
                      270: "35-49",
                      300: "50-100"}

    dictKey = getLevelKey(shardsPerLevel)
    keysList = list(shardsPerLevel)
    keyListIndex = keysList.index(dictKey)
    expectedLevel = user.userLevel
    
    while user.targetShards > 0:
        if expectedLevel in range(int(shardsPerLevel[keysList[keyListIndex]].split("-")[0]), 
        int(shardsPerLevel[keysList[keyListIndex]].split("-")[1]) + 1):
            user.targetShards -= keysList[keyListIndex]
            expectedLevel += 1
        else: 
            try: 
                keyListIndex += 1
            except IndexError:
                exit("Not enough levels to reach target shards")

    print(f"Level estimate: {expectedLevel}")
    print("Hour estimate: {:.1f} hours".format(hourEstimate))

if __name__ == '__main__':
    
    user = User()
    getUserInput()
    calculate()