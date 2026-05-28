from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Esto busca tu HTML dentro de la carpeta 'templates'
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)