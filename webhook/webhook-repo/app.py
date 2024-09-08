from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['github_events']
collection = db['events']

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def github_webhook():
    event = request.json

    if 'action' in event:
        event_type = event['action']
        author = event['author']
        timestamp = datetime.utcnow()

        # Prepare the data based on the event type
        if event_type == "PUSH":
            data = {
                "author": author,
                "to_branch": event['to_branch'],
                "timestamp": timestamp,
                "event": "push"
            }
        elif event_type == "PULL_REQUEST":
            data = {
                "author": author,
                "from_branch": event['from_branch'],
                "to_branch": event['to_branch'],
                "timestamp": timestamp,
                "event": "pull_request"
            }
        elif event_type == "MERGE":
            data = {
                "author": author,
                "from_branch": event['from_branch'],
                "to_branch": event['to_branch'],
                "timestamp": timestamp,
                "event": "merge"
            }
        else:
            return jsonify({"message": "Unknown event type"}), 400

        # Store the event in MongoDB
        collection.insert_one(data)

        return jsonify({"message": "Event received", "data": data}), 201

    return jsonify({"message": "Invalid payload"}), 400


@app.route('/events', methods=['GET'])
def get_events():
    events = collection.find().sort("timestamp", -1).limit(5)  # Get the latest 5 events
    event_list = []
    
    for event in events:
        if event["event"] == "push":
            event_list.append(f"{event['author']} pushed to {event['to_branch']} on {event['timestamp']}")
        elif event["event"] == "pull_request":
            event_list.append(f"{event['author']} submitted a pull request from {event['from_branch']} to {event['to_branch']} on {event['timestamp']}")
        elif event["event"] == "merge":
            event_list.append(f"{event['author']} merged branch {event['from_branch']} to {event['to_branch']} on {event['timestamp']}")
    
    return jsonify(event_list)

if __name__ == "__main__":
    app.run(debug=True)
