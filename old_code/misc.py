C = 4
T = 1
S = 2
B = 2

CHAIR = 35.0
TABLE = 120.5
SOFA = 240.75
BED = 367.74
TAX_PRICE = 0.78

print("Welcome to Daffa's Furniture Store!")
print("Estimated Cost: ")
print("Total Chair: " + "$" + str(CHAIR * C))
print("Total Table: " + "$" + str(TABLE * T))
print("Total Sofa: " + "$" + str(SOFA * S))
print("Total Bed: " + "$" + str(BED * B))
print("Tax Nowdays: " + "$" + str(TAX_PRICE))
print("####################################")
print("Total Cost: " + "$" + str( ((CHAIR * C) + (TABLE * T) + (SOFA * S) + (BED * B)) + ((CHAIR * C) + (TABLE * T) + (SOFA * S) + (BED * B) * TAX_PRICE) ))
