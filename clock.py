from datetime import datetime, time

def clock():
    time = datetime.now().strftime('%H:%M')
    return time
