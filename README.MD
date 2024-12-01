<h1 align="center">
API EM PYTHON
</h1>

## Tecnologias

- [Fastapi](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)


## Como Executar

- Clonar repositório git
- Instalar dependencias
```
pip install fastapi

pip install uvicorn
```

- Executar a aplicação:
```
uvicorn main:app --reload
```

A API poderá ser acessada em [localhost:8080](http://localhost:8080).
O Swagger poderá ser visualizado em [localhost:8080/swagger-ui.html](http://localhost:8080/docs)

## API Endpoints

Para fazer as requisições HTTP abaixo, pode ser feita diretamente no navegador ou na documentação

- Visualizar se a api esta funcionando
```
$ http GET :8080/

  {
    Vendas : 4
  }

```

- Buscar pelo id 
```
$ http GET :8080/1

  {
    "item": "lata",
    "preco_unitario": 4,
    "quantidade": 5
    
    }


```