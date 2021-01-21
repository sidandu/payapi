#!flask/bin/python
from payment_utils import payment_input_validator
from payment_gateway import payment_methods
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'dandu':
        return 'pass123'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from default auth popup
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/payment/api', methods = ['GET'])
@auth.login_required
def make_payment():
    try:
        validator_obj = payment_input_validator(request.json)
        validate_resp = validator_obj.validate_payment_info()
        if validate_resp:
            print("Log :: Invalid payment details :: ",validate_resp)
            return make_response(jsonify( { 'error': 'Bad request' } ), 400)
        else:
            print("valid payment details")
            pay_obj = payment_methods(request.json)
            pay_obj.select_payment_gateway()
            return jsonify( { 'payment_status': 'success' } ), 200
    except Exception:
        return make_response(jsonify( { 'error': 'Internal server error' } ), 500)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug = True)
