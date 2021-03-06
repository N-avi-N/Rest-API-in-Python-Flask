from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and user.password == password:
        return user

# This comes from Flash-JWT
def identify(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)