def getCost(model, tokens):
    if('curie:' in model):
        price=0.012
    else:
        price=0
    return tokens / 1000 * price

def printCost(model,tokens):
        print("Cost: {:.5f}$\n".format(getCost(model,tokens)))
