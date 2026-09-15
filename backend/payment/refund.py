"""Payment refund module."""

def process_refund(payment_id: str, amount: float) -> dict:
    return {
        "payment_id": payment_id,
        "amount": amount,
        "status": "refund_requested"
    }
