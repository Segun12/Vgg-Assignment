"""
        VGG Assignment 2
Build a command-line Banking Application with the following functionalities:
Application starts with a prompt to the user with the following options:
Press 1: create account
Press 2: transaction
2. Create account: This should prompt you to enter an email/or unique identity, and then a password. You must check your data structure to make sure the account is unique before creating the new account
3. Transaction: Authenticate the user by prompting for a password, if the password is correct, user is authenticated and show the following options:
Press 1: check balance
Press 2: deposit
Press 3: withdraw
Press 4: transfer
if the password is incorrect, tell the user that they are not authorized and go back to the create account option
4. check balance: query your data structure to check the balance of the authenticated user
5. deposit: prompt the user to enter an amount, then add the amount to the users balance
6. withdraw: prompt the user to enter an amount, if the user does not have money in their account, tell them to deposit and move to the deposit prompt. If they user has money, print out the amount withdrawn and the available balance,
7. transfer: prompt the user to enter an email of the person they want to transfer to, prompt for the amount, deduct the amount from the authenticated users balance, add the amount to the beneficiaries account,
Ensure that you clog all the gaps for those process flows that i have not explicitly defined.

*******************************************************************************************************
A command line banking application having the following functions;
- Open Account
- Perform transactions when user is authenticated
    -Withdraw Money
    - Deposit Money
    - Check Balance
    - Transfer Money
"""
print("=====================================")
def mainMenu():
    return input("Please press enter key to go back to main menu to perform another function or exit ...")

customerNames = ['Olabode Tosin', 'Olayinka Hameed', 'David Susan', 'Olabode Temitope', 'Olamide Temilase']
customerPins = ['0123', '2575', '7275', '2312', '5049']
customerBalances = [10000, 20000, 20000, 40000, 10000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

# This statement below helps the program to run continuously.
while True:
    # os.system("cls")
    print("=====================================")
    print(" ----Welcome to VGG Bank----         ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Other Transaction          >>=")
    print("=<< 3. Exit/Quit                  >>=")
    print("*************************************")
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your choice number from the above menu : ")
    # Account Opening
    if choiceNumber == '1':
        user = str(input('Input Full Name: ')).lower()
        password = str(input("Please input a password of your choice : "))


        if user in customerNames:
            print("User already exsist")
            print("\n")
        else:
            customerNames.append(user)
            customerPins.append(password)
            balance = 0.0
            deposition = float(input("Please input a value to deposit to start an account : "))
            balance = balance + deposition
            customerBalances.append(balance)
            print("\nName : ", customerNames[counter_2])
            print("Balance : -N-",customerBalances[counter_2])
            counter_1 = counter_1 + 1
            counter_2 = counter_2 + 1
            print('\n')
            print("----New account created successfully !----")
            print("Note! Please remember the Name and Password")
            print("========================================")
    
            # Account opening stops
            
    # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu()
        # other transaction
    elif choiceNumber == "2":
        print('\n')
        print("=====================================")
        print("*************************************")
        print("=<< 1. Withdraw Money             >>=")
        print("=<< 2. Deposit Money              >>=")
        print("=<< 3. Check Balance              >>=")
        print("=<< 4. Transfer Money             >>=")
        print("*************************************")
        newchoiceNumber = input("Select your choice number from the above menu : ")
        # withdraw money
        if newchoiceNumber == '1':
            j = 0
            # This while loop will prevent the user using the account if the username or pin is wrong.
            while j < 1:
                k = -1
                name = str(input("Please input your name : ")).lower()
                pin = input("Please input password : ")
                # This while loop will keep the function running when variable k is smaller than length of the
                # customerNames list.
                while k < len(customerNames) - 1:
                    k = k + 1
                    # These two if conditions find where both the name and pin matches.
                    if name == customerNames[k]:
                        if pin == customerPins[k]:
                            j = j + 1
                            # These few statement would show the balance taken from the list.
                            print("Your Current Balance: -N- ",customerBalances[k])
                            balance = (customerBalances[k])
                            # Statement below would take the amount to withdraw from user.
                            withdrawal = eval(input("Input value to Withdraw : "))
                            # The if condition below would look whether the withdraw is greater than the balance.
                            if withdrawal > balance:
                                # This statement below would take a deposition from the customer.
                                deposition = eval(input("Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                                # These few statements would update the value and show the balance to user.
                                balance = balance + deposition
                                print("Your Current Balance: -N- ", balance)
                                print("\n")
                                balance = balance - withdrawal
                                print("-\n")
                                print("----Withdraw Successfull!----")
                                customerBalances[k] = balance
                                print("Your New Balance: -N- ", balance)
                                print("\n")
                            else:
                                # Else condition mentioned above is to do withdrawal if the balance is greater than the
                                # withdraw amount.
                                balance = balance - withdrawal
                                # These few statement would update the values in the list and show it to the customer.
                                print("\n")
                                print("----Withdraw Successfull!----")
                                customerBalances[k] = balance
                                print('Money withdrawn: -N- ',withdrawal)
                                print("Your New Balance: -N- ", balance)
                                print("\n")
                if j < 1:
                    # The if condition above would work when the pin or the name is wrong.
                    print("Your name and pin does not match!\n")
                    break
                # This statement below helps the user to go back to the start of the program (main menu).
            mainMenu()
            # deposit money
        elif newchoiceNumber == '2':
            n = 0
            # The while loop below would work when the pin or the username is wrong.
            while n < 1:
                k = -1
                name = str(input("Please input your name : ")).lower()
                pin = input("Please input password : ")
                # The while loop below will keep the function running to find the correct user.
                while k < len(customerNames) - 1:
                    k = k + 1
                    # The two if conditions below would find whether both the pin and the name is correct.
                    if name == customerNames[k]:
                        if pin == customerPins[k]:
                            n = n + 1
                            # These statements below would show the customer balance and update list values according to
                            # the deposition made.
                            print("Your Current Balance: -N-", customerBalances[k])
                            balance = (customerBalances[k])
                            # This statement below takes the depositionn from the customer.
                            deposition = eval(input("Enter the value you want to deposit : "))
                            balance = balance + deposition
                            customerBalances[k] = balance
                            print("\n")
                            print("----Deposition successful!----")
                            print('Money Deposited: -N-', deposition)
                            print("Your New Balance: -N-", balance)
                if n < 1:
                    print("Your name and pin does not match!\n")
                    break
            # This statement below helps the user to go back to the start of the program (main menu).
            mainMenu()
          # deposit money ends
          
          # for balance check
        elif newchoiceNumber == "3":
            k = 5
            print("Customer name and balance: ")
            print('---------- ',customerNames[k],' ----------')
            print("-> Balance: -N-", customerBalances[k])
            print("\n")
            # This statement below helps the user to go back to the start of the program (main menu).
            mainMenu()
        elif newchoiceNumber == '4':
             k = 5
             transfer_amount = int(input("Enter amount to be transfered: "))
             beneficiary = str(input("Enter beneficiary's Name: ")).lower()
             if transfer_amount > customerBalances[k]:
                 print("----- Insufficient Fund! Please make deposit and try again -----\n")
                 mainMenu()
                 # confirming beneficiary's detail
             elif beneficiary in customerNames:
                 print("User already exsist")
                 print("\n")
             else:
                 customerNames.append(beneficiary)
                     
                # User's current balance after making a transfer
                 customerBalances[k] = customerBalances[k] - transfer_amount
                 current_balance = customerBalances[k]
                 print("------- Transfer Successful -------\nAmount transfered: ", transfer_amount, "\nBeneficiary's Name: ", beneficiary, "\nAccount Balance: ", current_balance)
                 mainMenu()
                 
        else:
            # This else function above would work when a wrong function is chosen.
            print("Invalid option selected by the customer")
            print("Please Try again!")
            # This statement below helps the user to go back to the start of the program (main menu).
            mainMenu()
    elif choiceNumber == "3":
            # These statements would be just showed to the customer.
            print("Thank you for banking with us!")
            print("Come again")
            print("Bye bye")
            quit()
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the customer")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu()
