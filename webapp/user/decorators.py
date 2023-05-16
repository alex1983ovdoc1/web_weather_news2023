from functools import wraps

from flask import current_app, flash, request, redirect, url_for
from flask_login import config, current_user




def admin_required(func):
	@wraps(func)
	def decorated_view(*args, **kwargs):
		if request.method in config.EXEMPT_METHODS:
			return func(*args, **kwargs)
		elif current_app.config.get('LOGIN_DISABLED'):
			return func(*args, **kwargs)
		elif not current_user.is_authenticated:
			return current_app.login_manager.unauthorized()
		elif not current_user.is_admin:
			flash('This page is only for ADMIN (decorators)')
			return redirect(url_for('news.index'))
		return func(*args, **kwargs)
	return decorated_view



# def admin_required(func):
#     @wraps(func)
#     def decorated_view(*args, **kwargs):
#         if request.method in config.EXEMPT_METHODS or current_app.config.get("LOGIN_DISABLED"):
#             pass
#         elif not current_user.is_authenticated:
#             return current_app.login_manager.unauthorized()

#         # flask 1.x compatibility
#         # current_app.ensure_sync is only available in Flask >= 2.0
#         if callable(getattr(current_app, "ensure_sync", None)):
#             return current_app.ensure_sync(func)(*args, **kwargs)
#         return func(*args, **kwargs)

#     return decorated_view
