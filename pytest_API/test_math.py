def test_addition():
    result = 2 + 3
    assert result == 5

def test_subtraction():
    result = 5 - 2
    assert result == 3

def test_string_length():
    my_string = "Hello, World!"
    assert len(my_string) == 13

def test_list_count():
    fruits = ["apple", "banana", "cherry", "date"]
    assert len(fruits) == 4

def test_that_fails_on_purpose():
    result = 2 + 2
    assert result == 4

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def test_even():
    assert is_even(4) == True

def test_odd():
    assert is_even(7) == False

def test_zero():
    assert is_even(0) == True

def test_negative_even():  
    assert is_even(-2) == True

def test_assert_equality():
    assert 10 == 10
    assert "Hello" == "Hello"
    assert [1, 2, 3] == [1, 2, 3]
    assert True == True

def test_assert_true_false():
    assert True
    assert not False
    assert 5 > 3
    assert 2 != 5

def test_assert_list():
    my_list = [1,2,3,4,5]
    assert 3 in my_list
    assert 6 not in my_list
    assert len(my_list) == 5

def test_assert_string():
    my_string = "kratik@gmail.com"
    assert "@" in my_string
    assert my_string.endswith(".com")
    assert "gmail" in my_string
    assert my_string.startswith("kratik")

def test_assert_dict():
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    assert "name" in my_dict
    assert my_dict["age"] == 30
    assert my_dict.get("city") == "New York"
    assert len(my_dict) == 3

