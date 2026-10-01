import datetime
import time

from Utils import colors


class Logger:
    def __init__(self, log_level: int) -> None:
        self.file = "./logs/" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))[:-3] + ".log"
        with open(file=self.file, mode="a", encoding='utf-8') as file:
            file.write("Program start\n")
        self.log_level = log_level

    def log(self, time, type, message):
        color = colors.bcolors.GREY
        prefix: str = "INFO"

        if type.lower() == 'warn':
            color = colors.bcolors.WARNING
            prefix = "WARNING"
        elif type.lower() == 'debug':
            color = colors.bcolors.OKGREEN
            prefix = "DEBUG"
        elif type.lower() == 'critical':
            color = colors.bcolors.FAIL
            prefix = "CRITICAL"

        self.general_log(color, time, prefix, message)


    def general_log(self, color, time, prefix, message):
        print(color + "" + time, "[" + prefix + "]", message, colors.bcolors.RESET)
        with open(file=self.file, mode="a", encoding='utf-8') as file:
            file.write(time + " " + "[" + prefix + "] " + message + "\n")


    def info(self, message, time = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(time.time()))):
        self.log(time, "info", message)

    def warn(self, message, time = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(time.time()))):
        self.log(time, "warn", message)

    def debug(self, message, time = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(time.time()))):
        self.log(time, "debug", message)

    def critical(self, message, time = time.strftime("%d/%m/%y %H:%M:%S", time.localtime(time.time()))):
        self.log(time, "critical", message)