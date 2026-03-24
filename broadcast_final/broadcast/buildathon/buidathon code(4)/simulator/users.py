import random
from datetime import datetime

def generate_users(t):
    """
    Generate users and their distances for a cell.
    Users are distributed based on time of day.
    Distance is uniform between 0.1km and 2.0km (realistic cell range).

    Args:
        t (int): Simulation timestep

    Returns:
        tuple: (users, distance_km)
    """
    hour = datetime.now().hour
    if 18 <= hour <= 23:
        users = random.randint(80, 140)
    elif 8 <= hour <= 17:
        users = random.randint(40, 80)
    else:
        users = random.randint(30, 60)
    users = max(10, users)
    distance_km = round(random.uniform(0.1, 2.0), 3)
    return users, distance_km