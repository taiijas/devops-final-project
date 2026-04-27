import os
import socket
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Cloud Pulse App")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
CLOUD_PROVIDER = os.getenv("CLOUD_PROVIDER", "AWS Cloud")
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

@app.get("/")
def home():
    hostname = socket.gethostname()
    now = datetime.utcnow().isoformat() + "Z"

    return f"""
    <!doctype html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #e8f3ff, #ffffff);
                margin: 0;
                padding: 40px;
                color: #222;
            }}
            .card {{
                max-width: 760px;
                margin: auto;
                background: white;
                border-radius: 18px;
                padding: 32px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.12);
            }}
            h1 {{
                margin-top: 0;
                font-size: 36px;
            }}
            .badge {{
                display: inline-block;
                background: #e6f7ec;
                color: #16783a;
                padding: 8px 14px;
                border-radius: 20px;
                font-weight: bold;
            }}
            table {{
                margin-top: 24px;
                width: 100%;
                border-collapse: collapse;
            }}
            td {{
                padding: 12px;
                border-bottom: 1px solid #eee;
            }}
            td:first-child {{
                font-weight: bold;
                width: 35%;
            }}
            code {{
                background: #f3f3f3;
                padding: 4px 8px;
                border-radius: 6px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">Running</span>
            <h1>{APP_NAME}</h1>
            <p>This application demonstrates DevOps concepts using GitHub, Jenkins, Docker, AWS Cloud, and Nagios monitoring.</p>

            <table>
                <tr><td>Version</td><td>{APP_VERSION}</td></tr>
                <tr><td>Environment</td><td>{ENVIRONMENT}</td></tr>
                <tr><td>Cloud Provider</td><td>{CLOUD_PROVIDER}</td></tr>
                <tr><td>Container Hostname</td><td><code>{hostname}</code></td></tr>
                <tr><td>UTC Time</td><td>{now}</td></tr>
                <tr><td>Health Endpoint</td><td><code>/health</code></td></tr>
            </table>
        </div>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "cloud_provider": CLOUD_PROVIDER,
        "hostname": socket.gethostname(),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.get("/info")
def info():
    return jsonify({
        "project": "DevOps Final Project",
        "flow": "Developer -> GitHub -> Jenkins -> Docker -> AWS -> Nagios",
        "application": APP_NAME,
        "version": APP_VERSION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
