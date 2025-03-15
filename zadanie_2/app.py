

def is_password_valid(password):
    if not isinstance(password, str):
        raise TypeError(password)

    return len(password) >= 8\
    and not ' ' in password\
    and any(not char.isalnum() for char in password)\
    and any(char.isupper() for char in password)


def rect_area(a, b):
    if not (isinstance(a, float | int) or isinstance(b, float | int)):
        raise TypeError(a,b)
    if a <= 0 or b <= 0:
        raise ValueError(a,b)
    return a * b


def is_pallindrome(t):
    if not isinstance(t, str):
        raise TypeError(t)

    t = t.lower()
    low = len(t) // 2 
    high = low + 1 if len(t) % 2 ==  1 else low
    return t[:high] == t[:low-1:-1]
    

def replace_char(text, original, substitute):
    if not (isinstance(text, str) or isinstance(original, str) or isinstance(substitute, str)):
        raise TypeError(text, original, substitute)
    if len(original) != 1 or len(substitute) != 1:
        raise ValueError(original, substitute)
    return ''.join([substitute if c == original else c for c in text])

def greet(name):
    if not isinstance(name, str):
        raise TypeError(name)
    return f'Hello, {name}'



if __name__ == "__main__":
    pass
