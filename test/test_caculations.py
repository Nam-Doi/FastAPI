
import pytest
from app.caculations import add,minus,BankAccount


@pytest.fixture()
def zero_bank_account():
    print("creating bank account")
    return BankAccount()


@pytest.fixture()
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected",[
    (3,2, 5),
    (7,1,8),
    (12,4,16)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected


def test_minus():
    assert minus(8,5) == 3

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    print("testing bank account")
    assert zero_bank_account.balance == 0

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_collect_interest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55   # can chac chan gia tri so sanh dung


@pytest.mark.parametrize("deposited, withdrew, expected",[
    (200,100, 100),
    (300,299,1),
    (12,4,8)
])
def test_bank_transactions(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(Exception):
        bank_account.withdraw(200)