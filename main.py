from fastapi import FastAPI

app = FastAPI()


vendas ={
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

@app.get("/")
def home():
    return {"Vendas" : len(vendas)}


@app.get("/{id}")
def findByid(id : int):
    if id in vendas:
        return vendas[id];
    else:
        return {"Error" : "Item inexistente"}

#pip install fastapi -> dependencia necessaria = acelera construcao de api
#pip install uvicorn -> dependencia necessaria = rodar projeto 
#uvicorn main:app --reload -> rodar isto main= nome do arquivo / app = nome da aplicacao instanciada da FastApi 
