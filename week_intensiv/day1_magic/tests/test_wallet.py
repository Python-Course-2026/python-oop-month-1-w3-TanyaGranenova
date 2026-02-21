import pytest
from week_intensiv.day1_magic.tasks.wallet import Wallet

def test_wallet_add():
    w1 = Wallet("Alice", 100.5)
    w2 = Wallet("Bob", 50.2)
    w3 = w1 + w2
    assert w3.balance == 150.7
    assert w3.name == "Joint Account"

def test_wallet_len():
    w = Wallet("Test", 123.99)
    assert len(w) == 123, "len() должен возвращать только целую часть баланса"