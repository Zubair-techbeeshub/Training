from fastapi import FastAPI

app = FastAPI()
@app.get('/')
async def index() -> dict[str,str]:
    return {'hello':'world'}

@app.get('/about')
async def about() -> dict [str,str]:
    return {'about':'This is an IT Company'}
