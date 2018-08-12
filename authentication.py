from functools import wraps
from flask import request
import firebase_admin
from firebase_admin import auth, credentials
from dotenv import load_dotenv
load_dotenv(verbose=True)
import os
from models.user import UserModel

cert = firebase_admin.credentials.Certificate({
    "type":
    "service_account",
    "project_id":
    os.getenv('FIREBASE_PROJECT_ID'),
    "private_key_id":
    os.getenv('FIREBASE_PRIVATE_KEY_ID'),
    "private_key":
    os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email":
    os.getenv('FIREBASE_CLIENT_EMAIL'),
    "client_id":
    os.getenv('FIREBASE_CLIENT_ID'),
    "auth_uri":
    os.getenv('FIREBASE_AUTH_URI'),
    "token_uri":
    os.getenv('FIREBASE_TOKEN_URI'),
    "auth_provider_x509_cert_url":
    os.getenv('FIREBASE_AUTH_PROVIDER_X509_CERT_URL'),
    "client_x509_cert_url":
    os.getenv('FIREBASE_CLIENT_X509_CERT_URL')
})
default_app = firebase_admin.initialize_app(cert)

def login_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        try:
            auth.verify_id_token(request.headers['auth'])
            return f(*args, **kwargs)
        except:
            return {'message': 'Unable to authenticate'}, 403
    return decorated_func

def admin_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        try:
            request_user_info = auth.verify_id_token(request.headers['auth'])
            user = UserModel.find_by_user_id(request_user_info['user_id'])

            if not user.is_admin:
                return {'message': 'User not an administrator.'}, 403

            return f(*args, **kwargs)
        except:
            return {'message': 'User not an administrator.'}, 403

    return decorated_func
