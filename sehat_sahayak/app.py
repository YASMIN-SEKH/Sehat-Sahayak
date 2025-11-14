from flask import Flask, render_template
from heart_disease import heart_bp
from diabetes import diabetes_bp
import os


def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(heart_bp, url_prefix='/heart')
    app.register_blueprint(diabetes_bp, url_prefix='/diabetes')

    @app.route('/')
    def main():
        return render_template('main.html')

    @app.route('/healthz')
    def health_check():
        return "OK", 200

    return app


# IMPORTANT: create the app for gunicorn
app = create_app()

# Only run with Flask development server when running locally
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
