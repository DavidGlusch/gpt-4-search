from flask import Flask, render_template, request, jsonify, session
from core.main import main

app = Flask(__name__)
app.secret_key = "9801741-984ysdfsdfsdf"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_organizations():
    number_of_organizations = int(request.form.get("number_of_organizations"))
    user_prompt = request.form.get("prompt")
    print(number_of_organizations, f"User`s prompt: {user_prompt}")

    session['total_organizations'] = number_of_organizations
    session['generated_organizations'] = 0
    data = main(number_of_organizations, user_prompt)
    session['generated_organizations'] += len(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
