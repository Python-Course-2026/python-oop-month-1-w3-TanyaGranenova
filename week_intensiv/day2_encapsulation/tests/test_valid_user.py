import pytest
from week_intensiv.day2_encapsulation.tasks.valid_user import ValidUser

def test_password_setter():
    u = ValidUser("admin", "old_password1")
    u.password = "short" # Слишком короткий
    assert u._password == "old_password1", "Пароль не должен меняться, если он короче 8 символов"

    u.password = "valid_pass_99"
    assert u._password == "valid_pass_99"

def test_password_masking():
    u = ValidUser("admin", "secret123")
    assert u.password == "********", "Геттер должен маскировать пароль"