from flask import Flask, make_response, request, abort, jsonify, render_template
# from api import make_soft_prediction
# from api import make_hard_prediction, open_email

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST'])
def index():
    return render_template('index.html', email_text=None)

# @app.route('/spam_score', methods=['POST'])
# def spam_or_ham():
#     if not request.json or ('email' not in request.json):
#         abort(400)
#
#     email = request.json['email']
#     prediction = make_hard_prediction(email)
#     score = make_soft_prediction(email)
#
#     response = {
#         'email': email,
#         'prediction': prediction,
#         'score': score
#     }
#
#     return jsonify(response), 201
@app.route('/tableau')
def get_tableau_page():
    return render_template('tableau.html')

if __name__ == '__main__':
    app.run(debug=True)
