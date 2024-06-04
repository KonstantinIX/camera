# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def get_variable():
#     # from main import count
#     # print(count)
#     # return count
#     with open('example.txt', 'r') as file:
#         data = file.read()
#         return "Значение переменной: " + data
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from datetime import datetime

app = Flask(__name__)
#это декоратор во Flask, который указывает на конечную точку маршрута
@app.route("/")
# функция для сцитывания данных из файла и вывод их на сайт
def home():
    with open('example.txt', 'r') as file:
        data = file.read()
        # бновление страницы каждую секунду
        # content количество секунд
        return """
<meta http-equiv="refresh" content="1" /> 
""".format(datetime.strftime(datetime.now(), "")) + "Количество вошедших: " + data
# запуск локального сервера
if __name__ == "__main__":
    app.run()