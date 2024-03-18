from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        file.save('video/traffic.mp4')
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()