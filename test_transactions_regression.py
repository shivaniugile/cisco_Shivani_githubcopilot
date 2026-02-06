import pytest

from example_new import total_per_customer


def test_skip_malformed_customer_id():
    # Regression: earlier implementations failed when customer_id was None or non-int
    orders = [
        {"order_id": 1, "customer_id": None, "amount": 10},
        {"order_id": 2, "customer_id": "not-an-int", "amount": 20},
        {"order_id": 3, "customer_id": 11, "amount": 30},
    ]
    assert total_per_customer(orders) == {11: 30.0}


def test_skip_non_numeric_amounts():
    orders = [
        {"order_id": 1, "customer_id": 2, "amount": "N/A"},
        {"order_id": 2, "customer_id": 2, "amount": 40},
    ]
    assert total_per_customer(orders) == {2: 40.0}
