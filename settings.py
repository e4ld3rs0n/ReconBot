from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from ReconBot.auth import login_required
from ReconBot.db import get_db

bp = Blueprint('settings', __name__)

@bp.route('/user-settings')
@login_required
def userconfig():
    sidebar_items = [
        {"label": "User settings", "url": url_for('settings.userconfig'), "active": True, "icon": "fa-user"},
        {"label": "App settings", "url": url_for('settings.appconfig'), "active": False, "icon": "fa-gear"}
    ]

    return render_template('user-settings.html', page_title='User settings', sidebar_items=sidebar_items)

@bp.route('/app-settings')
@login_required
def appconfig():
    sidebar_items = [
        {"label": "User settings", "url": url_for('settings.userconfig'), "active": False, "icon": "fa-user"},
        {"label": "App settings", "url": url_for('settings.appconfig'), "active": True, "icon": "fa-gear"}
    ]

    return render_template('app-settings.html', page_title='Application settings', sidebar_items=sidebar_items)