
accounts = {
    '102012': {
        'name': 'mike',
        'balance': 10000
    },
    '102013': {
        'name': 'vamsi',
        'balance': 34.5
    },
    '102014': {
        'name': 'Gajendra',
        'balance': 230500
    }
}

def show_menu():
        
    while True:
        print('''
            1. View Account Balance
            2. Transfer Amount
            3. Withdraw Amount
            4. Deposit Amount
            5. Exit
        ''')
        option = int(input('Choose an option:'))
        if option == 1:
            acc = input('Enter Acc number:')
            if acc in accounts:
                b = accounts[acc]['balance']
                print(f"Your balance is Rs.{b}/-")
            else:
                print('Account not found')
        elif option == 2:
            sa = input('Enter Source Account:')
            da = input('Enter Destination Account:')
            amount = int(input('Amount to Transfer'))
            accounts[sa]['balance'] -= amount
            accounts[da]['balance'] += amount
            print('Transfer successful.')
            pass
        elif option == 3:
            accc = input("enter  your account number:")
            if accc in accounts:
             withdrawal = int (input("withdrawal amount:"))
            accounts[accc]['balance'] -= withdrawal
            print(f"withdrawal succesfull:₹{withdrawal}.0")
            print(f"{accounts[accc]['balance']}₹. balance")
        elif option == 4:
            acc = input("enter your account number")
            if acc in accounts:
             deposit= int(input("enter deposit amount:"))
             accounts[acc]['balance'] += deposit
             print(f"deposit succesfull:₹{deposit}.0")
             print(f"{accounts[acc]['balance']}₹. balance")
        elif option == 5:
            print("EXIT")
            continue

        else:
            print('Invalid option')
            




def main():
        show_menu()

if __name__ == "__main__":
    main()