from flask import Flask
import os
import datetime
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username (safe alternative to os.getlogin())
    system_username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"

    # Get current time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    # Get top output safely
    top_processes = "\n".join([
        f"PID: {p.info['pid']}, Name: {p.info['name']}, CPU: {p.info['cpu_percent']}%" 
        for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])
    ][:10])

    return f"""
    <html>
    <body>
        <h1>HTOP Information</h1>
        <p><strong>Name:</strong> Sourav Deb</p>
        <p><strong>Username:</strong> {system_username}</p>
        <p><strong>Server Time (IST):</strong> {formatted_time}</p>
        <h2>Top Processes:</h2>
        <pre>{top_processes}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
