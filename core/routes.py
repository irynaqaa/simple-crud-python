from flask import Blueprint, render_template, abort, url_for, Response
from sqlalchemy.exc import SQLAlchemyError
import logging
from typing import List, Dict, Any

from core.models import Student, db
from core.config import (
    PAGE_TITLE,
    ADD_URL,
    TABLE_WIDTH,
    HEADER_BG_COLOR,
    COLUMN_HEADINGS,
)

logger = logging.getLogger(__name__)

main_bp = Blueprint("main", __name__)

PAGE_CONSTANTS: Dict[str, Any] = {
    "PAGE_TITLE": PAGE_TITLE,
    "ADD_URL": ADD_URL,
    "TABLE_WIDTH": TABLE_WIDTH,
    "HEADER_BG_COLOR": HEADER_BG_COLOR,
    "COLUMN_HEADINGS": COLUMN_HEADINGS,
}


@main_bp.route("/", methods=["GET"])
def home() -> Response:
    try:
        contact_list: List[Student] = (
            db.session.query(Student).order_by(Student.id.desc()).all()
        )
    except (SQLAlchemyError, Exception) as e:
        logger.exception("Error retrieving student data: %s", e)
        # Render a minimal error page with a 500 status code
        return (
            render_template(
                "error.html",
                message="Unable to connect to the database. Data cannot be retrieved.",
            ),
            500,
        )
    return render_template("home.html", contact_list=contact_list, **PAGE_CONSTANTS)