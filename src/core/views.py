from flask import Blueprint
from flask import Blueprint, render_template
from flask_login import login_user, current_user, logout_user, login_required
from src.accounts.models import User


core_bp = Blueprint("core", __name__)


@core_bp.route("/")
@login_required
def home():
    print("homeeeeee")
    print(current_user)
    return render_template("core/index.html")

