from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, welcome to the Flask app!"})

@app.route('/goodbye', methods=['GET'])
def goodbye():
    return jsonify("GOODBYE LITTLE GIRL!!")

if __name__ == '__main__':
    app.run(debug=True)
