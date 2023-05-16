from flask import Blueprint
from flask_login import current_user, login_required
from webapp.user.decorators import admin_required


blueprint = Blueprint('admin', __name__, url_prefix='/admin')


# page for admin
# @app.route('/admin')
@blueprint.route('/')
# @login_required
@admin_required
def admin_index():
    if current_user.is_admin:
        return "Hello admin! (admin/views)'"
#     else:
#         return "You aren't admin."
# # -------------



# from flask import Blueprint
# from flask_login import current_user
# from webapp.user.decorators import admin_required


# blueprint = Blueprint('admin', __name__, url_prefix='/admin')


# # page for admin
# @blueprint.route('/')
# @admin_required
# def admin_index():
#     if current_user.is_admin:
#         return "Hello admin!"
