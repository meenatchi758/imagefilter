from flask import Flask, render_template

app = Flask(__name__)

# Sample images and tags
images = [
    {"filename": "bakery cate 1.png", "tag": "nature"},
    {"filename": "bakery cate 2.png", "tag": "nature"},
    {"filename": "bakery cate 3.png", "tag": "city"},
    {"filename": "bakery cate 4.png", "tag": "animals"},
]

@app.route('/')
def index():
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
