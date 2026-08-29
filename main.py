import random
from flask import Flask
app = Flask(__name__)

fact_list = [
    "Más del 60% del mundo usa Internet, pero muchos aún no tienen acceso.",
    "Cada minuto se suben más de 500 horas de video a YouTube.",
    "Cada clic deja una huella digital que dice mucho de ti.",
    "El 90% de la información en línea se creó en los últimos dos años.",
    "Los centros de datos consumen más energía que muchos países."
    ]
#Pablito Clavo Un Clavito
@app.route("/")
def home():
     return f'<h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependencias tecnológicas.</h1><a href="/random_fact">¡Ver un hecho al azar!</a>'

@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(fact_list)}</p>'
    return f'<h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependencias tecnológicas.</h1><a href="/home">¡Ver un hecho al azar!</a>'
app.run(debug=True)
