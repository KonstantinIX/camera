from flask import Flask, Response, render_template_string
import cv2
import time
import os


app = Flask(__name__)
DATA_FILE = 'data.txt'
# Инициализация камеры
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = camera.read()  # Чтение кадра с камеры
        if not success:
            break
        else:
            # Кодируем кадр в JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Возвращаем кадр в формате multipart
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data')
def data():
    return read_data()

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return file.read()
    return "Файл не найден."

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Viewer</title>
    <script>
        function refreshData() {
            fetch('/data')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('data').innerText = data;
                });
        }
        setInterval(refreshData, 1000); // обновляем данные каждую секунду
    </script>
</head>
<body>
    <h1>Количество вошедших</h1>
    <pre id="data">{{ data }}</pre>
    <img src="/video_feed">
</body>
</html>
'''
@app.route('/')
def index():
    data = read_data()
    return render_template_string(HTML_TEMPLATE, data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

