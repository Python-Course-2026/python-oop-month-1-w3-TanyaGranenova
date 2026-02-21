import pytest
from week_intensiv.day6_systems.tasks.battle_system import Battle, Hero


def test_battle_to_the_death():
    # Сильный, но медленный против слабого
    warrior = Hero("Воин", 50, 15)
    goblin = Hero("Гоблин", 20, 5)

    battle = Battle()
    winner = battle.fight(warrior, goblin)

    assert winner == "Воин", "Воин должен был победить гоблина"
    assert goblin.hp <= 0, "У проигравшего HP должно быть <= 0"
    assert warrior.hp == 40, "Воин должен был получить 2 удара по 5 HP (пока гоблин был жив)"


def test_battle_one_shot():
    # Проверка на мгновенную победу
    titan = Hero("Титан", 100, 100)
    ant = Hero("Муравей", 1, 1)

    battle = Battle()
    winner = battle.fight(titan, ant)

    assert winner == "Титан"
    assert ant.hp <= 0
    assert titan.hp == 100, "Титан не должен был получить урон, так как убил муравья первым ударом"


def test_already_dead_hero():
    # Проверка граничного условия: один герой уже мертв
    h1 = Hero("Живой", 10, 5)
    h2 = Hero("Труп", 0, 5)

    battle = Battle()
    assert battle.fight(h1, h2) == "Живой", "Если один герой мертв, побеждает живой сразу"