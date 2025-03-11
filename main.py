from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import hashlib

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <body>
            <h3>Для того, чтобы хэшировать строку введите следующий запрос /hash/algorithm/string,
                Поддерживаемые алгоритмы: md5, sha1, sha256, sha512.
            </h3>
        </body>
    </html>
    """

@app.get("/hash/{algorithm}/{input_string}", response_class=HTMLResponse)
def read_root(algorithm, input_string):
    if algorithm == 'md5':
        result = hashlib.md5(input_string.encode('utf-8'))
    elif algorithm == 'sha1':
        result = hashlib.sha1(input_string.encode('utf-8'))
    elif algorithm == 'sha256':
        result = hashlib.sha256(input_string.encode('utf-8'))
    elif algorithm == 'sha512':
        result = hashlib.sha512(input_string.encode('utf-8'))
    else:
        return """
        <html>
            <body>
                <h3>Неподдерживаемый вид хэширования</h3>
            </body>
        </html>
        """
    return f"""
    <html>
        <body>
            <h3>
            Исходная строка: {input_string}
            </h3>
            <h3>
            Вид хэширования: {algorithm}
            </h3>
            <h3>
            Ваш результат: {result.hexdigest()}
            </h3>
        </body>
    </html>
    """