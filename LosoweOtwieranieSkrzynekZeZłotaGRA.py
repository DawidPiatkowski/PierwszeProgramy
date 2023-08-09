import random
 
chanceForChest = {'green': 75,  # percentage
                  'orange': 20,
                  'purple': 4,
                  'gold': 1
                  }
 
 
howMuchGoldFromChest = {'green': 1000,  # in kilograms :-)
                        'orange': 4000,
                        'purple': 9000,
                        'gold': 16000
                        }
 
 
drawnChestsTotal = {'green': 0,
                    'orange': 0,
                    'purple': 0,
                    'gold': 0
                    }
 
 
numberOfMovesThrougTheChamber = 5
 
chestChanceToDrawPercentage = 60
 
 
def will_draw_chest(chestChanceToDrawPercentage):
    isDrawChance = random.uniform(0, 100)
    if (isDrawChance < chestChanceToDrawPercentage):
        return 1
    else:
        return 0
 
 
for __ in range(numberOfMovesThrougTheChamber):
    if (will_draw_chest(chestChanceToDrawPercentage) == 1):
        drawnChest = random.choices(list(chanceForChest.keys()),
                                    list(chanceForChest.values()))
        addNewChest = drawnChestsTotal.get(drawnChest[0])
        drawnChestsTotal[drawnChest[0]] = addNewChest + 1
 
 
goldInDrawnChests = {
    key: drawnChestsTotal[key] * howMuchGoldFromChest[key]
    for key in drawnChestsTotal
}
 
print("\n Drawn chest total: ", drawnChestsTotal)
print("\n Gold in drawn chests: ", goldInDrawnChests)
print("\n Amount of gold in all chests: ",
      sum(goldInDrawnChests.values()), "\n")
