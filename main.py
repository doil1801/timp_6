from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import hashlib

app = FastAPI()

@app.get("/")
def read_root():
    return { 'info': """Для того, чтобы хэшировать строку введите следующий запрос /hash/algorithm/string. Поддерживаемые алгоритмы: md5, sha1, sha256, sha512."""
            }

@app.get("/hash/{algorithm}/{input_string}")
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
        return {
            "algorithm": "Неподдерживаемый алгоритм",
            "result_string": "Неподдерживаемый алгоритм"
        }
    return {
            "algorithm": algorithm,
            "result_string": result.hexdigest()
        }