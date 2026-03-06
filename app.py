from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>Home</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body { font-family: system-ui, Arial, sans-serif; margin: 40px; background: #f5f7fb; }
    .card { max-width: 760px; margin: 0 auto; background: white; border: 1px solid #dbe2ea; border-radius: 16px; padding: 24px; }
    h1 { margin-top: 0; }
    code { background: #eef2f7; padding: 2px 6px; border-radius: 6px; }
  </style>
</head>
<body>
  <div class="card">
    <h1>OK: Home page</h1>
    <p>Это минимальное приложение Flask, запущенное в Docker-контейнере.</p>
    <p>Проверочный адрес: <code>http://localhost/</code></p>
  </div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
