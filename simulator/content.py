import random

CONTENT_CATALOG = [
    ("Real Madrid vs Barcelona", 0.9),
    ("India vs Pakistan Cricket", 0.95),
    ("FIFA World Cup Final", 0.92),
    ("IPL Live Match", 0.85),
    ("Netflix Series Premiere", 0.6),
    ("Breaking News Live", 0.7)
]

def generate_content_request():
    """
    Returns content name and redundancy factor.
    """
    return random.choice(CONTENT_CATALOG)