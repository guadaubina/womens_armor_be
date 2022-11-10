from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify
from db.db_manager import save_new_consulta, all_consultas
import random


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "hello"


@app.route('/forms', methods=['POST'])
def new_consulta():
    req_json = request.json
    print(req_json)

    consulta_id = random.randint(1000, 10000000)
    req_json["consulta_id"] = consulta_id
    save_new_consulta(req_json)

    return {
        "consulta_id": str(consulta_id)
    }


@app.route("/forms", methods=["GET"])
def show_consultas():
    return all_consultas()


if __name__ == '__main__':
    app.run()
