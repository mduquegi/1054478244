from Flask import Flask

app = Flask (__name__)

@app.route('/')
def Raiz():
    numero= input("Ingrese un numero: ")
    return numero*1/2



