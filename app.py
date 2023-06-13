from flask import Flask, render_template


from main import main

app = Flask(__name__)


@app.route("/")
def display_table():
    data = main()

    columns = ["Organization Name", "Website", "Contact Information", "Specialization"]
    return render_template("table.html", data=data, columns=columns)


if __name__ == "__main__":
    app.run(debug=True)
