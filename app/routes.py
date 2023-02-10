from app import app


@app.route('/')
@app.route('/index')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Title</title>
    </head>
    <body>
    <h1>Header</h1>
    <p>Paragraph</p>
    </body>
    </html>'''
