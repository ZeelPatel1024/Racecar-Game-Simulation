import random
import math

#When creating a class, it can be done either in the same .py file that it is used or as a separate file.
#If it is a separate file you would have to link them by using an import statement.
class Car:

# The init def is standard to all classes.  It is used to create all of the variables that you will use in your class
# Notice there are no globals.  They are not necessary in a class.  The word self is used throughout the class
# to indicate that the variable is available everywhere.  You may still use local variables in a method without
# the word self

# The parameters in the init def are the ones that will be used when you create an object.  Typically these are things
# that may be different in each object.  If there is a variable that always starts at a single value, then it is simply
# set to that value in the init def
  def __init__(self, owner, carname, speed, handling, braking, gasStop,color,wheels):


      #speed, handling and braking he did rand numbers from like 0 to 100
    # These variables are set using the parameter.  They may have the same name as the parameter, but that is not
    # necessary.
    self.owner = owner

    #****************************************************
    #Create the rest of the variables needed here
    self.carname = carname
    self.speed = speed
    self.handling = handling
    self.braking = braking
    self.gasStop = gasStop
    self.color = color
    self.wheels = wheels

    # self.myTime = time

    #*****************************************
    #Create a variable called time that will be set to zero
    self.time = 0
    self.money = 0

# this def will keep track of the time spent on each lap by the car.  Time represents the total cummulative time in the race.
  def changeRaceTime(self,num):
    self.time += num
#******************************************
# create a def that will reset the time back to zero
  def resetTime(self):
    self.time = 0

  def changeMoney(self,num):
    self.money += num

  def resetMoney(self):
    self.money = 0

# The next few defs allow the statistics of the cars to be changed
  def changeSpeed(self,num):
    self.speed+=num

#******************************************
# create 2 more defs.  One will change the handling and one will change the braking
  def changeHandling(self,num):
      self.handling += num

  def setHandToZero(self):
    self.handling = 0

  def changeBraking(self,num):
      self.braking += num

  def setBrakToZero(self):
    self.braking = 0

  def changeWheels(self,num):
      self.wheels += num

  def setWheelsToZero(self):
    self.wheels = 0

  def setHandTo(self,num):
    self.handling = num

  def setBreakTo(self,num):
    self.braking = num

  def setWheelsTo(self,num):
    self.wheels = num

  def setSpeedTo(self,num):
    self.speed = num
# The next few defs simply return the contents of a variable.  This is necessary so that the code that uses the
# object will be able to access the data within the object.  Returns are the only way to get information out
# of a class.  These defs are simple, but it is possible to put more code than a simple return into them.
#   def getRaceTime(self):
#     return self.myTime

#******************************************
# create the rest of the defs you will need to return information
  def getRaceOwner(self):
    return self.owner

  def getRaceCarName(self):
    return self.carname

  def getRaceSpeed(self):
    return self.speed

  def getRacehandling(self):
    return self.handling

  def getRaceBraking(self):
    return self.braking

  def getGasStopRaceTime(self):
    return self.gasStop

  def getRaceTime(self):
    return self.time

  def getCarColor(self):
    return self.color

  def getCarWheels(self):
    return self.wheels

  def getMoney(self):
    return self.money


# Starting at this point is the actual program that will run.  We are out of the class.

# cars represents the array of Car objects
cars = []
carNames=["Mustang","BMW 3-Series","Porsche","Honda","Nissan"]
names = ["Jhon","Ian","Mark","Lexie","Elena"]
randColor = ["Lightning Blue", "Fire Red", "Sun Yellow", "Hot Pink", "Cloud White"]
# myCar is a single Car object
myCar=""

incSpeed = False
tampSpeed = False

incBreaking = False
tampBreaking = False

incHandeling = False
tampHandeling = False

incWheels = False
tampWheels = False

goToShop = True


# carnames contains strings that are chosen at random later
#******************************************
#create an array called carnames that will have strings representing the types of cars that will race such as Porsche

# This def will create all of the Car objects with the innitialized variables.  It is important to think through
# the Car class before doing this method so that it won't be necessary to redo it later.
# Generally you would only run this method once at the beginning of your project.  However there may be times you wish
# to add new cars to the array or remove some of the ones that are already there from the array.
def createCars():
  global myCar
  global raceInt


  # ******************************************
  #The first step is to innitialize my Car
  #choce a uper bound for speed, chose name, etc
  yourName = input("What is your name?")
  print("how many laps do you want to run")
  raceInt = int(input(""))


  myCar = Car(yourName,random.choice(carNames),random.randint(20,100), random.randint(1,5),random.randint(1,5), random.randint(1,5), random.choice(randColor), random.randint(1,5))


  myCar.resetMoney()

  # Second we innitialize all of the computer cars that will be raced against
  for i in range(5):
    cars.append(Car(names[i], random.choice(carNames), random.randint(20,100), random.randint(1,5), random.randint(1,5), random.randint(1,5), random.choice(randColor), random.randint(1,5)))

  # ******************************************

  #Once the Cars are innitialized, we need a method that will print the data so we can see what has happened
  printStats()

# This def simply prints the data in a nice way.  There is no right way to do it.
def printStats():
  global myCar
  #First we print myCar's data
  print("Stats for: " + myCar.getRaceOwner() + "\n Car Name: " + myCar.getRaceCarName() + "\n Speed: " + str(myCar.getRaceSpeed()) + "\n Handling: " + str(myCar.getRacehandling()) + "\n Braking: " + str(myCar.getRaceBraking()) + "\n GST" + str(myCar.getGasStopRaceTime()) + "\n Car Color: " + myCar.getCarColor() + "\n Car Wheel Type: " + str(myCar.getCarWheels()) + "\n")
  # ******************************************

  # Second we print all of the computers cars data

  for i in cars:
    print("Stats for: " + i.getRaceOwner() + "\n Car Name = " + i.getRaceCarName() + "\n Speed = " + str(i.getRaceSpeed()) + "\n Handling (range 1 bad, 5 best) = " + str(i.getRacehandling()) + "\n Braking (range 1 bad, 5 best) = " + str(i.getRaceBraking()) + "\n GST" + str(i.getGasStopRaceTime()) + "\n Car Color: " + i.getCarColor() + "\n Car Wheels: " + str(i.getCarWheels()) + "\n")



  # ******************************************


# This def actually runs the race
def runRace():
  global myCar
  global raceInt
  global incSpeed
  global tampSpeed
  global incBreaking
  global tampBreaking
  global incHandeling
  global tampHandeling
  global incWheels
  global tampWheels
  global temp

  temp = 0
  #Step 1 is to reset all of the times in the objects back to zero.  This is necessary if you plan on running more
  # than 1 race
  myCar.resetTime()
  for x in cars:
    x.resetTime()



  # myCar[5].resetTime(0)
  # print(myCar[5].getRaceTime())

  # ******************************************

  # We can now ask how many laps that want to be run.  This isn't necessary but adds some interest.


  # The next loop run the race for however many laps you have chosen.
  # The equation that you use to run the race is arbitrary at this point.  The goal would be to use the attributes
  # that you have chosen for your cars in and equation such that the end result makes sense.
  # ******************************************

  for i in range(raceInt):

    temp = 100 / (math.sqrt(myCar.getRaceSpeed()) + math.sqrt(myCar.getRacehandling()) / 2 +
                math.sqrt(myCar.getRaceBraking()) / 2 + math.sqrt(myCar.getGasStopRaceTime()/4)  + math.sqrt(myCar.getCarWheels()/2))

    myCar.changeRaceTime(temp)

    for x in cars:
      temp = 100 / (math.sqrt(x.getRaceSpeed()) + math.sqrt(x.getRacehandling()) / 2 +
                    math.sqrt(x.getRaceBraking()) / 2 + math.sqrt(x.getGasStopRaceTime() / 4) + math.sqrt(
                x.getCarWheels() / 2))
      x.changeRaceTime(temp)

  randEvent()

    # equation to calculate the time for the race
    # ******************************************



    # calling the changeRaceTime def in the class allows you to pass the variable you used in the equation into
    # your object to change the variable called time.
    # ******************************************

    #  This loop will do the same for the computer cars
    # ******************************************



# This is another method you could use to make the simulation more interesting.  You may choose to make some random
# events that have a chance of occuring during any lap of the race, before the race, or after the race.  These events
# may affect the attributes of the car temporarily (like a flat) or permanently.
def randEvent():
  global myCar
  global raceInt

  print("test")
  eventDet = random.randint(1,5)

  if eventDet == 1:
    print("OH NO Your car had a Flat Tire")
    myCar.changeRaceTime(55)




#This def is used to print the results after the race is over.
def printResults():
  global myCar
  global goToShop

  #The first step is to print the accumulated times of each car during the race.
  # print("test")

  print(myCar.getRaceOwner() + "'s time is: " + str(myCar.getRaceTime()) + "\n")

  for x in cars:
    print(x.getRaceOwner() + "'s time is: " + str(x.getRaceTime()) + "\n")

  # ******************************************


  # The second step is to find out who actually won and print the winners name.

  smallest = myCar.getRaceTime()
  winnerOwner = myCar.getRaceOwner()


  finalTimes = []
  finalOwners= []



  finalTimes.append(myCar.getRaceTime())
  finalOwners.append(myCar.getRaceOwner())

  for x in cars:
    if x.getRaceTime() < smallest:
      smallest = x.getRaceTime()
      winnerOwner = x.getRaceOwner()

    finalTimes.append(x.getRaceTime())
    finalOwners.append(x.getRaceOwner())
  #
  # print(finalTimes)
  # print(finalOwners)

  # Sorted Arrays
  finishTimes = []
  finishOwners = []

  podiumOwners = []

  for i in range(cars.__len__()+1):
    small = finalTimes[0]
    smallPos = 0

    for x in range(finalTimes.__len__()):
      if finalTimes[x] < small:
        small = finalTimes[x]
        smallPos = x

  # print(smallPos)
    finishTimes.append(small)
    finishOwners.append(finalOwners[smallPos])

    finalTimes.pop(smallPos)
    finalOwners.pop(smallPos)
  #
  # print(finishTimes)
  # print(finishOwners)

  print(winnerOwner + " is the Winner!")

  for i in range(0,3):
    podiumOwners.append(finishOwners[i])
  #
  # print("PO is: " + str(podiumOwners))

  print("1st Place Goes To: " + finishOwners[0] + " with the time of " + str(finishTimes[0]))
  print("2nd Place Goes To: " + finishOwners[1] + " with the time of " + str(finishTimes[1]))
  print("3nd Place Goes To: " + finishOwners[2] + " with the time of " + str(finishTimes[2]))

  for x in podiumOwners:
    if x == myCar.getRaceOwner():
      myCar.changeMoney(100)
      print("You have this much money: " + str(myCar.getMoney()))
      print("Congrats you came in the top 3, this means you can decide if you want to change your stats. Would you like to change your stats? Note: If you change your stats now then you can't go to the shop. \n Yes \n No")
      inp = input("")
      if inp == "yes":
        goToShop = False
        improveStats(podiumOwners)



  # ******************************************


# This def is used to improve the stats of the cars after the race.  The code should fit some criteria you have
# established.  For instance you may choose to only improve the stats of the winners or you may choose to make the
# players buy upgrades with some amount of money they have won.
def improveStats(PO):
  # First step is improve the stats of the computer cars
  global myCar

  print("Welcome to improve stats. What would you like to improve? \n 1. Speed \n 2. Handling \n 3. Braking")
  inp = input("")

  if inp == "1":
    myCar.changeSpeed(random.randint(1,10))
  elif inp == "2":
    myCar.setHandTo(random.randint(1,5))
  elif inp == "3":
    myCar.setBreakTo(random.randint(1,5))

  for x in PO:

    for i in cars:

      if(x == i.getRaceOwner()):
        if inp == "1":
          i.changeSpeed(random.randint(1, 10))
        elif inp == "2":
          i.setHandTo(random.randint(1, 5))
        elif inp == "3":
          i.setBreakTo(random.randint(1, 5))


  printStats()


def startShop():
  global incSpeed
  global tampSpeed
  global incBreaking
  global tampBreaking
  global incHandeling
  global tampHandeling
  global incWheels
  global tampWheels

  print("Welcome to the shop, I am Karen how can I help you today? \n1: Upgrade Car Speed ($10)\n2: Upgrade Car Braking ($20) \n3: Upgrade Car Handeling ($30) \n4: Change Car Wheels ($50)")
  inp = input("")

  if inp == "1":
    print("Ah so you want to change your speed, let me see what I have for you")
    print("...Mikie is going through his stuff")
    print("...Checking bills....")

    if myCar.getMoney() > 10:
      print("Here is what I got: You can chose to buy one of the following speed bosters for &10 \n1:  Get a speed boost (Able to use during race to speed up your car once) \n2: Tamper Speed (Use to tramper with the speed of a computers car)")
      ans1 = input("")
      myCar.changeMoney(-10)

      if ans1 == "1":
        incSpeed = True
        changeStuffRelatedToSpeed()
      elif ans1 == "2":
        tampSpeed = True
        changeStuffRelatedToSpeed()

    else:
      print("Sorry it seems you need more money. Have a nice day")

  if inp == "2":
    print("Ah so you want to change your breaking, let me see what I have for you")
    print("...Mikie is going through his stuff")
    print("...Checking bills....")

    if myCar.getMoney() > 10:
      print("Here is what I got: You can chose to buy one of the following breaking bosters for &20 \n1: Increase Breaking by 1 \n2: Tamper Braking of another car")
      ans2 = input("")
      myCar.changeMoney(-20)

      if ans2 == "1":
        incBreaking = True
        changeStuffRelatedToBreaking()
      elif ans2 == "2":
        tampBreaking = True
        changeStuffRelatedToBreaking()

    else:
      print("Sorry it seems you need more money. Have a nice day")

  if inp == "3":
    print("Ah so you want to change your handeling, let me see what I have for you")
    print("...Mikie is going through his stuff")
    print("...Checking bills....")

    if myCar.getMoney() > 10:
      print("Here is what I got: You can chose to buy one of the following handeling bosters for &30 \n1: Increase handeling by 1 \n2: Tamper handeling of another car")
      ans3 = input("")
      myCar.changeMoney(-30)

      if ans3 == "1":
        incHandeling = True
        changeStuffRelatedToHandeling()
      elif ans3 == "2":
        tampHandeling = True
        changeStuffRelatedToHandeling()


    else:
      print("Sorry it seems you need more money. Have a nice day")


  if inp == "4":
    print("Ah so you want to change your wheels, let me see what I have for you")
    print("...Mikie is going through his stuff")
    print("...Checking bills....")

    if myCar.getMoney() > 10:
      print("Here is what I got: You can chose to buy one of the following wheel bosters for &50 \n1: Increase wheels by 1 \n2: Tamper wheels of another car")
      ans5 = input("")
      myCar.changeMoney(-50)

      if ans5 == "1":
        incWheels = True
        changeStuffRealtedToWheel()
      elif ans5 == "2":
        tampWheels = True
        changeStuffRealtedToWheel()

    else:
      print("Sorry it seems you need more money. Have a nice day")


def changeStuffRelatedToSpeed():
  global incSpeed
  global tampSpeed
  global myCar
  print("you chose to change speed")

  if incSpeed == True:
      myCar.changeSpeed(10)
      print("Your cars new speed is: " + str(myCar.getRaceSpeed()))
  else:
    print(" ")

  if tampSpeed == True:
    choise = random.choice(cars)
    print("You sabatoged: " + choise.getRaceOwner() + "'s speed")
    choise.changeSpeed(-10)
  else:
    print(" ")

def changeStuffRelatedToBreaking():
  global incBreaking
  global tampBreaking
  global myCar
  print("you chose to change breaking")

  if incBreaking == True:
      myCar.changeBraking(1)
      if myCar.getRaceBraking() > 5:
        myCar.changeBraking(-1)
      print("Your Cars breaking is: " + str(myCar.getRaceBraking()))
  else:
    print(" ")

  if tampBreaking == True:
    choise = random.choice(cars)
    print("You sabatoged: " + choise.getRaceOwner() + "'s braking")
    choise.setBrakToZero()
  else:
    print(" ")

def changeStuffRelatedToHandeling():
  global incHandeling
  global tampHandeling
  print("You chose to change handeling")

  if incHandeling == True:
      myCar.changeHandling(1)
      if myCar.getRacehandling() > 5:
        myCar.changeHandling(-1)
      print("Your Cars handling is: " + str(myCar.getRacehandling()))
  else:
    print(" ")

  if tampHandeling == True:
    choise = random.choice(cars)
    print("You sabatoged: " + choise.getRaceOwner() + "'s handeling")
    choise.setHandToZero()
  else:
    print(" ")

def changeStuffRealtedToWheel():
  global incWheels
  global tampWheels
  print("You chose to change wheels")

  if incWheels == True:
      myCar.changeWheels(1)
      if myCar.getCarWheels() > 10:
        myCar.changeWheels(-3)
      print("Your Cars wheels are: " + str(myCar.getCarWheels()))
  else:
    print(" ")

  if tampWheels == True:
    choise = random.choice(cars)
    print("You sabatoged: " + choise.getRaceOwner() + "'s wheel's")
    choise.setWheelsToZero()
  else:
    print(" ")

  #hint for cheking win if you have varibvble x and put the first cars speed into that var, and take the next car and check if it is saller then x, if so your winning, check the other car against its speed.

  # ******************************************

  #Second step is to improve the stats of my car.
  # ******************************************

def reRandomiseCarSetting():
  for x in cars:
    x.setSpeedTo(random.randint(20,100))
    x.setBreakTo(random.randint(1,5))
    x.setHandTo(random.randint(1,5))
    x.setWheelsTo(random.randint(1,5))

#This method runs the entire project
def main():
  global incSpeed
  global tampSpeed
  global incBreaking
  global tampBreaking
  global incHandeling
  global tampHandeling
  global incWheels
  global tampWheels

  global goToShop
  # print("this is a place holdler")
  raceAgain = True
  createCars()
  while(raceAgain):
    runRace()
    printResults()
    print("Do you want to go to the shop? \n1: Yes \n2: No")
    inp2 = input("")
    if inp2 == "1":
      if goToShop == False:
        print("sorry you already updated your stats, you can't use the shop")
      else:
        startShop()

    print("Do you want to race again? \n1: yes\n2 no")
    inp = input("")
    if  inp == "1":
      raceAgain = True
      printStats()
      runRace()
      incSpeed = False
      tampSpeed = False
      incBreaking = False
      tampBreaking = False
      incHandeling = False
      tampHandeling = False
      incWheels = False
      tampWheels = False
      goToShop = True
      reRandomiseCarSetting()
    else:
      raceAgain = False

  # runRace()
# ******************************************



main()