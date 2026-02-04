import random
from datetime import datetime

def generate_users(t):
    """
    Dynamic users based on time of day.
    """
    hour = datetime.now().hour

    if 18 <= hour <= 23:          # evening peak
        users = random.randint(80, 140)
    elif 8 <= hour <= 17:         # daytime
        users = random.randint(40, 80)
    else:                         # late night
        users = random.randint(30, 60)

    return max(10, users)