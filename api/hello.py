# api/hello.py
from flask import Flask, jsonify
from vercel import Vercel

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello, Vercel!")

# Vercel wrapper to run Flask app
def handler(request):
    return Vercel(app).handle(request)
