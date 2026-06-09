class BaseModel:
    """
    Base model class with shared ID and serialization behavior.
    """

    def __init__(self, model_id):
        self._id = model_id

    @property
    def id(self):
        """Returns model ID."""
        return self._id

    def to_dict(self):
        """Converts base model data to dictionary."""
        return {
            "id": self._id
        }


class User(BaseModel):
    """
    User model using inheritance from BaseModel.
    """

    def __init__(self, model_id, name, email, active=True):
        super().__init__(model_id)
        self._name = name
        self._email = email
        self._active = active

    @property
    def email(self):
        """Returns user email."""
        return self._email

    @property
    def active(self):
        """Returns user active status."""
        return self._active

    def to_dict(self):
        """Converts user object to dictionary."""
        data = super().to_dict()
        data.update({
            "name": self._name,
            "email": self._email,
            "active": self._active
        })
        return data


class Product(BaseModel):
    """
    Product model using inheritance from BaseModel.
    """

    def __init__(self, model_id, name, category, price, in_stock=True):
        super().__init__(model_id)
        self._name = name
        self._category = category
        self._price = price
        self._in_stock = in_stock

    @property
    def category(self):
        """Returns product category."""
        return self._category

    @property
    def price(self):
        """Returns product price."""
        return self._price

    def to_dict(self):
        """Converts product object to dictionary."""
        data = super().to_dict()
        data.update({
            "name": self._name,
            "category": self._category,
            "price": self._price,
            "in_stock": self._in_stock
        })
        return data


class Order(BaseModel):
    """
    Order model using inheritance from BaseModel.
    """

    def __init__(self, model_id, user_id, product_ids, status):
        super().__init__(model_id)
        self._user_id = user_id
        self._product_ids = product_ids
        self._status = status

    @property
    def user_id(self):
        """Returns order user ID."""
        return self._user_id

    def to_dict(self):
        """Converts order object to dictionary."""
        data = super().to_dict()
        data.update({
            "user_id": self._user_id,
            "product_ids": self._product_ids,
            "status": self._status
        })
        return data


class ApiResponse:
    """
    Standard API response model.
    """

    def __init__(self, success, message, data=None):
        self.success = success
        self.message = message
        self.data = data

    def to_dict(self):
        """Converts API response to dictionary."""
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data
        }