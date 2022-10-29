# Life-death 
import random
class Sward:
    def __init__(self,side,number):
        self.__side = side
        self.__number = number
    def getSide(self):
        return self.__side
    def getNumber(self):
        return self.__number
    

def swards():
    swards = []
    filled = []
    for _ in range(10):
        side = random.randint(-1,1)
        number = random.randint(1,30)
        if number not in filled and side!=0:
            swards.append(Sward(side,number))
            filled.append(number)
        else:
            side = 0
            number = -1
            swards.append(Sward(side,number))

    return swards


class Betting:
    def __init__(self,number,numberOfChips):
        self.__number = number
        self.__numberOfChips = numberOfChips
    def getNumber(self):
        return self.__number
    def getNumberOfChips(self):
        return self.__numberOfChips

class Player:
    def __init__(self,name,amount,numberOfChips,numberList):
        self.__name = name 
        self.__amount = amount
        self.__numberOfChips = numberOfChips
        self.__numberList = numberList
    
    def getName(self):
        return self.__name
    
    def getAmount(self):
        return self.__amount
    
    def getNumOfChips(self):
        return self.__numberOfChips
    
    def getNumList(self):
        return self.__numberList
    
    def setNumOfChips(self,leftChips):
        self.__numberOfChips = leftChips
        return self.__numberOfChips
    
    def setNumberList(self,newList):
        self.__numberList = newList
        return self.__numberList

def inputOfPlayer(numOfChips):
    lst = []
    while numOfChips>0:
        number = int(input(("Chose a number between (1-30) : ")))
        chips = int(input("Enter chips of this number : "))
        if number>30 or number<1:
            print("Number isn't in proper range")
        elif chips>numOfChips:
            print("NOt enough chips left")
        else:
            numOfChips -= chips
            lst.append(Betting(number,numOfChips))

    return lst

def check(player,lst):
    total = 0
    for i in player.getNumList():
        for j in range(len(lst)):
            if i.getNumber() == lst[j].getNumber():
                total += (3*i.getNumberOfChips()*lst[j].getSide())
    return total 

def main():
    players = []
    print('\t\t\t\t\t\t      Welcome to life or death\n')
    print("\t\t\t\t\t\t=========== Let's Begin ============")
    bettingAmount = int(input("Enter betting amount : "))
    numberOfChips = int(input("Enter number of chips (make it even) : "))
    amountPerChips = bettingAmount/numberOfChips
     
    for i in range(2):
        name = input(f"Enter {'first' if i==0 else 'second'} player's name : ").strip()
        players.append(Player(name,bettingAmount,numberOfChips,[]))
    rounds = 1
    turn = -1 
    while (True):
        sward = swards()
        print('Players chips : ')
        for i in range(2):
                print(players[i].getName(), 'has',players[i].getNumOfChips(),'chips')
        numberOfChipsPerRound = int(input(f"Enter number of chips for round {rounds} : "))
        if numberOfChipsPerRound>players[1].getNumOfChips() or numberOfChipsPerRound>players[0].getNumOfChips()<0:
            print("You don't have enough chips")
        else:
            for i in range(2):
                print(f'Player {players[i].getName()} Guesses')
                lst = inputOfPlayer(numberOfChipsPerRound)
                players[i].setNumberList(lst)

            print('sward reveal(side,number) (-1,Death side), (0,none), (1,Life side) : ')    
            for i in range(len(sward)):
                print(f'{i+1} {sward[i].getSide(),sward[i].getNumber()}', end='  ')
                if i==4:
                    print('')
            print('')
            players[0].setNumOfChips(players[0].getNumOfChips() + check(players[0],sward) - (check(players[1],sward)))
            players[1].setNumOfChips(players[1].getNumOfChips() + check(players[1],sward) - (check(players[0],sward)))
            rounds +=1
        if players[1].getNumOfChips()<=0 or players[0].getNumOfChips()<=0 or numberOfChips<=0:
            for i in range(2):
                print(players[i].getName(), 'has',players[i].getNumOfChips(),'chips')
            for i in range(2):
                if players[i].getNumOfChips()>0:
                    print(f'You {players[i].getName()} won')
                    break
            break
main()
# main.9812{more}