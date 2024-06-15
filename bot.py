from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from ReconBot.auth import login_required
from ReconBot.db import get_db

bp = Blueprint('bot', __name__)

@bp.route('/')
@login_required
def index():
    db = get_db()
    # posts = db.execute(
    #     'SELECT p.id, title, body, created, author_id, username'
    #     ' FROM post p JOIN user u ON p.author_id = u.id'
    #     ' ORDER BY created DESC'
    # ).fetchall()

    sidebar_items = [
        {"label": "Dashboard", "url": "/", "active": True, "icon": "fa-gauge"},
        {"label": "Add Target", "url": "/add-target", "active": False, "icon": "fa-gauge"},
        {"label": "Remove Target", "url": "/remove-target", "active": False, "icon": "fa-gauge"},
        {"label": "Settings", "url": "/settings", "active": False, "icon": "fa-gauge"}
    ]

    flash("This is a test alert! You can dismiss me")
    return render_template('base.html', page_title='Dashboard', sidebar_items=sidebar_items)