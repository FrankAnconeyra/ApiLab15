from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.post("/enviarApi")
async def recibir_datos_desde_laravel(request: Request):
    datos = await request.json()
    print("Datos recibidos desde Laravel:", datos)
    return {"message": "Datos recibidos correctamente"}


fotos = [
    {"id": 1, "ruta": "ruta1", "descripcion": "descripción1"},
    {"id": 2, "ruta": "ruta2", "descripcion": "descripción2"},
]

def ordenar_fotos(lista_fotos, id_foto_primera):
    foto_primera = None
    for foto in lista_fotos:
        if foto["id"] == id_foto_primera:
            foto_primera = foto
            lista_fotos.remove(foto)
            break
    if foto_primera:
        lista_fotos.insert(0, foto_primera)
    return lista_fotos

fotos_ordenadas = ordenar_fotos(fotos.copy(), 2)  

url = "http://127.0.0.1:8000/enviarApi"

try:

    response = requests.post(url, json={"datos": fotos_ordenadas})

    if response.status_code == 200:
        print(response.json())  
    else:
        print("Error en la solicitud:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error en la solicitud:", e)
