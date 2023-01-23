from flask import Flask, jsonify
 
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def hello_world():
    result = {
        'message': '日本語 Hello world'
    }
    return jsonify(result)
 
@app.route('/post/', methods=["POST", "GET"])
def hello_post():
    result = {
        'post': 'ポスト'
    }
    return jsonify(result)
 
@app.route('/get/<key>', methods=["GET"])
def hello_get(key):
    res = key
    if (key == "abc"):
        res = "ABC"
    elif (key == "xyz"):
        res = "XYZ"
    result = {
        'get': res
    }
    return jsonify(result)
 
if __name__ == "__main__":
    app.run()
