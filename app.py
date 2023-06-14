from flask import Flask, render_template, request, redirect, session, url_for, jsonify

from main import main

app = Flask(__name__)
app.secret_key = "9801741-984ysdfsdfsdf"
#
#
# @app.route('/submit-data', methods=['POST'])
# def display_table():
#     number_of_organizations = request.json.get("numberOfOrganizations")
#     print(number_of_organizations)
#     data = main(number_of_organizations)
#
#     columns = ["Organization Name", "Website", "Contact Information", "Specialization"]
#     # return render_template("table.html", data=data, columns=columns)
#
#
#     session['data'] = data
#
#     # Redirect to the index page
#     return redirect(url_for('index'))
#
#
# @app.route('/')
# def index():
#     data = session.get('data')
#     columns = ["Organization Name", "Website", "Contact Information", "Specialization"]
#     if data:
#         # Retrieve the data from the session
#         # data = session.get('data')
#
#         # Define the columns for the table
#
#
#         # Pass the data and columns to the template
#         return render_template('table.html', data=data, columns=columns)
#     return render_template('table.html', columns=columns)
#
#
#
# if __name__ == "__main__":
#     app.run(debug=True)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_organizations():
    number = request.form.get('number')
    data = main(number)
    return jsonify(data)