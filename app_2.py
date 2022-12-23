from flask import Flask, render_template, request, redirect, url_for
flask_application = Flask(__name__)


@flask_application.route("/", methods=['GET','POST'])
def home():
	if request.method == 'POST':
		val1 = request.form['val1']
		val1 = int(val1)
		val2 = request.form['val2']
		val2 = int(val2)
		operator = request.form['operator']

		
		if operator == "+":
			result = val1 + val2
		elif operator == "-":
			result = val1 - val2
		elif operator == "*":
			result = val1 * val2
		else:
			return redirect(url_for("calculate_error", operator=operator))

		return redirect(url_for("calculate", text_result=result))

	return render_template("index_2.html", 
						   content="Imanuel")

@flask_application.route("/<text_result>", methods=['GET'])
def calculate(text_result):
	return f'Hasil calculation: {text_result}'

@flask_application.route("/calculate-error?operator=<operator>", methods=['GET'])
def calculate_error(operator):
	return f'{operator} error'

if __name__ == '__main__':
	flask_application.run()