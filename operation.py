import json
import time

def account_creation(user_name, currency_name, balance = 0):
    """
    create an account based on user name, currency type and initial balance
    """

    if currency_name not in ["HKD","USD","SGD"]:
        print("Illegal currency name, please input HKD, USD or SGD")
        return

    with open('accounts.json','r') as f:
        accounts = json.load(f)

    if user_name in accounts.keys():
        if currency_name in accounts[user_name]:
            print("This currency account existed, please use another currency name")
        else:
            accounts[user_name][currency_name] = [balance,[],[]]
            print(f"User name: {user_name}, Currency name: {currency_name} account has been created")
    else:
        accounts[user_name] = {currency_name:[balance,[],[]]}
        print(f"User name: {user_name}, Currency name: {currency_name} account has been created")
    with open("accounts.json", 'w') as f:
        json.dump(accounts, f)
        

def money_deposit(user_name, currency_name, amount):
    """
    Deposit based on user name, currency type and deposit amount
    """
    with open('accounts.json','r') as f:
        accounts = json.load(f)
    if user_name in accounts.keys():
        if currency_name in accounts[user_name]:
            accounts[user_name][currency_name][0] += amount
            accounts[user_name][currency_name][2].append((time.time(),"Deposit","+"+str(amount)))

            print(f"successfully deposit {amount} {currency_name} to {user_name} {currency_name} account")
        else:
            print("Currency account doesn't exist")
    else:
        print(f"User name {user_name} doesn't exist")


    with open("accounts.json", 'w') as f:
        json.dump(accounts, f)

def money_withdrawal(user_name, currency_name, amount):
    """
    Withdrawal based on user name, currency type and withdrawal amount
    """
    with open('accounts.json','r') as f:
        accounts = json.load(f)
    if user_name in accounts.keys():
        if currency_name in accounts[user_name]:
            if accounts[user_name][currency_name][0] >= amount*1.01:
                if len(accounts[user_name][currency_name][1]) < 5:

                    accounts[user_name][currency_name][0] -= amount*1.01
                    accounts["OSL_FEE"][currency_name][0] += amount*0.01
                    accounts[user_name][currency_name][1].append(time.time())
                    accounts[user_name][currency_name][2].append((time.time(),"Withdrawal",-1*amount))
                    accounts[user_name][currency_name][2].append((time.time(),"Withdrawal FEE",-0.01*amount))

                    print(f"successfully withdrawal {amount} {currency_name} from {user_name} {currency_name} account")
                else:
                    if time.time() - accounts[user_name][currency_name][1][0]> 300:
                        accounts[user_name][currency_name][0] -= amount*1.01
                        accounts["OSL_FEE"][currency_name][0] += amount*0.01
                        accounts[user_name][currency_name][1].pop(0)
                        accounts[user_name][currency_name][1].append(time.time())
                        accounts[user_name][currency_name][2].append((time.time(),"Withdrawal",-1*amount))
                        accounts[user_name][currency_name][2].append((time.time(),"Withdrawal FEE",-0.01*amount))
                        print(f"successfully withdrawal {amount} {currency_name} from {user_name} {currency_name} account")
                    else:
                        print("you have withdrawaled 5 times in 5 minutes, please wait for a moment")
                
            else:
                print("insufficient funds to withdrawal")
        else:
            print("Currency account doesn't exist")
    else:
        print(f"User name {user_name} doesn't exist")


    with open("accounts.json", 'w') as f:
        json.dump(accounts, f)

def money_transfer(user_out, user_in, currency_name, amount):
    """
    Transfer based on two user names, currency type and transfer amount
    """

    with open('accounts.json','r') as f:
        accounts = json.load(f)

    if user_out in accounts.keys() and user_in in accounts.keys():
        if currency_name in accounts[user_out] and currency_name in accounts[user_in]:
            if accounts[user_out][currency_name][0] >= amount*1.01:
                accounts[user_out][currency_name][0] -= amount*1.01
                accounts[user_in][currency_name][0] += amount
                accounts["OSL_FEE"][currency_name][0] += amount*0.01

                accounts[user_out][currency_name][2].append((time.time(),"Transfer out","+"+ str(amount)))
                accounts[user_out][currency_name][2].append((time.time(),"Transfer out FEE","+"+str(0.01*amount)))
                accounts[user_in][currency_name][2].append((time.time(),"Transfer in","+"+ str(amount)))
                
                print(f"successfully transfer {amount} {currency_name} from {user_out} to {user_in}")
            else:
                print("insufficient funds to transfer")
        else:
            print("Currency account doesn't exist")
    else:
        print(f"User name doesn't exist")


    with open("accounts.json", 'w') as f:
        json.dump(accounts, f)

def list_bank_account_balance(user_name):
    with open('accounts.json','r') as f:
        accounts = json.load(f)
    if user_name in accounts.keys():
        for currency in accounts[user_name].keys():
            print(f"User name: {user_name}, Currency name: {currency}, Available Balance: {accounts[user_name][currency][0]}")
    else:
        print("User name doesn't exist")

def display_transaction_statement(user_name):
    with open('accounts.json','r') as f:
        accounts = json.load(f)

    if user_name in accounts.keys():

        for currency in accounts[user_name]:
            for information in accounts[user_name][currency][2]:
                print(time.asctime(time.localtime(information[0])), currency , information[1],information[-1])

    else:
        print(f"User name {user_name} doesn't exist")