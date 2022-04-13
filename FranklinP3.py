# FranklinP3
# Programmer: Anthony Franklin
# Email: afranklin18@cnm.edu
# Purpose: provides user capability to find fruit in a string


fruits = [
'Apricots',
'Asian Pears',
'Avocados',
'Bananas',
'Blackberries',
'Blueberries',
'Boysenberries',
'Cactus Pear',
'Cantaloupe',
'Cherries',
'Coconut',
'Cranberries',
'Figs',
'Gooseberries',
'Grapefruit',
'Grapes',
'Honeydew Melon',
'Kiwifruit',
'Limes',
'Longan',
'Loquat',
'Lychee',
'Madarins',
'Malanga',
'Mandarin Oranges',
'Mangos',
'Mulberries',
'Nectarines',
'Oranges','Papayas',
'Passion Fruit',
'Peaches',
'Pears',
'Persimmons',
'Pineapple',
'Plums',
'Pomegranate',
'Prunes',
'Quince',
'Raisins',
'Raspberries',
'Rhubarb',
'Strawberries',
'Tangelo',
'Tangerines',
'Tomato',
'Ugli Fruit',
'Watermelon'
]

x=[]


input_sentence=input("Please type a sentence containing at least 1 fruit name :").title()
for fruit in fruits:
     if fruit in input_sentence:
         x.append(fruit)

count=len(x)
print ("Your sentence contains the name of", str(count),"fruits.")
print ("Your fruits are ",x)
del x[0]
x.append("AND BRUSSELSPROUTS!!")
print ("For a healthier option, maybe try",x)
print()
                    
                     
