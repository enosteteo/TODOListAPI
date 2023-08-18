from flask import Flask, url_for

from auth import auth_blueprint
from tasks import tasks_blueprint
from users.router import users_blueprint

app = Flask(__name__)
app.register_blueprint(tasks_blueprint, url_prefix='/tasks')
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(users_blueprint, url_prefix='/users')

@app.route("/")
def hello_world():
    return f"<h1>Hello, World!</h1>\n <p>System routes can be viewed at <a href=http://localhost:8000{url_for('site_map')}>http://localhost:8000{url_for('site_map')}</a></p>"

# temporary. util to list all routes
def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

# site-map
@app.route("/site_map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    links_normalized = []
    for link in links:
        links_normalized.append(f"<a href=http://localhost:8000{link[0]}>{link[1]}</a>")
        if "site_map" in link[1]:
            links_normalized[-1] = f"<a href=http://localhost:8000{link[0]}>{link[1]} <- you are here</a>"
    links_normalized = "<br>".join(links_normalized)
    return f"<h1>Site Map</h1>\n<p>{links_normalized}</p>", 200
