from flask import Flask, request, render_template
from status import set_status, check_status
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('status.html', data=check_status())

@app.route("/")
def get_status():
    return {"status": check_status ()}

@app.post("/")
def update_status():
    data = request.json
    status = data.get("status", "")
    status_location = data.get("location", "")
    status_reason = data.get("reason", "")

    if not status.strip() or not status_location.strip() or not status_reason.strip():
        return {"error": "Status, location, and reason are required"}, 400

    if any(len(value) > 30 for value in (status, status_location, status_reason)):
        return {"error": "Status, location, and reason are too long"}, 400

    saved_time = set_status(status, status_location, status_reason)

    return {"status": status, "location": status_location, "reason": status_reason, "time": saved_time}

