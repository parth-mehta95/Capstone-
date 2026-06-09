import re


class ValidationResult:
    """
    Stores validation result data.
    """

    def __init__(self, is_valid=True, errors=None):
        self.is_valid = is_valid
        self.errors = errors or []

    def to_dict(self):
        return {
            "is_valid": self.is_valid,
            "errors": self.errors,
        }


class ValidationService:
    """
    Base validation service class.
    Child validators override the validate method.
    """

    def validate(self, data):
        raise NotImplementedError("Child validator must implement validate method")

    def required(self, data, field_name):
        if field_name not in data or data[field_name] in [None, ""]:
            return f"{field_name} is required"
        return None


class UserValidator(ValidationService):
    """
    Validates user request data.
    """

    def validate(self, data):
        errors = []

        for field in ["name", "email"]:
            error = self.required(data, field)
            if error:
                errors.append(error)

        email = data.get("email", "")
        if email and not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            errors.append("email must be valid")

        return ValidationResult(len(errors) == 0, errors)


class ProductValidator(ValidationService):
    """
    Validates product request data.
    """

    def validate(self, data):
        errors = []

        for field in ["name", "category", "price"]:
            error = self.required(data, field)
            if error:
                errors.append(error)

        price = data.get("price")
        if price is not None and not isinstance(price, (int, float)):
            errors.append("price must be a number")

        if isinstance(price, (int, float)) and price < 0:
            errors.append("price cannot be negative")

        return ValidationResult(len(errors) == 0, errors)


class OrderValidator(ValidationService):
    """
    Validates order request data.
    """

    def validate(self, data):
        errors = []

        for field in ["user_id", "product_ids", "status"]:
            error = self.required(data, field)
            if error:
                errors.append(error)

        if "product_ids" in data and not isinstance(data["product_ids"], list):
            errors.append("product_ids must be a list")

        return ValidationResult(len(errors) == 0, errors)


class DataValidator(ValidationService):
    """
    Generic validator for query/filter data.
    """

    def validate(self, data):
        errors = []

        max_price = data.get("max_price")

        if max_price is not None:
            try:
                float(max_price)
            except ValueError:
                errors.append("max_price must be a valid number")

        return ValidationResult(len(errors) == 0, errors)