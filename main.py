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


@app.route('/key=<string:keyword>&maxCount=<string:cnt>')
@app.route('/key=<string:keyword>&mx=<string:cnt>')
@app.route('/k=<string:keyword>&maxCount=<string:cnt>')
@app.route('/k=<string:keyword>&mx=<string:cnt>')
@app.route('/key=<string:keyword>')
@app.route('/k=<string:keyword>')
def getTorr(keyword, cnt='15'):
    cnt = int(cnt)
    if cnt <= 0:
        return jsonify({'_status': 'OK', 'result': []})
    val = pvcodes.get_Torr(keyword, cnt)
    print(len(val['result']))
    return jsonify(val)


@app.route('/getorr=<string:id>')
def download_torr(id: str):
    val = pvcodes.downTorr(id)

    if val == None:
        obj = {
            '_status': 'ERROR',
            'result': [{'message': f'Torrent not found for id={id}'}]
        }
        return jsonify(obj)
    else:
        return send_from_directory(pvcodes.basePATH, f'{val}.torrent', as_attachment=True)


@app.route('/recent')
@app.route('/r')
def getRecnt():
    obj = pvcodes.getRecent()
    return jsonify(obj)


@app.route('/info=<string:id>')
@app.route('/i=<string:id>')
def get_torr_info(id: str):

    resObj = pvcodes.getInfo(id)
    print(resObj['_status'])
    return jsonify(resObj)


@app.errorhandler(404)
def not_found(e):
    return render_template('err404.html')


if __name__ == "__main__":
    app.run(debug=True)
