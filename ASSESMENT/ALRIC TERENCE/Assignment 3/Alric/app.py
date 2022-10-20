from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)
app.secret_key="Alric"

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/branch/1")
def branch1():
    return render_template('branch1.html')


@app.route("/branch/2")
def branch2():
    return render_template('branch2.html')


@app.route("/branch/3")
def branch3():
    return render_template('branch3.html')


@app.route("/branch/4")
def branch4():
    return render_template('branch4.html')


@app.route("/branch/5")
def branch5():
    return render_template('branch5.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
