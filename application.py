from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello():
    return "Xin Chao!!!!!"


if __name__ == '__main__':
    application.run(host= '0.0.0.0', port=5000, debug=True)
