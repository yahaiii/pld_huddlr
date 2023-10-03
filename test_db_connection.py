from flask import Flask, jsonify
from app.models.user_model import User
from app import db  # Import your SQLAlchemy db instance

app = Flask(__name__)

# Your other routes and configurations...

@app.route('/check-db-connection')
def check_db_connection():
    try:
        # Attempt to query the database (e.g., fetch a count of users)
        user_count = db.session.query(db.func.count(User.UserID)).scalar()
        return jsonify({'message': 'Database connection is working!', 'user_count': user_count})
    except Exception as e:
        # Handle any database connection errors
        return jsonify({'error': 'Database connection error', 'details': str(e)}), 500  # HTTP 500 for internal server error

if __name__ == '__main__':
    app.run()
