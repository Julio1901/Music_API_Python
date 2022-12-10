from flask import Flask, jsonify, request

#Criando api com o nome do arquivo atual (MusicAPI)
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

musics = [
    {
        'id': 1,
        'name': 'Beautiful Mistakes',
        'artist': 'Maroon 5'
    },
    {
        'id': 2,
        'name': 'Sugar',
        'artist': 'Maroon 5'
    },
    {
        'id': 3,
        'name': 'Lost Stars',
        'artist': 'Adam Levine'
    }
]

@app.route('/musics', methods=['GET'])
def get_musics():
    return jsonify(musics)

@app.route('/musics/<int:id>', methods=['GET'])
def get_music(id):
    for i in musics:
        if i.get('id') == id:
            return jsonify(i)

@app.route('/musics/<int:id>',methods=['PUT'])
def update_music(id):
    music_updated = request.get_json()
    for i, music in enumerate(musics):
        if music.get('id') == id:
            musics[i].update(music_updated)
            return jsonify(musics[i])

@app.route('/musics',methods=['POST'])
def create_music():
    new_music = request.get_json()
    musics.append(new_music)
    return jsonify(musics)

@app.route('/musics/<int:id>', methods=['DELETE'])
def delete_music(id):
    for i, music in enumerate(musics):
        if music.get('id') == id:
            del musics[i]
    return jsonify(musics)


app.run(port=5001,host='localhost',debug=True)