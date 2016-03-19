from flask import Flask,request
from easyprocess import EasyProcess
from flask.ext.cors import CORS
app = Flask(__name__)


CORS(app)

@app.route("/generate", methods=['GET', 'POST'])
def generate():
	#get the query

	if request.method == 'POST':
		query = request.form['query']
	else:
		query = request.args.get('query')
	query = query.replace("\"","\\\"")
	command = "java -jar g.jar -qs \""+query+"\""
	command_results = EasyProcess(command).call().stdout
	result = command_results.split("RDF Output:")[1]

	return str(result)

if __name__ == "__main__":
	app.debug = True
	app.run()
