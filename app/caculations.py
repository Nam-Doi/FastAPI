def add(nums1: int, nums2: 2):
    return nums1 + nums2


def minus(nums1: int, nums2: 2):
    return nums1 - nums2



class BankAccount():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds in account")
        self.balance -= amount
    def collect_interest(self):
        self.balance *=1.1
