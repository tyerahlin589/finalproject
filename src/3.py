import random
import time

def get_random_number(max_value):
    return random.randint(0, max_value)

def get_random_boolean():
    return random.choice([True, False])

def get_random_string(length=8):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.choice(letters) for i in range(length))

def get_random_integer(min_value, max_value):
    return random.randint(min_value, max_value)

def get_random_float(min_value, max_value):
    return random.uniform(min_value, max_value)

def get_random_date():
    return datetime.datetime.strptime(str(random.randint(1970, 2050)), '%Y-%m-%d').date()

def get_random_time():
    return datetime.datetime.strptime(str(random.randint(0, 86399)), '%H:%M:%S').time()

def get_random_datetime():
    date = get_random_date()
    time = get_random_time()
    return datetime.datetime(year=date.year, month=date.month, day=date.day, hour=time.hour, minute=time.minute, second=time.second)

def get_random_uuid():
    return uuid.UUID(int = random.randint(0, 2**128))
