from application.coding_style import check_coding_style
from application.configuration import * 
from application.data_processing import process_data
from application.json_report import generate_json_report
from application.authentication import authenticate_user
from application.command_line_interface import get_command_line_arguments


def main():
    # Get the command line arguments
    args = get_command_line_arguments()
    # Authenticate the user
    if authenticate_user(args.username, args.password):
        # Process the data
        data = process_data(args.data)
        # Generate the JSON report
        generate_json_report(data, args.output_file)
    else:
        print("Authentication failed")

if __name__ == "__main__":
    main()
