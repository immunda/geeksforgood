# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config.from_object('g4g.settings.Config')

# Register blueprints
from g4g.views import main
app.register_blueprint(main)


@app.route("/health-check", methods=['GET'])
def health_check():
    return 'OK'
