from functools import wraps

from flask import Markup, flash, url_for, redirect
from flask_login import current_user

def confirm_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            message=Markup(
                    'Please confirmed your account first.'
                    'Not receive the email.'
                    )
            flash(message, 'warning')
            return redirect(url_for('blog.index'))
        return func(*args, **kwargs)
    return decorated_function
