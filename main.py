import qrcode
from fastapi import FastAPI, Response, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="images"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <body>
            <h3>This is a qr-code creator. Go to the /qr_code?link=your_url, where your_url is an url, which you want to code into qr-code
            </h3>
        </body>
    </html>
    """

@app.get("/qr_code", response_class=HTMLResponse)
def read_item(link):
    code = qrcode.make(link)
    with open('./images/qr.png', 'wb') as qr:
        code.save(qr)
    return """
    <html>
        <body>
            <img 
                src="/static/qr.png"
            />
        </body>
    </html>
    """