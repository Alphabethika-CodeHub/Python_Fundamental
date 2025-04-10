TAX_PRICE = 0.012
PRICE_PER_MAPS = 65.7
PRICE_PER_DEVELOPER = 792.18

print("Welcome to Daffa's Game Development Service!")
type_of_game = input("What Type of Game do u Wanna Make? ")
development_people = input("How Many Developers do u Need? ")
total_map = input("How Many Maps do u Need? ")
print("############################################")
print("Requested:")
print("Type of Game: " + type_of_game)
print("Total of Developer: " + str(development_people))
print("Total Map: " + str(total_map))
print("Tax Price: " + str(TAX_PRICE))
print("############################################")
print("Estimated Cost: ")
print("Cost of Developers: $" + str(float(development_people) * float(PRICE_PER_DEVELOPER)))
print("Cost of Maps: $" + str(float(total_map) * float(PRICE_PER_MAPS)))
TOTAL_COST_WITH_TAX = ((float(development_people) * float(PRICE_PER_DEVELOPER)) + (
            float(total_map) * float(PRICE_PER_MAPS))) * TAX_PRICE
TOTAL_COST_PROJECT_WITHOUT_TAX = (float(development_people) * float(PRICE_PER_DEVELOPER)) + (
            float(total_map) * float(PRICE_PER_MAPS))
print("Total Cost of Tax: $" + str(TOTAL_COST_WITH_TAX))
print("############################################")
print("TOTAL PROJECT COST: $" + str(TOTAL_COST_WITH_TAX + TOTAL_COST_PROJECT_WITHOUT_TAX) )
