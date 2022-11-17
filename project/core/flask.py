from flask import render_template, Blueprint

core = Blueprint('core', __name__, template_folder='templates', url_prefix='/')

# main page
@core.route("/")
def index():
    return render_template('index.html') 

@core.route("/test")
def index():
    print('{"name":"ofri", "age": 21}')
    return '{"name":"ofri", "age": 21}'