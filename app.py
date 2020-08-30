from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)



@app.route('/')
def hello():
    # return "Hello World!"
    data = [(1,'nishan'), (2, 'paudel'), (3, 'upadhyay'), (5,'today'), (6,'soory'),(7,'back to work'),(8,'right now')]
    return  render_template('index.html', data=data)

@app.route('/request', methods=['POST','GET'])
def recom_query():
    print('hello')
    print(request.form)
    return redirect(url_for('hello'))

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()