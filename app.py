from flask import Flask, render_template, request, jsonify, session


from main import main

app = Flask(__name__)
app.secret_key = "9801741-984ysdfsdfsdf"


def generate_data(count, description=None):
    if description:
        return main(count, description)
    return main(count)


@app.route("/")
def home():
    return render_template("index_long.html")


@app.route("/generate", methods=["POST"])
def generate_organizations():
    number = request.form.get("number")
    description = request.form.get("description")
    print(number, description)

    session['total_organizations'] = int(number)
    session['generated_organizations'] = 0
    data = generate_data(int(number), description)
    session['generated_organizations'] += len(data)
    return jsonify(data)


if __name__ == '__main__':
    Flask.run(app)
