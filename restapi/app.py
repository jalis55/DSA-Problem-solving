from flask import Flask,request
from flask_restful import Resource, Api
from transformers import pipeline

app = Flask(__name__)
api = Api(app)

class TextAnalizer(Resource):
    def post(self):
        # Endpoint to process text
        if 'text' not in request.json:
            return {"error": "No 'text' key provided"}, 400

        text = request.json['text']   
        if not text:
            return {'error': 'No text data provided'}, 400
        # pre trained model
        sentiment_pipeline = pipeline("sentiment-analysis")
        preds=sentiment_pipeline(text)
        result=preds[0]["label"]

        return {"sentiment": result}, 200

api.add_resource(TextAnalizer, '/analyze')

if __name__ == '__main__':
    app.run(debug=True)
