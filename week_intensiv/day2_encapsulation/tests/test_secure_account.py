import pytest
from week_intensiv.day2_encapsulation.tasks.secure_account import SecureAccount

def test_balance_protection():
    acc = SecureAccount(100)
    with pytest.raises(AttributeError):
        var = acc.__balance  # Проверка на приватность
    assert acc.balance == 100

def test_deposit_validation():
    acc = SecureAccount(100)
    with pytest.raises(ValueError):
        acc.deposit(-50)
    with pytest.raises(ValueError):
        acc.deposit(0)