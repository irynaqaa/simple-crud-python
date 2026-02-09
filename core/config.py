PAGE_TITLE: str = "Homepage"
ADD_URL: str = "/add-siswa"  # matches existing add route
TABLE_WIDTH: str = "80%"
HEADER_BG_COLOR: str = "#DDDDDD"
COLUMN_HEADINGS: dict[str, str] = {
    "name": "Name",
    "age": "Age",
    "email": "Email",
    "action": "Action",
}

PAGE_CONSTANTS: dict[str, object] = {
    "PAGE_TITLE": PAGE_TITLE,
    "ADD_URL": ADD_URL,
    "TABLE_WIDTH": TABLE_WIDTH,
    "HEADER_BG_COLOR": HEADER_BG_COLOR,
    "COLUMN_HEADINGS": COLUMN_HEADINGS,
}

__all__ = [
    "PAGE_TITLE",
    "ADD_URL",
    "TABLE_WIDTH",
    "HEADER_BG_COLOR",
    "COLUMN_HEADINGS",
    "PAGE_CONSTANTS",
]