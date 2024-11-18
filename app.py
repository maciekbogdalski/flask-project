from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Database connection
def connect_db():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "dvdrental"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASS", "postgres"),
        host=os.getenv("DB_HOST", "localhost"),
        port="5432"
    )

@app.route("/")
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM film LIMIT 10;")
    films = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", films=films, page=1)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM film WHERE title ILIKE %s LIMIT 10;", (f"%{query}%",))
    films = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", films=films, query=query, page=1)

@app.route("/page/<int:page>")
def paginate(page):
    items_per_page = 10
    offset = (page - 1) * items_per_page
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM film LIMIT %s OFFSET %s;", (items_per_page, offset))
    films = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", films=films, page=page)

@app.route("/refresh")
def refresh():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM film LIMIT 10;")
    films = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", films=films, page=1)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)


