"""Order-related data models."""

from datetime import datetime
from typing import Optional, List
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum


class OrderStatus(Enum):
    """Enum for order status."""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


@dataclass
class OrderItem:
    """Individual item within an order."""

    id: int
    product_id: int
    product_name: str
    product_sku: str
    quantity: int
    unit_price: Decimal

    @property
    def total_price(self) -> Decimal:
        """Calculate total price for this item."""
        return self.unit_price * self.quantity

    @property
    def formatted_unit_price(self) -> str:
        """Get formatted unit price string."""
        return f"${self.unit_price:.2f}"

    @property
    def formatted_total_price(self) -> str:
        """Get formatted total price string."""
        return f"${self.total_price:.2f}"

    def to_dict(self) -> dict:
        """Convert order item to dictionary."""
        return {
            "id": self.id,
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_sku": self.product_sku,
            "quantity": self.quantity,
            "unit_price": float(self.unit_price),
            "total_price": float(self.total_price),
            "formatted_unit_price": self.formatted_unit_price,
            "formatted_total_price": self.formatted_total_price,
        }


@dataclass
class Order:
    """Order model representing a customer purchase."""

    id: int
    user_id: int
    status: OrderStatus
    items: List[OrderItem] = field(default_factory=list)
    shipping_address: Optional[str] = None
    billing_address: Optional[str] = None
    order_date: Optional[datetime] = None
    shipped_date: Optional[datetime] = None
    delivered_date: Optional[datetime] = None
    notes: Optional[str] = None

    def __post_init__(self):
        """Set order date if not provided."""
        if self.order_date is None:
            self.order_date = datetime.now()

    @property
    def total_amount(self) -> Decimal:
        """Calculate total order amount."""
        return sum(item.total_price for item in self.items)

    @property
    def total_items(self) -> int:
        """Get total number of items in order."""
        return sum(item.quantity for item in self.items)

    @property
    def formatted_total_amount(self) -> str:
        """Get formatted total amount string."""
        return f"${self.total_amount:.2f}"

    def add_item(self, item: OrderItem) -> None:
        """Add an item to the order."""
        self.items.append(item)

    def remove_item(self, item_id: int) -> bool:
        """Remove an item from the order by ID."""
        for i, item in enumerate(self.items):
            if item.id == item_id:
                del self.items[i]
                return True
        return False

    def to_dict(self) -> dict:
        """Convert order to dictionary."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "status": self.status.value,
            "total_amount": float(self.total_amount),
            "formatted_total_amount": self.formatted_total_amount,
            "total_items": self.total_items,
            "items": [item.to_dict() for item in self.items],
            "shipping_address": self.shipping_address,
            "billing_address": self.billing_address,
            "order_date": self.order_date.isoformat() if self.order_date else None,
            "shipped_date": self.shipped_date.isoformat() if self.shipped_date else None,
            "delivered_date": self.delivered_date.isoformat() if self.delivered_date else None,
            "notes": self.notes,
        }
