
water = 400
milk = 540
coffee = 120
cups = 9
money = 550
action =""
  
class CoffeeMachine:
  def __init__(self, start):
    self.start = start
    global action
    
    while self.start != 0 and self.start:
      print("\nWrite action (buy, fill, take, remaining, exit) \n")
      action = input(": ")
      action = action.lower().strip()

      if action == 'buy':
        Buy_coffee()
      elif action == 'fill':
        Fill_machine()
      elif action == 'take':
        Take_money()
      elif action == 'remaining':
        Remaining()
      break
 
def Buy_coffee():
  global water
  global milk
  global coffee
  global money
  global cups

  coffee_type = (input ("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to menu: "))
  if coffee_type == '1':
    if water - 250 > 0 and coffee - 16 > 0 and cups - 1 > 0:
      water = water - 250
      coffee = coffee - 16
      money = money + 4
      cups = cups - 1
      print("I have enough resources, making you a coffee!")
    else:
      print("Sorry, not enough resources!")


  elif coffee_type == '2':
    if water - 350 > 0 and milk - 75 > 0 and coffee - 20 > 0 and cups - 1 > 0:
      water = water - 350
      milk = milk - 75
      coffee = coffee - 20
      money = money + 7
      cups = cups - 1
      print("I have enough resources, making you a coffee!")
    else:
      print("Sorry, not enough resources!")

  elif coffee_type == '3':
    if water - 200 > 0 and milk - 100 > 0 and coffee - 12 > 0 and cups - 1 > 0:
      water = water - 200
      milk = milk - 100
      coffee = coffee - 12
      money = money + 6
      cups = cups - 1
      print("I have enough resources, making you a coffee!")
    else:
      print("Sorry, not enough resources!")

  elif coffee_type == 'back':
    pass
  else:
    print ('Please enter thr right number')
  CoffeeMachine("go")


def Fill_machine():
  global water
  global milk
  global coffee
  global cups

  add_water = int(input ('\nWrite how many ml of water do you want to add: '))
  water = water + add_water
  add_milk = int(input ('\nWrite how many ml of milk do you want to add: '))
  milk = milk + add_milk
  add_coffee = int(input ('\nWrite how many grams of coffee beans do you want to add: '))
  coffee = coffee + add_coffee
  add_cups = int(input ('\nWrite how many disposable cups of coffee do you want to add: '))
  cups = cups + add_cups
  print("")
  CoffeeMachine("go")

def Take_money():
  global money
  print ('\nI gave you $' + str(money))
  money = money - money
  CoffeeMachine("go")
  

def Remaining():
  print("\nThe coffee machine has:")
  print(str(water) + " of water") 
  print(str(milk)+ " of milk")
  print(str(coffee) + " of coffee beans")
  print(str(cups) + " of disposable cups")
  print("$" + str(money) + " of money\n")
  CoffeeMachine("go")

CoffeeMachine("go")



