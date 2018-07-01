from itertools import accumulate

def verify(isbn):

    isbn = list(str(isbn.replace("-", "")))

    if len(isbn) != 10:
        return False

    if isbn[-1].lower() == "x":
        isbn[-1] = 10

    factors = list(range(1, 11))
    factors.reverse()

    try:
        dot_product = list(accumulate((int(a) * b for a, b in zip(isbn, factors))))[-1]
        return dot_product%11 == 0
    except:
        return False
