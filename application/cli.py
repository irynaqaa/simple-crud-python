import argparse
from main import process_data, generate_report


def setup_cli():
    """Set up command-line interface for the application."""
    parser = argparse.ArgumentParser(description='Data Processing CLI')
    parser.add_argument('input_file', type=str, help='Input data file')
    parser.add_argument('--output_format', type=str, choices=['csv', 'json'], default='csv', help='Output format')
    return parser


def main():
    parser = setup_cli()
    args = parser.parse_args()
    data = process_data(args.input_file)
    generate_report(data, args.output_format)


if __name__ == '__main__':
    main()
