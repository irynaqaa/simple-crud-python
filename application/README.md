# Data Processing Application

## Overview
This application processes input data files and generates reports in CSV and JSON formats.

## Requirements
- Python 3.x
- Required packages can be installed using:
```sh
pip install -r requirements.txt
```

## Usage
To run the application, use the command line interface:
```sh
python cli.py <input_file> [--output_format csv|json]
```

## Running Tests
To run the tests, use:
```sh
python -m unittest tests.py
```

## Linting
To check code quality, run:
```sh
bash tmp_code.sh
```