def calculate_discount(price, discount_percent):
    discount = (discount_percent / 100) * price
    return price - discount

def test_ten_percent_discount():
    assert calculate_discount(1000,10) == 900
def test_fifty_percent_discount():
    assert calculate_discount(500,50) == 250
def test_zero_percent_discount():
    assert calculate_discount(200,0) == 200
def test_hundred_percent_discount():
    assert calculate_discount(100,100) == 0