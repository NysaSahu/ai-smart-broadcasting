import random

def apply_perturbations(users, popularity, sinr_linear):
    events = {
        "flash_crowd": False,
        "mobility_loss": False,
        "channel_fading": False
    }

    if random.random() < 0.15:
        users += random.randint(10, 25)
        popularity = min(1.0, popularity + 0.15)
        events["flash_crowd"] = True

    if random.random() < 0.10:
        users = max(0, users - random.randint(5, 15))
        events["mobility_loss"] = True

    sinr_linear *= random.uniform(0.7, 1.0)
    events["channel_fading"] = True

    return users, popularity, sinr_linear, events