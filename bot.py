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
        {"label": "Dashboard", "url": url_for('bot.index'), "active": True, "icon": "fa-gauge"},
        {"label": "Scan target", "url": url_for('bot.scan_target'), "active": False, "icon": "fa-magnifying-glass"}
    ]

    return render_template('dashboard.html', page_title='Dashboard', sidebar_items=sidebar_items)

@bp.route('/scan')
@login_required
def scan_target():
    sidebar_items = [
        {"label": "Dashboard", "url": url_for('bot.index'), "active": False, "icon": "fa-gauge"},
        {"label": "Scan target", "url": url_for('bot.scan_target'), "active": True, "icon": "fa-magnifying-glass"}
    ]

    return render_template('scan-target.html', page_title='Scan target', sidebar_items=sidebar_items)