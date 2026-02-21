import pytest
from week_intensiv.day6_systems.tasks.market_engine import Market, Participant, Item
from week_intensiv.day6_systems.tasks.delivery_service import DeliveryService, Order, Courier


# --- ТЕСТЫ МАРКЕТА ---
def test_market_successful_deal():
    market = Market()
    buyer = Participant("Ivan", 1000)
    seller = Participant("Shop", 0)
    iphone = Item("iPhone", 800)

    market.deal(buyer, seller, iphone)

    assert buyer.money == 200, "Деньги не списались у покупателя"
    assert seller.money == 800, "Деньги не пришли продавцу"
    assert iphone in buyer.inventory, "Товар не попал в инвентарь покупателя"


def test_market_insufficient_funds():
    market = Market()
    buyer = Participant("Poor Student", 50)
    seller = Participant("Shop", 0)
    book = Item("Python Book", 100)

    with pytest.raises(ValueError, match="Недостаточно средств"):
        market.deal(buyer, seller, book)

    assert buyer.money == 50, "Деньги не должны списываться при ошибке"
    assert len(buyer.inventory) == 0


# --- ТЕСТЫ ДОСТАВКИ ---
def test_delivery_success():
    service = DeliveryService()
    order = Order(1, "ул. Пушкина, 10")
    courier = Courier("Petr")

    result = service.deliver(order, courier)

    assert courier.is_busy is True, "Курьер должен стать занятым"
    assert order.status == "Delivered", "Статус заказа не изменился"
    assert "Petr" in result and "1" in result


def test_delivery_courier_busy():
    service = DeliveryService()
    order = Order(2, "ул. Ленина, 5")
    busy_courier = Courier("Ivan")
    busy_courier.is_busy = True  # Имитируем занятость

    result = service.deliver(order, busy_courier)

    assert result == "Курьер занят"
    assert order.status == "In processing", "Статус заказа не должен меняться, если курьер занят"