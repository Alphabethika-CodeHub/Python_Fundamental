# Change The Value to See The Changes.
weight = 1
type_shipping = "BRONZE"  # Type: BRONZE, SILVER, PLATINUM

TOTAL_COST = 0.0
GROUND_SHIPPING_BRONZE_CHARGE = 20.00
GROUND_SHIPPING_SILVER_CHARGE = 60.00
GROUND_SHIPPING_PLATINUM_CHARGE = 120.00

# 2 Pound or Less
LV1_PRICE_PER_POUND = 4.50

# 6 Pound or Less
LV2_PRICE_PER_POUND = 9.12

# 12 Pound or Less
LV3_PRICE_PER_POUND = 12.37

# 25 Pound or Less
LV4_PRICE_PER_POUND = 15.9

# 50 Pound or Less
LV5_PRICE_PER_POUND = 23.73


def CheckShippingType():
    if type_shipping == "BRONZE":
        TOTAL_COST = GROUND_SHIPPING_BRONZE_CHARGE
        return TOTAL_COST
    elif type_shipping == "SILVER":
        TOTAL_COST = GROUND_SHIPPING_SILVER_CHARGE
        return TOTAL_COST
    elif type_shipping == "PLATINUM":
        TOTAL_COST = GROUND_SHIPPING_PLATINUM_CHARGE
        return TOTAL_COST
    else:
        print("Unknown Type of Shipping.")


# Weight Shipping.
if weight <= 2:
    TOTAL_COST = CheckShippingType()
    TOTAL_COST += weight * LV1_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(TOTAL_COST))
elif weight <= 6:
    TOTAL_COST = CheckShippingType()
    TOTAL_COST += weight * LV2_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(TOTAL_COST))
elif weight <= 12:
    TOTAL_COST = CheckShippingType()
    TOTAL_COST += weight * LV3_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(TOTAL_COST))
elif weight <= 25:
    TOTAL_COST = CheckShippingType()
    TOTAL_COST += weight * LV4_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(TOTAL_COST))
elif weight <= 50:
    TOTAL_COST = CheckShippingType()
    TOTAL_COST += weight * LV5_PRICE_PER_POUND
    print("You're Using: " + type_shipping + " Type of Shipping.")
    print("Estimated Cost: $" + str(TOTAL_COST))
else:
    print("Out of Range")
