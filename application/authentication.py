import authlib

# Define a user database
users = {
    "john": "hello",
    "mary": "world"
}

# Define an authentication function
def authenticate(username, password):
    if username in users and users[username] == password:
        return True
    return False

# Use the authentication function
if authenticate("john", "hello"):
    print("Authentication successful")
else:
    print("Authentication failed")