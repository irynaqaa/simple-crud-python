import pycodestyle

def check_coding_style(file_path):
    # Create a StyleGuide object
    style_guide = pycodestyle.StyleGuide(
        max_line_length=120,
        hang_closing=False,
    )
    # Check the coding style of the file
    result = style_guide.check_files([file_path])
    # Print the result
    print(f"Coding style check result: {result.total_errors}" )

# Check the coding style of the current file
check_coding_style(__file__)
