from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    output_file_path = 'c:/sharedbi/inter_complete.txt'

    if os.path.exists(output_file_path):
        with open(output_file_path, 'r', encoding='utf-8') as f:
            interpretation = f.read()
    else:
        interpretation = "Aucune interprétation disponible."

    return render_template('index.html', interpretation=interpretation)

if __name__ == '__main__':
    app.run(debug=True)
