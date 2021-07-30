from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def add(a=10, b=20):
    a = int(request.form['a'])
    b = int(request.form['b'])
    return str(a + b)


if __name__ == '__main__':
    app.run(port=7000, debug=True)
