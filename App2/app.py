from flask import Flask, request, send_file, render_template
from flask_cors import CORS
import io
import pandas as pd
from ai4bharat.transliteration import XlitEngine
from inference.main import get_hifigan, get_Tactron2, infer


app = Flask(__name__)
CORS(app)

hifigan, h = get_hifigan()
model, hparams = get_Tactron2()

ur_rm = pd.read_csv("urdu_to_roman.csv")
ur_rm = ur_rm.set_index('0')['1'].to_dict()

e = XlitEngine(src_script_type="indic", beam_width=10, rescore=False)

def transliteration(sentence):
    words = sentence.split()
    translit = ""
    for word in words:
        try:
            translit += " " + ur_rm[word]
        except:
            translit += " " + e.translit_word(word, lang_code="ur", topk=1)[0]
    return translit.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    if 'text' not in data:
        return {"error": "No text provided"}, 400

    urdu_text = data['text']
    roman_text = transliteration(urdu_text)
    tts = infer(roman_text, False, False)

    # Create an MP3 file in a memory buffer
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # Return the MP3 as a file attachment
    return send_file(
        mp3_fp,
        mimetype='audio/mpeg',
        as_attachment=True,
        download_name='response.mp3'
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # app.run(host='0.0.0.0', port=5000)
