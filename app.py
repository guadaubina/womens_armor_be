from flask import Flask
from flask_cors import CORS
import mock.mock_manager as mock

app = Flask(__name__)
CORS(app)


@app.route('/api/pedidos-ayuda/', methods=['GET'])
def get_ayuda():
    print("Hola")
    return mock.read_mock_json(mock.MOCK_ID_GET_ALL)


@app.route('/api/pedidos-ayuda/', methods=['POST'])
def post_ayuda():
    data = request.get_json()
    list.append(data)
    return mock.read_mock_json(mock.MOCK_ID_POST)


if __name__ == '__main__':
    app.run()
