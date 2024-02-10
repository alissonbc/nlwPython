from flask import Blueprint, jsonify, request

tagsRoutesBp = Blueprint('tagsRoutes', __name__)

@tagsRoutesBp.route('/createTag', methods=['POST'])
def create_tag():
    print(request.json)
    return jsonify({'response': 'ok'}), 200