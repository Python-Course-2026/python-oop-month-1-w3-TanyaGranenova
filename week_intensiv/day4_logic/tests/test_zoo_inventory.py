from  week_intensiv.day4_logic.tasks.zoo_inventory import ZooInventory, Animal


def test_zoo_food_calculation():
    zoo = ZooInventory()
    # Добавляем разных животных
    zoo.add_animal(Animal("Lion", 5.0))  # 5кг * 30 = 150
    zoo.add_animal(Animal("Tiger", 3.0))  # 3кг * 30 = 90

    # Итого за 30 дней: (5 + 3) * 30 = 240
    result = zoo.calculate_monthly_food()
    assert result == 240, f"Ожидалось 240 кг еды, но получено {result}"


def test_zoo_species_count():
    zoo = ZooInventory()
    zoo.add_animal(Animal("Penguin", 1.0))
    zoo.add_animal(Animal("Penguin", 1.2))
    zoo.add_animal(Animal("Elephant", 50.0))

    assert zoo.count_species("Penguin") == 2, "Метод count_species неверно считает количество одного вида"
    assert zoo.count_species("Elephant") == 1
    assert zoo.count_species("Zebra") == 0, "Для отсутствующего вида должно возвращаться 0"


def test_zoo_empty_inventory():
    zoo = ZooInventory()
    assert zoo.calculate_monthly_food() == 0, "Сумма еды для пустого зоопарка должна быть 0"
    assert zoo.count_species("Lion") == 0