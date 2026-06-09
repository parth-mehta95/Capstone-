from validators import DataValidator, OrderValidator, ProductValidator, UserValidator


def test_user_validator_accepts_valid_user():
    validator = UserValidator()

    result = validator.validate({
        "name": "Parth",
        "email": "parth@example.com",
    })

    assert result.is_valid is True
    assert result.errors == []


def test_user_validator_rejects_invalid_email():
    validator = UserValidator()

    result = validator.validate({
        "name": "Parth",
        "email": "wrong-email",
    })

    assert result.is_valid is False
    assert "email must be valid" in result.errors


def test_product_validator_rejects_negative_price():
    validator = ProductValidator()

    result = validator.validate({
        "name": "Course",
        "category": "education",
        "price": -10,
    })

    assert result.is_valid is False
    assert "price cannot be negative" in result.errors


def test_order_validator_requires_product_ids_list():
    validator = OrderValidator()

    result = validator.validate({
        "user_id": 1,
        "product_ids": "not-a-list",
        "status": "processing",
    })

    assert result.is_valid is False
    assert "product_ids must be a list" in result.errors


def test_data_validator_rejects_invalid_max_price():
    validator = DataValidator()

    result = validator.validate({
        "max_price": "abc",
    })

    assert result.is_valid is False
    assert "max_price must be a valid number" in result.errors