from backend.models import Product
from sqlalchemy.orm import Session

# Minimum stock threshold before triggering a refill suggestion
MIN_STOCK_THRESHOLD = 5


def check_refill_needed(product: Product) -> str | None:
    """
    Check if a specific product needs restocking based on a global threshold.

    Returns a suggestion string if stock is below the minimum threshold.
    """
    if product.stock is not None and product.stock <= MIN_STOCK_THRESHOLD:
        return f"📦 Stock for '{product.name}' is running low. Please restock."
    return None


def check_stock_levels(db: Session, user_id: int) -> list[str]:
    """
    Check stock levels for all products owned by a specific user.

    Returns a list of restocking suggestions.
    """
    products = db.query(Product).filter(Product.user_id == user_id).all()
    suggestions = []

    for product in products:
        if product.stock is not None and product.stock <= MIN_STOCK_THRESHOLD:
            suggestions.append(
                f"🔔 '{product.name}' has only {product.stock} left. Consider restocking."
            )

    return suggestions
