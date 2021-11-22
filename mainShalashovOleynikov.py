stockbalance = {}

def addStock(name, count):

    stockbalance[name] = count
    return stockbalance


while True:

    print('Введите название')
    name = input()
    print('Введите количество')
    count = input()
    addStock(name, count)
    print(stockbalance)