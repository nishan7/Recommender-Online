import json
import urllib

from flask import Flask, render_template, request, jsonify
import recsys

app = Flask(__name__)

data = recsys.TITLES


@app.route('/')
def main():
    return render_template('main.html', data=data)


@app.route('/request', methods=['POST', 'GET'])
def recom_query():
    idxs = [int(i) for i, title in request.form.items()]
    recoms = recsys.get_recoms(idxs)
    recoms_lst = [(title, 'https://google.com/search?q=' + urllib.parse.quote(title), img_link) for title, img_link in
                  recoms]
    return jsonify(recoms_lst)


@app.route('/api/', methods=['GET'])
def recom_query_api():
    arguments = request.args['param']
    TMDbids = json.loads(arguments)
    print(TMDbids['movie_id'])
    recoms = recsys.get_recoms(TMDbids['movie_id'])
    recoms_lst = [(title) for title, img_link in
                  recoms]
    return jsonify(recoms_lst)


if __name__ == '__main__':
    app.run()

# https://image.tmdb.org/t/p/w154
