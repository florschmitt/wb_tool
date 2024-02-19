from fastapi import FastAPI

api = FastAPI()

# define a root `/` endpoint
@api.get("/")
def index():
    return {"ok": "API connected"}


@api.get("/predict")
def predict(feature1, feature2, feature3):

    # model = picle.load_model()
    # prediction = model.predict(feature1, feature2)

    return {'prediction': int(float(feature1)*float(feature2)*float(feature3))}
