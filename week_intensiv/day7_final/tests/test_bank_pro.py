import pytest
from week_intensiv.day7_final.tasks.bank_pro import BankPro, SavingsAccount, BusinessAccount


def test_transfer_with_commission():
    bank = BankPro()
    # Бизнес-счет с 2000 руб.
    biz = BusinessAccount("Corp", 2000)
    # Обычный счет с 0 руб.
    sav = SavingsAccount("Ivan", 0)

    # Перевод 1000 руб. С бизнес-счета должно списаться 1000 + 5% = 1050
    status = bank.transfer(biz, sav, 1000)

    assert status == "Успех"
    assert sav.balance == 1000, "На счет получателя должна прийти полная сумма"
    assert biz.balance == 950, "С бизнес-счета должна списаться сумма + 5% комиссии"


def test_business_overdraft():
    bank = BankPro()
    biz = BusinessAccount("Startup", 100)  # Денег мало
    sav = SavingsAccount("Other", 0)

    # Пытаемся перевести 1000 (комиссия 50). Итого 1050.
    # 100 - 1050 = -950. Это входит в лимит -1000.
    status = bank.transfer(biz, sav, 1000)

    assert status == "Успех"
    assert biz.balance == -950
    assert sav.balance == 1000


def test_insufficient_funds_all_types():
    bank = BankPro()
    sav1 = SavingsAccount("User1", 100)
    sav2 = SavingsAccount("User2", 100)

    # Обычный счет не может уйти в минус
    status = bank.transfer(sav1, sav2, 150)

    assert status == "Ошибка"
    assert sav1.balance == 100, "Баланс не должен измениться при ошибке"
    assert sav2.balance == 100


def test_business_limit_exceeded():
    bank = BankPro()
    biz = BusinessAccount("Shop", 0)
    sav = SavingsAccount("User", 0)

    # Лимит -1000. Пытаемся списать 1100 + комиссия.
    status = bank.transfer(biz, sav, 1100)

    assert status == "Ошибка"
    assert biz.balance == 0