from fastapi import FastAPI
import sample

app = FastAPI()

@app.get('/')
def index():
    return {'Hello': 'World'}

@app.get('/users/{user_id}')
def read_item(user_id: int):
    return {'user_id': user_id}

@app.get('/proofread/{text}')
def read_item(text: str):
    return {'校正後': sample.proofread(text)}
