class BaseService:
    """
    Base service class with reusable data access methods.
    """

    def __init__(self, items=None):
        self._items = items or []

    def get_all(self):
        """Returns all items as dictionaries."""
        return [item.to_dict() for item in self._items]

    def get_by_id(self, item_id):
        """Finds an item by ID."""
        for item in self._items:
            if item.id == item_id:
                return item.to_dict()
        return None

    def add_item(self, item):
        """Adds a new item to the service."""
        self._items.append(item)
        return item.to_dict()


class UserService(BaseService):
    """
    Service class for user-related business logic.
    """

    def get_active_users(self):
        """Returns only active users."""
        return [
            user.to_dict()
            for user in self._items
            if user.active
        ]

    def get_user_emails(self):
        """Returns email addresses of active users."""
        return [
            {
                "id": user.id,
                "email": user.email
            }
            for user in self._items
            if user.active
        ]


class ProductService(BaseService):
    """
    Service class for product-related business logic.
    """

    def filter_by_category(self, category):
        """Filters products by category."""
        return [
            product.to_dict()
            for product in self._items
            if product.category.lower() == category.lower()
        ]

    def filter_by_price(self, max_price):
        """Filters products by maximum price."""
        return [
            product.to_dict()
            for product in self._items
            if product.price <= max_price
        ]

    def get_product_summary(self):
        """Returns simplified product data."""
        return [
            {
                "id": product.id,
                "name": product.to_dict()["name"],
                "price": product.price
            }
            for product in self._items
        ]


class OrderService(BaseService):
    """
    Service class for order-related business logic.
    """

    def get_orders_by_user(self, user_id):
        """Returns orders for a specific user."""
        return [
            order.to_dict()
            for order in self._items
            if order.user_id == user_id
        ]