import configparser
import os

# Create a ConfigParser object
config = configparser.ConfigParser()

# Define the configuration requirements
config['DEFAULT'] = {'debug': 'True'}
config['DATABASE'] = {'host': 'localhost', 'database': 'mydatabase', 'user': 'myuser', 'password': 'mypassword'}
config['ENVIRONMENT'] = {'environment': 'development'}

# Write the configuration to a file
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Load the configuration from the file
config.read('config.ini')

# Access the configuration values
debug = config['DEFAULT']['debug']
host = config['DATABASE']['host']
database = config['DATABASE']['database']
user = config['DATABASE']['user']
password = config['DATABASE']['password']
environment = config['ENVIRONMENT']['environment']

# Print the configuration values
print(f'Debug: {debug}')
print(f'Host: {host}')
print(f'Database: {database}')
print(f'User: {user}')
print(f'Password: {password}')
print(f'Environment: {environment}')