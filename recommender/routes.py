import os
from flask import Flask, request, jsonify
from recommender.train import load_cos, recommendations

app = Flask(__name__)

#test endpoint
@app.route("/")
def index():
    return "all is up and running"

@app.route("/title", methods=['post'])
def recommend_title():
    try:
        title = request.json['title']
        top_5_rec=recommendations(title,load_cos())
            
        
        return jsonify(top_5_rec)
    except Exception as e:
        print(e)
        return jsonify({
            "status": "failed",
            "response": "Check the input json",
            "error": str(e)
            })
