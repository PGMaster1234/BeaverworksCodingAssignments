def cost_calculator(*pizza, drinks=None, wings=None, coupon=None):
    if coupon is None:
        coupon = 0
    if wings is None:
        wings = []
    if drinks is None:
        drinks = []
    cost = 0
    cost += 13 * len(pizza)
    for p in pizza:
        for t in p:
            if t == "pepperoni":
                cost += 1
            if t == "mushroom":
                cost += 0.5
            if t == "olive":
                cost += 0.5
            if t == "anchovy":
                cost += 2
            if t == "ham":
                cost += 1.5
    print(cost)
    for d in drinks:
        if d == "small":
            cost += 2
        if d == "medium":
            cost += 3
        if d == "large":
            cost += 3.5
        if d == "tub":
            cost += 3.75
    for w in wings:
        if w == 10:
            cost += 5
        if w == 20:
            cost += 9
        if w == 40:
            cost += 17.5
        if w == 100:
            cost += 48
    coupon = cost * coupon
    cost *= 1.0625
    cost -= coupon
    return round(cost, 2)


# print(cost_calculator([], ["pepperoni", "ham"], drinks=["small", "tub"], wings=[100, 10], coupon=.5))
# print(cost_calculator(drinks=['tub'], coupon=0.1))
print(cost_calculator(['pepperoni'], [], wings=[10, 20]))
