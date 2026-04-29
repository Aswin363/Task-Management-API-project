from app import create_app

# Create Flask app using factory
app = create_app()

# Run server
if __name__ == "__main__":
    with app.app_context():
        from app.models import db
        db.create_all()   # Create tables if not exist

    app.run(host="0.0.0.0", port=5000, debug=False)