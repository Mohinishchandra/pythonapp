
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Python Dynamic Web Application</h1>
    <form action="/welcome" method="POST">
        <input type="text" name="username"
               placeholder="Enter your name" required>
        <button type="submit">Submit</button>
    </form>
    """

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form.get("username")
    return f"<h1>Welcome, {username}!</h1><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
