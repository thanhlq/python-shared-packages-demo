"""Product-related data models."""

from datetime import datetime
from typing import Optional, List
from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class Category:
    """Product category model."""

    id: int
    name: str
    description: Optional[str] = None
    parent_id: Optional[int] = None
    is_active: bool = True
    created_at: Optional[datetime] = None

    def __post_init__(self):
        """Set creation timestamp if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

    def to_dict(self) -> dict:
        """Convert category to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "parent_id": self.parent_id,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


@dataclass
class Product:
    """Product model representing a sellable item."""

    id: int
    name: str
    description: str
    price: Decimal
    sku: str
    category_id: int
    stock_quantity: int = 0
    is_active: bool = True
    images: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    weight: Optional[float] = None
    dimensions: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        """Set timestamps if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()

    @property
    def is_in_stock(self) -> bool:
        """Check if product is in stock."""
        return self.stock_quantity > 0

    @property
    def formatted_price(self) -> str:
        """Get formatted price string."""
        return f"${self.price:.2f}"

    def to_dict(self) -> dict:
        """Convert product to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": float(self.price),
            "formatted_price": self.formatted_price,
            "sku": self.sku,
            "category_id": self.category_id,
            "stock_quantity": self.stock_quantity,
            "is_active": self.is_active,
            "is_in_stock": self.is_in_stock,
            "images": self.images,
            "tags": self.tags,
            "weight": self.weight,
            "dimensions": self.dimensions,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
