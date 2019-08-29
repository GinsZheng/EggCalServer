from flask import Flask, jsonify
import random
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    randomNum = random.randint(int('0x4e00', 16), int('0x9fa5', 16))
    randomUnicode = "\\u%x" % randomNum
    randomWord = str(randomUnicode.encode('utf-8').decode('unicode_escape'))

    blackEggProbability = str(random.randint(1, 333))
    # imageLink = "https://www.baidu.com/img/bd_logo1.png?qua=high"
    imageLink = "http://127.0.0.1:5000/static/images/imageInBlackEgg.png"

    return jsonify({'word': randomWord, 'probability': blackEggProbability, 'link': imageLink})


if __name__ == '__main__':
    app.run()
