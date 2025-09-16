from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Taxi Pricing Model API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)