from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Hello World!</h1>"

@app.route('/dojo')
def dojo():
	return f"<h1>Dojo!</h1>"

@app.route('/say/<name>')
def sayMyName(name):
	print("say: " + name)
	return f"<h1>Hi {name.capitalize()}!</h1>"

@app.route('/repeat/<int:num_times>/<phrase>')
def repeatPhrase(phrase, num_times):
	print(phrase)
	print(num_times)
	title = "Repeater"
	return render_template('index.html', title=title, phrase=phrase, num_times=num_times)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('index.html', title='404', phrase='Sorry! No response. Try again.', num_times=1)

if __name__ == "__main__":
	app.run(debug=True)