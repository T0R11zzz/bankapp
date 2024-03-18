

class Bank:
    def __init__(self):
        pass

    def main(self):
        print("Start banking(d/w/s/x):")# d:deposit  w:withdrawl  s:show balance  x:exit
        op = input()
        match op:
            case d:
                print("Start banking")


        # inpt=input("Amount to deposit:")
        # deposit=float(inpt)
        # print("Amount $%.2f deposited" % deposit)
        #
        # inpt=input("Amount to withdraw:")
        # withdraw=float(inpt)
        # print('Amount $%.2f withdrawn' %withdraw)







if _name_=="_main_":
    Bank.main()


class Manager:
    def __int__(self,name):
        slef.name=name


class Customer:
    def __init__(self,name):
        self.name=name
        self.accounts=[]


class Account:
    def __init__(self,account_type):
        self.account_type=account_type
        self.balance=0
