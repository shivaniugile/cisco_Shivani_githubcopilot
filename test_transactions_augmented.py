import pytest

from example_new import total_per_customer


def test_missing_amount_treated_as_zero():
    orders = [{"order_id": 1, "customer_id": 5}]
    assert total_per_customer(orders) == {5: 0.0}


def test_string_amounts_and_ids_are_coerced():
    orders = [
        {"order_id": 1, "customer_id": "7", "amount": "10"},
        {"order_id": 2, "customer_id": "7", "amount": "5.5"},
    ]
    result = total_per_customer(orders)
    assert result == {7: pytest.approx(15.5)}


def test_negative_amounts_allowed_and_aggregated():
    orders = [
        {"order_id": 1, "customer_id": 9, "amount": -20},
        {"order_id": 2, "customer_id": 9, "amount": 50},
    ]
    assert total_per_customer(orders) == {9: 30.0}
