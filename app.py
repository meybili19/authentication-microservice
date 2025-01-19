from flask import Flask, render_template
from flask_cors import CORS
from config import Config
from models import db
from routes import authenticate_user

# Crear la aplicación
app = Flask(__name__,  static_folder='FRONTEND')

# Habilitar CORS
CORS(app)

# Configuración de la aplicación
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)


@app.route('/')
def home():
    return "Home Page - Please login first"

# Registrar la ruta de autenticación
@app.route('/login', methods=['POST'])
def login_route():
    return authenticate_user()

# Nueva ruta para la vista CRUD
@app.route('/crud_user')
def crud_user():
    return render_template('crud_user.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
