from flask import Blueprint, render_template, request
from .interface_connector import get_recommendations

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        model_name = request.form.get('model', 'minilm') # Default to 'minilm'
        results = get_recommendations(query, model_name)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render_template('partials/_results.html', query=query, results=results)
        else:
            return render_template('index.html', query=query, results=results)
    return render_template('index.html', query=None, results=None)
