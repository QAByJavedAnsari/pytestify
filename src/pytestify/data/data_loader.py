import yaml

def load_config(file_path='src/pytestify/config/config.yaml'):
    """
    Load configuration parameters from a YAML file.
    """
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def load_schema(file_path='src/pytestify/config/schema_config.yaml'):
    """
    Load schema parameters from a YAML file.
    """
    with open(file_path, 'r') as file:
        schema = yaml.safe_load(file)
    return schema


def load_data(file_path):
    """Load test data from a file."""
    with open(file_path, 'r') as file:
        data = file.read()
    return data

