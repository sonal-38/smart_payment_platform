"""Order service."""

def create_order(order_id: str, amount: float) -> dict:
    return {
        "order_id": order_id,
        "amount": amount,
        "status": "created"
    }
