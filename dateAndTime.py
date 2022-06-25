from datetime import datetime, time

def hour():
    actual_time = datetime.now().strftime('%H:%M')
    return actual_time


def data():
    data_actual = datetime.today().strftime('%d/%m/%Y')
    return data_actual