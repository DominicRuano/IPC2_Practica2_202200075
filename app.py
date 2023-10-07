from flask import Flask

app = Flask('__main__')

@app.route('/')
def serve_html():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
