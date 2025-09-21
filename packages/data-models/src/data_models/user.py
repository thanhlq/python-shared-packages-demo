"""User-related data models."""

from datetime import datetime
from typing import Optional
from dataclasses import dataclass


@dataclass
class User:
    """User model representing a system user."""

    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        """Set creation timestamp if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    @property
    def full_name(self) -> str:
        """Get the user's full name."""
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> dict:
        """Convert user to dictionary."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


@dataclass
class UserProfile:
    """Extended user profile information."""

    user_id: int
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    phone_number: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    location: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert user profile to dictionary."""
        return {
            "user_id": self.user_id,
            "bio": self.bio,
            "avatar_url": self.avatar_url,
            "phone_number": self.phone_number,
            "date_of_birth": self.date_of_birth.isoformat() if self.date_of_birth else None,
            "location": self.location,
        }
