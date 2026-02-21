import pytest
from  week_intensiv.day4_logic.tasks.warehouse_manager import WarehouseManager, Product

def test_warehouse_logic():
    wm = WarehouseManager()
    wm.add_product(Product("Phone", "Electronics", 500))
    wm.add_product(Product("TV", "Electronics", 1500))
    wm.add_product(Product("Apple", "Food", 2))

    assert wm.get_total_value() == 2002
    electronics = wm.filter_by_category("Electronics")
    assert len(electronics) == 2
    assert all(isinstance(p, Product) for p in electronics)