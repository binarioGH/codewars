#-*-coding: utf-8-*-
def max_number(n):
    return int("".join(sorted(str(n), reverse=True))) 