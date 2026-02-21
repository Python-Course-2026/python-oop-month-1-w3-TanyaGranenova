import pytest

from week_intensiv.day1_magic.tasks.item_comparison import Item


def test_item_less_than():
    cheap = Item("Pen", 50)
    expensive = Item("Laptop", 50000)

    assert cheap < expensive, "Метод __lt__ должен сравнивать товары по цене"
    assert not (expensive < cheap), "Метод __lt__ работает неверно при обратном сравнении"


def test_item_equality():
    item1 = Item("Phone", 1000)
    item2 = Item("Phone", 1000)
    item3 = Item("Tablet", 1000)

    assert item1 == item2, "Метод __eq__ должен возвращать True, если имя и цена совпадают"
    assert item1 != item3, "Метод __eq__ должен возвращать False, если имена разные, даже при равной цене"


def test_sorting_integration():
    # Если __lt__ реализован верно, стандартная сортировка Python сработает автоматически
    items = [Item("B", 300), Item("A", 100), Item("C", 200)]
    items.sort()

    assert items[0].price == 100
    assert items[1].price == 200
    assert items[2].price == 300, "Сортировка списка объектов не сработала через __lt__"


def test_comparison_with_different_type():
    # Злая проверка: что будет, если сравнить товар со строкой или числом?
    item = Item("Book", 100)
    try:
        # Это не должно вызывать фатальную ошибку, если студент обработал типы,
        # либо должно вести себя предсказуемо для Python.
        assert item != "Not an item"
    except Exception as e:
        pytest.fail(f"Сравнение с другим типом данных вызвало ошибку: {e}")