from flask import Flask, render_template

app = Flask(__name__)

usuario = {
    "nombre": "Soy Rodolfo",
    "descripcion": "🚀 Ciencia de datos, innovación y tecnología.",
    "imagen": "perfil.jpg"
}

enlaces = [
    {"nombre": "LinkedIn", "url": "https://www.linkedin.com/in/rodolfojapa", "icono": "fab fa-linkedin", "color": "#0077B5"},
    {"nombre": "YouTube", "url": "https://www.youtube.com/@rodolfojapa", "icono": "fab fa-youtube", "color": "#FF0000"},
    {"nombre": "Kick", "url": "https://kick.com/rodolfojapa", "icono": "fa-solid fa-play", "color": "#52FF00"},
    {"nombre": "Discord", "url": "https://discord.gg/rodolfojapa", "icono": "fab fa-discord", "color": "#5865F2"},
    {"nombre": "GitHub", "url": "https://github.com/rodolfojapa", "icono": "fab fa-github", "color": "#24292F"}
]

@app.route('/')
def index():
    return render_template('index.html', usuario=usuario, enlaces=enlaces)

if __name__ == '__main__':
    app.run(debug=True)
