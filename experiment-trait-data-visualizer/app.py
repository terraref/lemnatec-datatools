from api_data_retrieval.trait_data_retrieval import get_trait_data
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

@app.route('/')
def data_summary():
	trait_data = get_trait_data(2016, 8, 12)
	return render_template('index.html', trait_data=trait_data)

if __name__ == '__main__':
	app.run()