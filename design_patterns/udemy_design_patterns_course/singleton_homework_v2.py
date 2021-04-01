import datetime
from rich.console import Console


#########################################################################
# Implementation of a custom Logger class using Singleton design pattern
#########################################################################

class Logger:
    """ A custom logging class using that can only have one instance.
    Logs can either be displayed on the console or saved to file."""

    _logger = None
    COLORS = {
            'WARNING': 'rgb(255,249,61)',
            'INFO': 'rgb(0,170,255)',
            'DEBUG': 'rgb(0,255,69)',
            'CRITICAL': 'rgb(255,77,61) on rgb(15,15,15)',
            'ERROR': 'rgb(255,77,61)'
    }

    def __new__(cls, *args, **kwargs):
        if not cls._logger:
            cls._logger = super().__new__(cls)
        return cls._logger

    def __init__(self, level='DEBUG', output='console'):
        self.level = level
        self.output = output

    def log_to(self, msg):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_msg = f"[{timestamp}] {self.level}: {msg}"
        if self.output == 'console':
            # To use Rich module in PyCharm you will need to enable “emulate terminal”
            # in output console option in run/debug configuration to see styled output
            console = Console()
            console.print(log_msg, style=self.COLORS[self.level.upper()], highlight=False)
        elif self.output == 'file':
            filename = datetime.datetime.now().strftime("log_%m_%d_%Y") + '.log'
            with open(filename, 'a+') as log_file:
                log_file.write(log_msg + '\n')

    def info(self, msg):
        prev_level, self.level = self.level, 'INFO'
        self.log_to(msg)
        self.level = prev_level

    def debug(self, msg):
        prev_level, self.level = self.level, 'DEBUG'
        self.log_to(msg)
        self.level = prev_level

    def warning(self, msg):
        prev_level, self.level = self.level, 'WARNING'
        self.log_to(msg)
        self.level = prev_level

    def error(self, msg):
        prev_level, self.level = self.level, 'ERROR'
        self.log_to(msg)
        self.level = prev_level

    def critical(self, msg):
        prev_level, self.level = self.level, 'CRITICAL'
        self.log_to(msg)
        self.level = prev_level

    def set_level(self, level):
        self.level = level

    def set_output(self, output):
        self.output = output

    def __call__(self, msg):
        self.log_to(msg)


if __name__ == "__main__":
    logger1 = Logger()
    logger1.error("System Error")
    logger1.info("Calculation completed")
    logger1.debug("No errors detected")
    logger1.set_level('ERROR')
    logger1('This is a Logger call')
    logger1.warning('A yellow warning!')
    logger1.critical('Just a test!')

    logger2 = Logger('INFO')

    print(f"logger1 id: {id(logger1)}, logger2 id: {id(logger2)}")
    print(f"Is logger1 the same as logger2? {logger1 is logger2}")

    print('Initial logger2 level: ', end="")
    print(logger2.level)
    logger1.set_level('ERROR')

    print('Logger2 level after setting the level on logger1 to ERROR: ', end="")
    print(logger2.level)
