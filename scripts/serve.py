import os
import yaml

# Specify the path to your YAML configuration file
CONFIG_FILE=os.path.join(os.getcwd(), 'env.yml')

try:
# Read the YAML configuration
    with open(CONFIG_FILE, "r") as yaml_file:
        config_data = yaml.safe_load(yaml_file)

    current_key=""
    # Set environment variables based on the configuration data
    for key, value in config_data.items():
        current_key=key

        os.environ[key] = str(value)
except FileNotFoundError:
    print("The configuration file was not found. Please make sure config.yml file exists in the root directory")
    exit(1)
except KeyError:
    print(f"The configuration file is missing {current_key}")
    exit(1)

# Run the mkdocs serve command
os.system('mkdocs serve')

