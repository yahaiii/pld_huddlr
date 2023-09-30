from flask import Blueprint, render_template, request, jsonify
from app import db
from app.models.topic_model import Topic
from flask_login import login_required

# Create a Blueprint object
topic_routes = Blueprint('topic_routes', __name__)

# Route to list all topics
@topic_routes.route('/topics', methods=['GET'])
def list_topics():
    topics = Topic.query.all()
    topic_list = [{'id': topic.id, 'name': topic.name} for topic in topics]
    return jsonify({'topics': topic_list})

# Route to create a new topic
@topic_routes.route('/topics', methods=['POST'])
@login_required  # Requires user authentication
def create_topic():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Topic name is required'}), 400

    topic = Topic(name=name)
    db.session.add(topic)
    db.session.commit()

    return jsonify({'message': 'Topic created successfully'}), 201

# Route to delete a topic by ID
@topic_routes.route('/topics/<int:topic_id>', methods=['DELETE'])
@login_required  # Requires user authentication
def delete_topic(topic_id):
    topic = Topic.query.get(topic_id)

    if not topic:
        return jsonify({'error': 'Topic not found'}), 404

    db.session.delete(topic)
    db.session.commit()

    return jsonify({'message': 'Topic deleted successfully'})

# Add more routes and functionality as needed
