from os import listdir, set_blocking
from flask import Flask, jsonify, send_from_directory, render_template, url_for
import os

from src.torr import Torrent


pvcodes = Torrent()
PORT = os.environ.get('PORT') or 5057
app = Flask(__name__, template_folder=f'{pvcodes.basePATH}/src/template')


@app.route('/')
def root():
    print(pvcodes.basePATH)
    return render_template('index.html')


@app.route('/key=<string:keyword>')
def getTorr(keyword):
    val = pvcodes.get_Torr(keyword)
    return jsonify(val)


@app.route('/getorr=<string:id>')
def getor(id: str):
    val = pvcodes.downTorr(id)

    if val == None:
        obj = {
            '_status': 'ERROR',
            'result': [{'message': f'Torrent not found for id={id}'}]
        }
        return jsonify(obj)
    else:
        return send_from_directory(pvcodes.basePATH, f'{val}.torrent', as_attachment=True)


@app.errorhandler(404)
def not_found(e):
    return render_template('err404.html')


if __name__ == "__main__":
    app.run(debug=True)
