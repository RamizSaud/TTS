from flask import Flask, request, send_file, render_template
from flask_cors import CORS
from gtts import gTTS
import io

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    if 'text' not in data:
        return {"error": "No text provided"}, 400

    urdu_text = data['text']
    tts = gTTS(text=urdu_text, lang='ur', slow=False)

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
