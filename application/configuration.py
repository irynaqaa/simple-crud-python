import configparser

# Define a function to read the configuration

def read_config(filename):
    try:
        # Read the configuration from the config file
        config = configparser.ConfigParser()
        config.read(filename)
        return config
    except Exception as e:
        print(f"Error reading configuration: {e}")
        return None
