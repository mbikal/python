def apply_discount(price, discount):
    is_price_int_float = isinstance(price, (int, float))
    is_discount_int_float = isinstance(discount, (int, float))

    if not is_price_int_float:
        return "The price should be a number"

    if not is_discount_int_float:
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    return final_price
