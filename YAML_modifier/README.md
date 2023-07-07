# YAML File Updater

This script allows you to update specific fields in a YAML file by providing field-value pairs as command-line arguments.

## Prerequisites

- Python 3.x
- PyYAML library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ataha/python-snippets.git

## Usage

```bash
python script.py <file_name> <field1=value1> <field2=value2> ...


<file_name>: The path to the YAML file you want to update.
<field1=value1>, <field2=value2>, etc.: Field-value pairs specify the fields you want to update in the YAML file.
For example, to update the version and author fields in a YAML file named config.yaml, you would run:

```bash
python script.py config.yaml version=1.2.3 author="John Doe"


Make sure to enclose field values in double quotes if they contain spaces or special characters.
