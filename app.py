from flask import Flask, jsonify, url_for
import random

app = Flask(__name__)

app.config.from_pyfile('config.py')


@app.route('/')
def hello_world():
    random_num = random.randint(int('0x4e00', 16), int('0x9fa5', 16))
    random_unicode = "\\u%x" % random_num
    random_word = str(random_unicode.encode('utf-8').decode('unicode_escape'))

    black_egg_probability = str(random.randint(1, 1000))

    image_url = url_for('static', filename='images/imageInBlackEgg.png')
    image_link = app.config['DOMAIN'] + image_url

    return jsonify({'word': random_word, 'probability': black_egg_probability, 'link': image_link})


if __name__ == '__main__':
    app.run(port=5001)
