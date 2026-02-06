import pytest

from example_new import total_per_customer


def test_high_volume_like_scenario():
    # Simulate many small orders across a few customers
    orders = []
    for cid in range(1, 4):
        for i in range(100):
            orders.append({"order_id": cid * 1000 + i, "customer_id": cid, "amount": 1})

    result = total_per_customer(orders)
    assert result == {1: 100.0, 2: 100.0, 3: 100.0}


def test_mixed_real_world_scenario():
    # Mixed valid, missing, and dirty data resembling real ingestion
    orders = [
        {"order_id": 1, "customer_id": 100, "amount": 120},
        {"order_id": 2, "customer_id": 101, "amount": "30"},
        {"order_id": 3, "customer_id": 100, "amount": None},
        {"order_id": 4, "customer_id": "101", "amount": "20.5"},
        {"order_id": 5, "customer_id": None, "amount": 500},
        {"order_id": 6, "customer_id": 100, "amount": -10},
    ]

    result = total_per_customer(orders)
    # 100 -> 120 + 0 + (-10) = 110
    # 101 -> 30 + 20.5 = 50.5
    assert result[100] == pytest.approx(110.0)
    assert result[101] == pytest.approx(50.5)
