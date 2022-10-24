import os
import sys
import math
import machine
import us_ntp as ntp
from network import WLAN
from console_colors import bcolors as color

FILE_PATH = "/flash/log.log"
MAX_FILE_SIZE = math.pow(1024, 3)
FILE_SIZE_INDEX = 6

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

_level_dict = {
    CRITICAL: "Crit",
    ERROR: "Error",
    WARNING: "Warn",
    INFO: "Info",
    DEBUG: "Debug",
}

_stream = sys.stderr


class LogRecord:
    def __init__(self):
        self.__dict__ = {}

    def __getattr__(self, key):
        return self.__dict__[key]


class Handler:
    def __init__(self):
        pass

    def setFormatter(self, fmtr):
        pass


class Logger:

    level = NOTSET
    handlers = []
    record = LogRecord()
    log_file = None

    def __init__(self, name):
        self.name = name

        bssid = input("Write the network bssid and press enter\n")
        password = input("Write the network password and press enter\n")

        rtc_res = ntp.connect_to_google_servers(bssid, WLAN.WPA2, password)

        if not rtc_res:
            print("Failed to connect")
            machine.idle()

        self.log_file = open(FILE_PATH, "a+")

    def __del__(self):
        self.log_file.close()

    def _level_str(self, level):
        l = _level_dict.get(level)
        if l is not None:
            return l
        return "LVL%s" % level

    def setLevel(self, level):
        self.level = level

    def isEnabledFor(self, level):
        return level >= (self.level or _level)

    def log(self, print_color, level, msg, *args):
        if self.isEnabledFor(level):
            levelname = self._level_str(level)
            timestamp = ntp.ddmmyyyyHHmmss(-3)

            if args:
                msg = msg % args
            if self.handlers:

                d = self.record.__dict__
                d["color"] = color
                d["timestamp"] = timestamp
                d["levelname"] = levelname
                d["levelno"] = level
                d["message"] = msg
                d["name"] = self.name
                for h in self.handlers:
                    h.emit(self.record)
            else:
                log_msg = "[" + timestamp + "][" + self.name + "]-[" + \
                    levelname + "]-" + msg

                print(print_color + log_msg + color.RESET, sep="", file=_stream)
                
                self.shouldResetLogCursor(len(log_msg) + 1)
                self.log_file.write(log_msg + "\n")
                self.log_file.flush()

    def debug(self, msg, *args):
        self.log(color.RESET, DEBUG, msg, *args)

    def info(self, msg, *args):
        self.log(color.INFO, INFO, msg, *args)

    def warning(self, msg, *args):
        self.log(color.WARNING, WARNING, msg, *args)

    def error(self, msg, *args):
        self.log(color.ERROR, ERROR, msg, *args)

    def critical(self, msg, *args):
        self.log(color.ERROR, CRITICAL, msg, *args)

    def exc(self, e, msg, *args):
        self.log(ERROR, msg, *args)
        sys.print_exception(e, _stream)

    def exception(self, msg, *args):
        self.exc(sys.exc_info()[1], msg, *args)

    def addHandler(self, hndlr):
        self.handlers.append(hndlr)

    def shouldResetLogCursor(self, str_size):
        file_stats = os.stat(FILE_PATH)

        if file_stats[FILE_SIZE_INDEX] + str_size > MAX_FILE_SIZE:
            self.log_file.seek(0,0)

_level = INFO
_loggers = {}


def getLogger(name="root"):
    if name in _loggers:
        return _loggers[name]
    l = Logger(name)
    _loggers[name] = l
    return l


def info(msg, *args):
    getLogger().info(msg, *args)


def debug(msg, *args):
    getLogger().debug(msg, *args)


def basicConfig(level=INFO, filename=None, stream=None, format=None):
    global _level, _stream
    _level = level
    if stream:
        _stream = stream
    if filename is not None:
        print("logging.basicConfig: filename arg is not supported")
    if format is not None:
        print("logging.basicConfig: format arg is not supported")



__version__ = '0.4'
