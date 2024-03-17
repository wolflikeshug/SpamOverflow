from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/health')
def health():
    return jsonify({'status': 'ok'})


@api.route('/customers/<int:customer_id>/emails', methods=['GET'])
def get_emails(customer_id):

    limit = request.args.get('limit', default = 100, type = int)
    offset = request.args.get('offset', default = 0, type = int)
    start_time = request.args.get('start_time', default = None, type = str)
    end_time = request.args.get('end_time', default = None, type = str)
    from_email = request.args.get('from_email', default = None, type = str)
    to_email = request.args.get('to_email', default = None, type = str)
    state = request.args.get('state', default = "all", type = str)
    only_malicious = request.args.get('only_malicious', default = False, type = bool)

    return jsonify({
            "customer_id": customer_id,
            "limit": limit, 
            "offset": offset,
            "start_time": start_time,
            "end_time": end_time,
            "from_email": from_email,
            "to_email": to_email,
            "state": state,
            "only_malicious": only_malicious
    })

@api.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    return jsonify({
        "id": todo_id,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    })

@api.route('/todos', methods=['POST'])
def post_todo():
    return jsonify({
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2023-02-27T00:00:00",
        "created_at": "2023-02-20T00:00:00",
        "updated_at": "2023-02-20T00:00:00"
    }), 201

