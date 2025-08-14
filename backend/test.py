from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
    
    
@app.get('/favicon.ico', include_in_schema=False)
async def default_favicon():
    return FileResponse("favicon.ico")