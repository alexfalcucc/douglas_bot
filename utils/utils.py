import datetime
import ast


class Temperature(object):
    """
    Temperature converter:
    how to use:
    >>> Celsius = [39.2, 36.5, 37.3, 37.8]
    >>> Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
    >>> print Fahrenheit
    [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
    >>> C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
    >>> print C
    [39.200000000000003, 36.5, 37.300000000000004, 37.799999999999997]
    >>>
    """
    def __init__(self, T):
        self.t = T

    def fahrenheit_to_celsius(self):
        return map(lambda x: (float(9)/5)*x + 32, self.t)

    def celsius_to_fahrenheit(self):
        return map(lambda x: (float(5)/9)*(x-32), self.fahrenheit_to_celsius())


def utf8_encode(string):
    return string.encode('utf-8')


def verify_text(names, text):
    return [name for name in names if name in text]


def equals_text(names, text):
    return [name for name in names if name == text]


def remove_bot_name(names, text):
    for name in names:
        if name in text:
            text = text.replace(name, '')
    return text


def get_UNIX_datetime(UNIX_ID):
    return (
        datetime.datetime.fromtimestamp(
            int(UNIX_ID)
        ).strftime('%Y-%m-%d %H:%M:%S')
    )


def convert_str_to_dict(string):
    return ast.literal_eval(string)
