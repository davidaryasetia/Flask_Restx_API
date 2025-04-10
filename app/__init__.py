# Initializing Application with init.py 
from flask import Flask, redirect
from flask_restx import Api 


def create_app(): 
    app = Flask(__name__)

    # Prefix Routing API 
    api_prefix = "/api/lombok"
    api = Api(
        app, 
        title="Service API For Lombok Gastronomic", 
        description="This is service API for Lombok Gastronomic APP", 
        version="1.0", 
        prefix=api_prefix, 
        doc=api_prefix
    )

    app.route('/')
    def redirecting_home(): 
        return redirect(api_prefix)

    return app
