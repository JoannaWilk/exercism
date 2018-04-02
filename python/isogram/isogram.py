def is_isogram(string):
    text = string.replace("-", "").replace(" ", "").lower()
    return len(text) == len(set(text))
