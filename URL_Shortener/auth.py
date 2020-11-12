from functools import wraps
from flask import request, Response, current_app


#the username and password can be found on ".env" file
def check_auth(username, password):
	return username == current_app.config['ADMIN_USERNAME'] and password == current_app.config['ADMIN_PASSWORD']

def authenticate():
	return Response(
		'Could You Verify Your Access Level\nYou Have To Log In With Proper Credentials',
		401, {'www-Authenticate': 'Basic realm="Login Required"'})

def require_auth(f):
	@wraps(f)
	def decored(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()

		return f(*args, **kwargs)

	return decored