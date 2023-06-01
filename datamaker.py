from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def load_categories():
    with open('categories.csv', 'r') as file:
        reader = csv.reader(file)
        categories = [row[0] for row in reader]
    return categories

@app.route('/')
def index():
    category = request.args.get('category', 'get_info')
    categories = load_categories()
    return render_template('index.html', category=category, categories=categories)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    category = request.form['category']
    line = f'("{text}", "{category}"),\n'

    with open('data.csv', 'a', newline='') as file:
        file.write(line)

    categories = load_categories()
    return render_template('index.html', message='Entry saved successfully!', category=category, categories=categories)

if __name__ == '__main__':
    app.run(port=5001)
