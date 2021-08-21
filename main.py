from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = "25g0thqearovnf@0943qgjervwdlk;"


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':

    app.run(debug=True)
