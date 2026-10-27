from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return{"Django":"API"}

@app.get("/course")
def courses():
    return {"Course": "Django & Backend API Development with Python"}

@app.get("/django/api")
def django():
    return{"Type":"Basic to advance"}