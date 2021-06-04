from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "you deplyed it"}



if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)