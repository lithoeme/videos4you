from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get('url')
    download_type = data.get('type')  # 'video', 'playlist', 'channel'
    quality = data.get('quality')  # 'best', 'audio'

    options = {
        'format': 'best' if quality == 'best' else 'bestaudio',
        'noplaylist': download_type == 'video',
        'playlistend': 1 if download_type == 'video' else None
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        return jsonify({'status': 'success', 'title': info['title']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
