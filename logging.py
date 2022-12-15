# Логирование

from datetime import datetime as dt


def logging_to_file(arithmetic):
    path = "log.csv"
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, "a")
    f.write(f'{time_sign}--> {arithmetic}\n')
    f.close()
