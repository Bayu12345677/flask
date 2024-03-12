from cmath import pi
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
import requests
import shutil, os, easyocr

app = Flask(__name__)
  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ocr_bypasses', methods=['POST'])
def ocr_bypasses():
  if request.method == 'POST':
    data = request.get_json(force=True)
    url = data['url']
    """
    img = requests.get(url, stream=True).raw
    img_name = 'img.jpeg'
    with open(img_name, 'wb') as out_file:
      shutil.copyfileobj(img, out_file)
    """
    os.system(f"curl -sL {url} -o img.jpeg")
    atext = easyocr.Reader(['en'], gpu = False)
    text = atext.readtext('img.jpeg')
    return jsonify({'url':text,'result':text})
    # return jsonify({'result':url})
  else:
    return 'Error'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
