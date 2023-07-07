import sys
import yaml


def update_yaml_file(file_path, field_updates):
    # Load the YAML file
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Update the specified fields
    for field, value in field_updates.items():
        nested_fields = field.split('.')
        nested_data = yaml_data
        for nested_field in nested_fields[:-1]:
            if isinstance(nested_data, list):
                index = int(nested_field)
                nested_data = nested_data[index]
            else:
                nested_data = nested_data.get(nested_field, {})
        last_field = nested_fields[-1]
        if isinstance(nested_data, list) and last_field.isdigit():
            index = int(last_field)
            nested_data[index] = value
        else:
            nested_data[last_field] = value

    # Save the updated YAML file
    with open(file_path, 'w') as file:
        yaml.safe_dump(yaml_data, file)


if __name__ == '__main__':
    # Parse command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_name> <field1=value1> <field2=value2> ...")
        sys.exit(1)

    file_name = sys.argv[1]
    field_updates = {}

    # Parse field=value arguments
    for arg in sys.argv[2:]:
        field, value = arg.split('=')
        field_updates[field] = value

    # Update the YAML file
    update_yaml_file(file_name, field_updates)

    print("YAML file updated successfully.")
