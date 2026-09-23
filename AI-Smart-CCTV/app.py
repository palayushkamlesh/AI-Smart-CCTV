from flask import Flask
import config
from database.models import db
from routes.dashboard import dashboard
from routes.remote import remote

app = Flask(__name__)

# -----------------------------
# Configuration
# -----------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# -----------------------------
# Initialize Database
# -----------------------------
db.init_app(app)

with app.app_context():
    db.create_all()

# -----------------------------
# Register Routes
# -----------------------------
app.register_blueprint(dashboard)
app.register_blueprint(remote)

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )