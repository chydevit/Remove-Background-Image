from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    file = request.files['image']
    filename_wo_ext = os.path.splitext(file.filename)[0]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(input_path)
    image = Image.open(input_path)
    output = remove(image)

    output_filename = f"{filename_wo_ext}_no_bg.png"
    output_path = os.path.join(UPLOAD_FOLDER, output_filename)
    output.save(output_path, format='PNG')

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
