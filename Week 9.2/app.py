from flask import Flask, render_template, request

app = Flask(__name__)


# http://localhost:5000/home
# http://www.antkh.com/home
@app.route("/home", methods=["GET", "POST"])
def home():
    text = "hello world"
    if request.method == "POST":
        text = request.form["textinput"]

    words = text.split()

    # return render_template(
    #     "home.html", 
    #     text=text,
    #     letters=len(text), 
    #     words=len(words)
    # )

    return f"""
    Count Letters & Words<br>
    - Letter: {len(text)}<br>
    - Words: {len(words)}<br>
    """


@app.route('/about', methods=["POST"])
def about():
    return "Create by Sambo."


@app.route("/post/1")
def product():
    return render_template("post/1.html")

app.run(debug=True)
