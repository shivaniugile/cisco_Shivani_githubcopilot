import pytest

from example_new import total_per_customer


def test_single_order_single_customer():
    orders = [{"order_id": 1, "customer_id": 10, "amount": 100}]
    assert total_per_customer(orders) == {10: 100.0}


def test_multiple_orders_same_customer():
    orders = [
        {"order_id": 1, "customer_id": 1, "amount": 10},
        {"order_id": 2, "customer_id": 1, "amount": 20},
    ]
    assert total_per_customer(orders) == {1: 30.0}


def test_multiple_customers():
    orders = [
        {"order_id": 1, "customer_id": 1, "amount": 50},
        {"order_id": 2, "customer_id": 2, "amount": 25},
    ]
    assert total_per_customer(orders) == {1: 50.0, 2: 25.0}
