from flask import Flask, Response, render_template_string

import os

import OpenCVproject

#������� ��������� ���������� Flask. __name__ ��������� �� �������� �������� �����
app = Flask(__name__)

DATA_FILE = 'data.txt'

@app.route('/video_feed')
def video_feed():
    return Response(OpenCVproject.doAFaceSearch(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data')
def data():
    return read_data()

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return file.read()
    return "Файл не найден"

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Camera</title>
    <script>
        function refreshData() {
            fetch('/data')
                .then(response => response.text())
                .then(data => {
                    document.getElementById('data').innerText = data;
                });
        }
        setInterval(refreshData, 1000);
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

if __name__ == 'PythonApplication':
    print("rabotaet")
    app.run(host='0.0.0.0', port=5000)