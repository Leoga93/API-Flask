from flask import Flask # Importar Flask

app = Flask(__name__) # Instanciamos la aplicación 

@app.route('/') # Definiremos diferentes rutas, para esto se utiliza el decorador @app.route('/') donde se le
# Pasa la ruta como un string. Esto hace que cuando se acceda a la aplicación a través de esta ruta se va a 
# Ejecutar la aplicación hello_world
def hello_world():
    return 'Hello, world!'

@app.route('/predict')
def predict():
    return 'predicciones'

if __name__ == "__main__": # Sirven para ejecutar la aplicación
    app.run( )