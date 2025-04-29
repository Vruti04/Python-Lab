#Q4
def food():
    
    food_items=[('Panner tikka',99),('Hakka noodles',109),('Veg Sandwich',119),('Panner chilli',149)]
    for x in food_items:
        print(x)
    print(sorted(food_items))
    import operator
    print(sorted(food_items,key=operator.itemgetter(1),reverse= True))
food()

