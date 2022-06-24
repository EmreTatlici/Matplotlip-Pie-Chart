import matplotlib.pyplot as plt

# you have fruits, users take them, and you can show the rate of selling of each fruits in the pie chart.

taken_fruits = [0,0,0,0,0]

fruits = ['elma','armut','muz','cilek','seftali']


def buyFruit(fruitName):
    for fruit in fruits:
        if fruitName == fruit:
            index = fruits.index(fruitName)
            taken_fruits[index] += 1


while True:
    option = input('1- buy fruit \n2- show pie chart\n3- exit\n')

    if option == '1':
        fruitName = input('name of fruit you want to buy: ')
        buyFruit(fruitName)


    elif islem == '2':
        pieChart = plt.pie(taken_fruits, labels= fruits,autopct='%1.1f%%')
        # explode = myexplode
        plt.legend()
        plt.show()

    elif islem == '3':
        break
    else:
        print('wrong option!!')


















