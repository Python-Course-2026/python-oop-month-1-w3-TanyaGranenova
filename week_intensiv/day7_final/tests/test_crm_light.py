import pytest
from week_intensiv.day7_final.tasks.crm_light import CRM, Client


def test_crm_add_and_get():
    crm = CRM()
    c1 = Client(1, "Alice", "alice@example.com")
    crm.add_client(c1)

    found = crm.get_client(1)
    assert found is not None
    assert found.name == "Alice"
    assert crm.get_client(999) is None, "Должен возвращать None для несуществующего ID"


def test_crm_update_dynamic():
    crm = CRM()
    c1 = Client(10, "Bob", "bob@mail.ru")
    crm.add_client(c1)

    # Обновляем только email
    crm.update_client(10, email="new_bob@mail.ru")
    assert c1.email == "new_bob@mail.ru"
    assert c1.name == "Bob", "Имя не должно было измениться"

    # Обновляем всё сразу
    crm.update_client(10, name="Robert", email="robert@mail.ru")
    assert c1.name == "Robert"
    assert c1.email == "robert@mail.ru"


def test_crm_delete():
    crm = CRM()
    crm.add_client(Client(1, "User1", "u1@test.com"))
    crm.add_client(Client(2, "User2", "u2@test.com"))

    crm.delete_client(1)
    assert len(crm.clients) == 1
    assert crm.get_client(1) is None


def test_crm_update_non_existent():
    crm = CRM()
    # Не должно падать с ошибкой, если ID не найден
    try:
        crm.update_client(404, name="Ghost")
    except Exception as e:
        pytest.fail(f"Метод update_client упал при попытке обновить несуществующего клиента: {e}")