import logging


""" Folosind Singleton pattern, să se implementeze o clasă Logger, care are o metodă log()
care primește un mesaj și face print cu timestamp curent + mesaj.
Exemplu orientativ de output:
log(“eroare în sistem”) -> va afișa la terminal “[10:24:33] eroare in sistem”.
Formatul exact de timestamp poate fi ales după preferință
(hint: se poate adaugă și data calendaristică dacă se dorește).
"""


###################################################################
# Implementation of a Logger class using a Singleton metaclass
# and the built-in logging module
###################################################################


class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Logger(metaclass=Singleton):
    _logger = None

    def __init__(self):
        self._logger = logging.getLogger()
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("[%(asctime)s] %(message)s", "%H:%M:%S")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

    def get_logger(self):
        return self._logger


if __name__ == "__main__":
    logger1 = Logger().get_logger()
    logger1.debug("Eroare in sistem")

    logger2 = Logger().get_logger()

    print(f"logger1 id: {id(logger1)}, logger2 id: {id(logger2)}")
    print(f"Is logger1 the same as logger2? {logger1 is logger2}")

    print("Initial logger2 level: ", end="")
    print(logging.getLevelName(logger2.level))
    logger1.setLevel(logging.ERROR)

    print("Logger2 level after setting the level on logger1 to ERROR: ", end="")
    print(logging.getLevelName(logger2.level))
