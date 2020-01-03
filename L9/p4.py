class InvalidAmount(Exception):
    def __init__(self, msg):
        self.msg = msg
class InsufficientFundsException(Exception):
    def __init__(self, res):
        self.res = res
class Bank:
    def __init__(self, no, bal):
        self.no = no
        self.bal = bal
    def __str__(self):
        return "no= " + str(self.no) + " balance=" + str(self.bal)
    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmount("amount cannot be -ve")
        self.bal += amount
    def withdraw(self, amount):
        if amount < 0:
            raise InvalidAmount("amount cannot be -ve")
        if(self.bal - amount < 1000):
            raise InsufficientFundsException("balance cannot be < 1000")
        self.bal -= amount

try:
    b = Bank(100,5000)
    print(b)
    b.withdraw(500)
    print(b)
except InvalidAmount as e:
    print(e.msg)
except InsufficientFundsException as e:
    print(e.res)
