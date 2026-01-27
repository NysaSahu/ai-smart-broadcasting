class User:
    def __init__(self, user_id):
        self.user_id = user_id


def generate_users(num_users):
    users = []
    for i in range(num_users):
        users.append(User(i))
    return users
