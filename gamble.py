# Getting app ready
import os
import time
import random
running = True
bankAccount = float(random.randrange(1000, 10000))
wallet = float(random.randrange(200, 1000))
usingChoice = ""
choice = ""
transferFromWallet = 0
transferFromBank = 0

# Function to clear the terminal
def clearScreen():
    # Check the operating system
    if os.name == 'posix':  # For Unix/Linux/Mac OS
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')

# Intro screen
def introPrompt():
    choice = ""
    clearScreen()
    print("-------------====================-------------------")
    print("        Welcome to your imminent demise")
    print(" Please choose one of the given options below:")
    print("                   Bank")
    print("                  Casino")
    choice = input().lower()
    print("-------------====================-------------------")
    print(f"[{choice}]")
    time.sleep(1)

    if choice == "bank":
        bankTerminal()
    elif choice == "casino" or choice == "gamble":
        casino()

# Main bank program
def bankTerminal():
    global running
    global bankAccount
    global wallet

    # If withdraw- or deposit amount = 0
    def transfer0():    
            print("\n-------------------=====================-------------------------")
            print("                ATM Machine: Beep Boop Beep.")
            print("      The fuck are you doing you dumbass cunt, either give")
            print("      me money, take my money, or get the fuck out of here.")
            print("-------------------=====================-------------------------")

    # If withdraw amount < 0
    def withdrawNeg():
            print("\n-------------------=====================-------------------------")
            print("                ATM Machine: Beep Boop Beep.")
            print("      The fuck are you doing you dumbass cunt, you cant")
            print("           withdraw a negative amount of money.")
            print("-------------------=====================-------------------------")

    # If deposit amount < 0
    def depositNeg(): 
            print("\n-------------------=====================-------------------------")
            print("                ATM Machine: Beep Boop Beep.")
            print("      The fuck are you doing you dumbass cunt, you cant")
            print("           deposit a negative amount of money.")
            print("-------------------=====================-------------------------")

    # Banking main menu
    if running:
        clearScreen()
        print("----------------==============----------------------")
        print("      Welcome to unbranded sketchy ATM service.")
        print("\n           What would you like to do?")
        print("                    Deposit")
        print("                    Withdraw")
        print("                  Check Balance")
        print("----------------==============----------------------")
        choice = input().lower()

        # Check if choice is valid
        if choice not in ["withdraw", "with", "deposit", "dep", "balance", "check balance", "bal"]:
            print("\n----------------==============----------------------")
            print("    Sorry, your answer is invalid, try again.")
            print("       Withdraw, Deposit or Check Balance?")
            print("----------------==============----------------------")
            choice = input().lower()

        # Check balance of bank account
        if choice == "check balance" or choice == "balance" or choice == "bal":     # Check if choice is check balance
            # Make sure bankAccount is an integer
            try:
                bankAccount = int(bankAccount)
            except ValueError:
                try:
                    bankAccount = float(bankAccount)
                except ValueError:
                    print("System error.")
            # Make sure wallet is an integer
            try:
                wallet = int(wallet)
            except ValueError:
                try:
                    wallet = float(wallet)
                except ValueError:
                    print("System error.")
            # Print current balance                
            print("\n----------------==============----------------------")
            print(f"       Your current account balance is: €{bankAccount:,.2f}")
            print(f"        And you have €{wallet:,.2f} in your wallet")
            print("----------------==============----------------------") 
            choice = ""

        # Deposit from wallet to bank account
        if choice == "deposit" or choice == "dep":     # Check if choice is deposit
            print("\n----------------==============----------------------")
            print("       How much do you wish to deposit?")
            print("----------------==============----------------------")
            transferFromWallet = input().lower()      # Input amount to deposit
            
            if transferFromWallet == "all" or transferFromWallet == "max":
                print("\n------------------==================------------------------")
                print(f"         Deposited €{wallet:,.2f} from wallet to bank.")
                print("------------------==================------------------------")
                bankAccount += wallet
                wallet = 0
            else:

                # Check if withdrawn amount is greater than the amount in wallet
                if transferFromWallet > wallet:       
                    print("\n------------------====================------------------------")
                    print("   Broke ass bitch, you don't have enough cash to deposit.")
                    print("------------------====================------------------------") 
                elif transferFromWallet == 0:
                    transfer0()
                elif transferFromWallet < 0:
                    depositNeg()
                elif transferFromWallet > 0:
                    try:
                        transferFromWallet = float(transferFromWallet)
                        print("\n------------------==================------------------------")
                        print(f"         Deposited €{transferFromWallet:,.2f} from wallet to bank.")
                        print("------------------==================------------------------")
                        wallet -= transferFromWallet  
                        bankAccount += transferFromWallet
                    except ValueError:
                        transferFromWallet = int(transferFromWallet)
                        print("\n------------------==================------------------------")
                        print(f"         Deposited € {transferFromWallet:,.2f} from wallet to bank.")
                        print("------------------==================------------------------")
                        wallet -= transferFromWallet    
                        bankAccount += transferFromWallet

        # Withdraw from bank account to wallet
        if choice == "withdraw" or choice == "with":    # Check if choice is withdraw
            print("\n----------------==============----------------------")
            print("       How much do you wish to withdraw?")
            print("----------------==============----------------------")
            transferFromBank = input().lower()          # Input amount to withdraw

            if transferFromBank == "all" or transferFromBank == "max":
                print("\n------------------==================------------------------")
                print(f"         Withdrew €{bankAccount:,.2f} from bank to wallet.")
                print("------------------==================------------------------")
                wallet += bankAccount
                bankAccount = 0
            else:
                # Check if withdrawn amount is greater than the amount in bank account
                if transferFromBank > bankAccount:
                    print("\n------------------====================------------------------")
                    print("   Insufficient funds, your bank account balance is too low.")
                    print("------------------====================------------------------")
                elif transferFromBank == 0:
                    transfer0()
                elif transferFromBank < 0:
                    withdrawNeg()
                elif transferFromBank > 0:
                    try:
                        transferFromBank = float(transferFromBank)
                        bankAccount -= transferFromBank  
                        wallet += transferFromBank
                        print("\n------------------==================------------------------")
                        print(f"         Withdrew €{transferFromBank:,.2f} from bank to wallet.")
                        print("------------------==================------------------------")
                    except ValueError:
                        transferFromBank = int(transferFromBank)
                        bankAccount -= transferFromBank    
                        wallet += transferFromBank
                        print("\n------------------==================------------------------")
                        print(f"         Withdrew €{transferFromBank:,.2f} from bank to wallet.")
                        print("------------------==================------------------------")
        time.sleep(1)
        print("Do you wish to continue using this Sketchy ATM Machine?")
        print("                        Y/N")
        usingChoice = input().lower()
        if usingChoice == "n" or usingChoice == "no":
            running = False
            time.sleep(0.2)
            introPrompt()
        elif usingChoice == "y" or usingChoice == "yes":
            bankTerminal()
        else:
            print("Invalid choice.")
            time.sleep(0.25)

# Main casino program
def casino():
    global wallet
    minBet = 50
    def invalidGuess():
        print("\nInvalid guess")
    def invalidEntry():
        print("\nInvalid entry.")

    # Risk Level 1
    def gambling(riskLevel, riskReward, betAmount):
        global wallet
        global retry
        time.sleep(0.5)
        # correctNumber = random.randrange(1,riskLevel)
        correctNumber = 1
        print(f"\nPlease guess a number from 1-{riskLevel}:")
        guess = input()
        try:
            guess = int(guess)
            if 0 < guess <= riskLevel:
                print(f"\n"*2 + f"Current bet is €{betAmount:,.2f}")
                print("--------------------------------")
                print("Roling...")
                time.sleep(5)
                print(f"You guessed the number: {guess}")
                time.sleep(2)
                print(f"The rolled number is: {correctNumber}")
                time.sleep(2)
                if guess == correctNumber:
                    winnings = betAmount * riskReward
                    print("\n"*3 + "Congratulations!")
                    print("You have correctly guessed the number.")
                    print(f"You have won €{winnings:,.2f}")
                    wallet += winnings
                    print("Would you like to try again?")
                    print("Y/N")
                    retry = input().lower()
                    if retry == "y":
                        casino()
                    elif retry == "n":
                       retryPrompt
                    else:
                        invalidEntry()
                else:
                        print("\n"*3 + "Unlucky!")
                        print("You did not pick the winning number.")
                        print("Would you like to try again?")
                        print("Y/N")
                        retry = input().lower()
                        if retry == "y":
                            casino()
                        elif retry == "n":
                            retryPrompt
                        else:
                            invalidEntry()

            else:
                invalidGuess()
                gambling()    
        except ValueError:
            invalidEntry()
            gambling()

    def retryPrompt():
        print("Would you like to try again?")
        print("Y/N")
        retry = input().lower()
        if retry == "y":
            casino()
        elif retry == "n":
            mainMenuPrompt()
        else:
            invalidEntry()

    def mainMenuPrompt():
        print("Okay, would you like to go to main menu?")
        print("Y/N")
        mainMenu = input().lower()
        if mainMenu == "y":
            introPrompt()
        elif mainMenu == "n":
            exit()
        else:
            invalidEntry()

    # Risk menu
    def riskMenu(betAmount):
        print("\nPlease choose a risk level:")
        print("     Level 1: 1-10 | 5x")
        print("     Level 2: 1-20 | 15x")
        print("     Level 3: 1-40 | 35x")
        print("     Level 4: 1-70 | 50x")
        print("     Level 5: 1-99 | 80x")
        riskLevel = str(input().lower())

        # Risk Level 1
        if riskLevel == "1" or riskLevel == "level 1" or riskLevel == "level1":
            print("\nLevel 1 has been selected.")
            gambling(10, 5, betAmount)
            
        # Risk Level 2
        elif riskLevel == "2" or riskLevel == "level 2" or riskLevel == "level2":
            print("\nLevel 2 has been selected.")
            gambling(20, 15, betAmount)

        # Risk Level 3
        elif riskLevel == "3" or riskLevel == "level 3" or riskLevel == "level3":
            print("\nLevel 3 has been selected.")
            gambling(40, 35, betAmount)

        # Risk Level 4
        elif riskLevel == "4" or riskLevel == "level 4" or riskLevel == "level4":
            print("\nLevel 4 has been selected.")
            gambling(70, 50, betAmount)
        
        # Risk Level 5
        elif riskLevel == "5" or riskLevel == "level 5" or riskLevel == "level5":
            print("\nLevel 5 has been selected.")
            gambling(99, 80, betAmount)

        else:
            invalidEntry()
            time.sleep(1)
            riskMenu()

    # Gambling program
    def gambleMenu():
        print("             Please enter how much you're willing to bet:")
        betAmount = input()
        if betAmount == "all" or betAmount == "max":
            betAmount = wallet
            riskMenu(betAmount)
        else:
            try:
                betAmount = float(betAmount)
                if betAmount < minBet:
                    print("\n                 The minimal amount you can bet is €50.")
                    gambleMenu()

                elif betAmount > wallet:
                    print("\n         You can not bet more than you have.")
                    print("If necessary you can go to the bank and withdraw some money.")
                    print("          Would you like to go to the bank?")
                    print("                         Y/N")
                    returnChoice = input().lower()
                    if returnChoice == "y":
                        bankTerminal()
                    elif returnChoice == "n":
                        print("\nWell what now? I guess either lower your bet, or dont gamble.")
                        time.sleep(1)
                        gambleMenu()
                    else:
                        invalidEntry()
                        time.sleep(1)
                        gambleMenu()
                else:
                    riskMenu(betAmount)

            except ValueError:
                print(f'Well you cant gamble "{betAmount}"\n')
                gambleMenu()
    # Initiating casino
    clearScreen()
    print("--------------------------================--------------------------")
    print("                       Welcome to the casino")
    gambleMenu()

introPrompt() # Initiate intro screen
