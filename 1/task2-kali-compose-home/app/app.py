import os
from flask import Flask

try:
    import psycopg
except Exception:
    psycopg = None

app = Flask(__name__)
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://appuser:appsecret@db:5432/appdb')


def get_db_status():
    if psycopg is None:
        return 'Unavailable', 'Модуль psycopg не установлен.'
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=3) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT current_database(), current_user;')
                db_name, db_user = cur.fetchone()
        return 'Connected', f"Подключение к БД успешно: база '{db_name}', пользователь '{db_user}'."
    except Exception as exc:
        return 'Unavailable', f'Ошибка подключения к БД: {exc}'


@app.route('/')
def home():
    db_status, db_message = get_db_status()
    return f'''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <title>Home</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body {{ font-family: system-ui, Arial, sans-serif; margin: 40px; background: #f5f7fb; }}
    .card {{ max-width: 860px; margin: 0 auto; background: white; border: 1px solid #dbe2ea; border-radius: 16px; padding: 24px; }}
    h1 {{ margin-top: 0; }}
    code {{ background: #eef2f7; padding: 2px 6px; border-radius: 6px; }}
    .ok {{ color: #166534; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>OK: Home page</h1>
    <p>Это приложение из задания 1, запущенное через Docker Compose.</p>
    <p>Перед приложением стоит <strong>Nginx</strong>, база данных — <strong>PostgreSQL</strong>.</p>
    <p><strong>Статус БД:</strong> <span class="ok">{db_status}</span></p>
    <p>{db_message}</p>
    <p>Проверочный адрес: <code>http://localhost/</code></p>
  </div>
</body>
</html>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
