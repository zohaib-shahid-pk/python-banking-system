deposit_amount=0

def deposit():
    global deposit_amount
    salary_deposit=input("Enter Your deposit Amount: ").strip()

    if salary_deposit == "":
        print("you don't have enter money ")
    elif salary_deposit.isdigit():
        deposit_amount += (int(salary_deposit))
        print("your ammount is successfully add" , deposit_amount)
    else:
        print("text Invild, please enter number")



withdraw_amount=0
def withdraw():

    global deposit_amount
    salary_withdraw=input("Enter Your withdraw Amount: ").strip()
    if salary_withdraw == "":
        print("You donot enter amount to for withdraw")
    elif salary_withdraw.isdigit():
        withdraw_amount=int(salary_withdraw)
        if withdraw_amount < deposit_amount:
            #deposit_amount-=withdraw_amount

            print("withdraw successfully : ",withdraw_amount)
        else:
            print("your withdraw amount is greater the deposit account so Withdraw invalid")
    else:
        print("you enter aphabit so execution invalid")



def show_current_account():
    print("Your current balance is : ",deposit_amount)




def suggest_one(x):

    match x:
        case 1:
            show_current_account()
        case 2:
            withdraw()
        case 3:
            deposit()
        case _:
            show_current_account()


while True:
    print("Your have use your account")
    choice=input("press Y/N : ")
    if choice=='y':
        match choice:
            case 'y':
                print("choose one of them")
                print("show current amount :  1")
                print("withdraw amount :  2")
                print("deposit amount :  3")
                select = int(input("Enter number: "))
                suggest_one(select)
            case 'n':
                print("exite account successfully")
            case _:
                print("your enter wrong alphabit")
    else:
        break


