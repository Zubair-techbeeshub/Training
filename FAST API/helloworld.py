from fastapi import FastAPI

app = FastAPI()
@app.get('/')
async def index():
    return {'hello':'world'}

@app.get('/about')
async def about():
    return {'about':'This is an IT Company'}
