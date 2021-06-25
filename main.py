from flask import Flask, jsonify

app = Flask(__name__)

dht = -1
watering_flag = False


@app.route('/get-dht', methods=['GET'])
def get_dht():
    return jsonify({'dht': dht})


@app.route('/set-dht/<val>', methods=['POST'])
def set_dht(val):
    global dht
    dht = val
    return jsonify({})


@app.route('/get-wf', methods=['GET'])
def get_wf():
    return jsonify({'watering_flag': watering_flag})


@app.route('/set-wf/<val>', methods=['POST'])
def set_wf(val):
    global watering_flag
    if val == 0:
        watering_flag = False
    else:
        watering_flag = True
    return jsonify({})


if __name__ == '__main__':
    app.run(port=5000)
