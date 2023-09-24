from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
 
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        post = request.form["text"]
        return render_template("index.html", post=post)
 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)