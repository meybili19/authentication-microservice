import jwt
import datetime
from flask import request, jsonify
from models import db, User
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
from config import Config
import os

# Cargar las variables de entorno
load_dotenv()

# Ruta de autenticación
def authenticate_user():
    try:
        datos = request.json
        user = User.query.filter_by(email=datos['email']).first()

        # Verificar si el usuario existe
        if not user:
            return jsonify({"message": "User not found"}), 404

        # Verificar si la contraseña es correcta (si es un hash, usa check_password_hash)
        if not check_password_hash(user.password, datos['password']):
            return jsonify({"message": "Invalid credentials"}), 401

        # Si las credenciales son correctas, generar un JWT
        payload = {
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiración del token
        }
        token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

        return jsonify({
            'message': 'Login successful',
            'token': token
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400