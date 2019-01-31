def count(string):
    chars = {}
    for symbol in string:
        if symbol in chars:
            chars[symbol] += 1
        else:
            chars[symbol] = 1
    return chars