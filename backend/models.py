from dataclasses import asdict, dataclass


@dataclass
class UserProfile:
    """
    Represents a sample user profile for the React Native app.
    """

    id: int
    name: str
    email: str
    role: str = "user"

    def to_dict(self):
        return asdict(self)


@dataclass
class TaskItem:
    """
    Represents a sample task item.
    """

    id: int
    title: str
    completed: bool = False

    def to_dict(self):
        return asdict(self)


@dataclass
class ApiResponse:
    """
    Standard API response structure.
    """

    success: bool
    message: str
    data: object = None

    def to_dict(self):
        return asdict(self)