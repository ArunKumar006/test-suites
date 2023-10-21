import re

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
def test_sum():
    assert 10+2==12


def validate_email(email):
    # Regular expression for a simple email validation
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

# pytest test cases using regex
def test_valid_email():
    assert validate_email("user@example.com") == True

def test_invalid_email():
    assert validate_email("invalid_email") == False

def test_valid_email_with_subdomain():
    assert validate_email("user@sub.example.co.uk") == True

def validate_phone(phone):
    match=re.match(r"\+\d{12}$",phone)
    return match is not None



def test_valid_phone():
    assert validate_phone("+919544794545")

def test_invalid_phone():
    assert validate_phone("+9195447945450") == False
