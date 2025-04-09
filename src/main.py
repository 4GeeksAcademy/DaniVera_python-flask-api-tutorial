#importa la clase flack desde la libreria
from flask import Flask

#creamos una instancia de la aplicación Flask
#__name__---app = Flaski(main.py)
app = Flask(__name__)

@app.route("/")#decorador (FORMA RAPIDA DE EXTENDER LA FUNCION DEF HELLO., AÑADES UN PODER MAS. DECORADOR---ENVUELVES TAZA CAFE CON FUNDA),le dice a Flask : cuando alguien entre a "/, ejecuta la funcion hello" 
def hello():
    return "Hello, Flask!"
#preguntamos a Py si esto se esta ejecutando o importando
if __name__ == "__main__":
    #app.run hace que corra la aplicación= el tRUE ACTIVA EL MODO DESARROLLADOR
    app.run(debug=True)