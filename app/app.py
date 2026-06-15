from flask import Flask
import os
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("CLOUD_PROVIDER", "unknown")
    host = os.getenv("HOSTNAME", "local")

    return f"""
    <html>
    <head>
        <title> Welkom to CAPOC v2 | ☁️</title>
        <style>
            body {{ font-family: Arial; background:#0f172a; color:white; height:100vh; display:flex; align-items:center; justify-content:center; }}
            .card {{ background: #1e293b; padding:40px; border-radius:16px; width:520px; }}
            h1 {{ color:#38bdf8; }}
            .ok {{ color:#22c55e; font-weight:bold; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Cloud Agnostic Prototype</h1>
            <p class="ok">Application Running</p>
            <p><b>Environment:</b> {env}</p>
            <p><b>Host:</b> {host}</p>
            <p><b>Tijd:</b> {datetime.now(ZoneInfo("Europe/Amsterdam")).strftime("%d-%m-%Y %H:%M:%S")}</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)