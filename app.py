
import os
import math
import logging

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from dotenv import load_dotenv
from database import db
from models import User


# Load environment variables
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Application configuration
secret_key = os.getenv("SECRET_KEY")

if not secret_key:
    raise RuntimeError("SECRET_KEY is missing from environment variables.")

app.config["SECRET_KEY"] = secret_key
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Allowed expense categories
ALLOWED_CATEGORIES = {
    "utilities",
    "entertainment",
    "school_fees",
    "shopping",
    "healthcare"
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


@app.route("/submit", methods=["POST"])
def submit_survey():

    try:
        # Collect participant information
        age = request.form.get("age", "").strip()
        gender = request.form.get("gender", "").strip()
        total_income = request.form.get("total_income", "").strip()

        # Validate required fields
        if not age or not gender or not total_income:
            flash("Please complete all required fields.", "error")
            return redirect(url_for("home"))

        age = int(age)
        total_income = float(total_income)

        # Validate age and income
        if age < 1 or age > 120:
            flash("Please enter a valid age.", "error")
            return redirect(url_for("home"))

        if not math.isfinite(total_income) or total_income < 0:
            flash("Please enter a valid income amount.", "error")
            return redirect(url_for("home"))

        # Collect selected expense categories
        selected_categories = request.form.getlist(
            "expense_categories"
        )

        if not selected_categories:
            flash("Please select at least one expense category.", "error")
            return redirect(url_for("home"))

        # Validate expense categories
        if not set(selected_categories).issubset(ALLOWED_CATEGORIES):
            flash("Invalid expense category selected.", "error")
            return redirect(url_for("home"))

        expenses = {}

        # Process each selected expense
        for category in selected_categories:

            amount = request.form.get(category, "").strip()

            if not amount:
                flash(
                    f"Please enter an amount for {category}.",
                    "error"
                )
                return redirect(url_for("home"))

            amount = float(amount)

            if not math.isfinite(amount) or amount < 0:
                flash(
                    "Expense amounts must be valid non-negative numbers.",
                    "error"
                )
                return redirect(url_for("home"))

            expenses[category] = amount

        # Create User object
        participant = User(
            age=age,
            gender=gender,
            total_income=total_income,
            expenses=expenses
        )

        # Save survey information to MongoDB
        db.users.insert_one(participant.to_dict())

        flash("Survey submitted successfully!", "success")

    except ValueError:
        flash("Please enter valid numeric values.", "error")

    except Exception:
        logger.exception("Survey submission failed.")
        flash(
            "Unable to save your survey. Please try again later.",
            "error"
        )

    return redirect(url_for("home"))


if __name__ == "__main__":
    # Local development only
    app.run(debug=False)
