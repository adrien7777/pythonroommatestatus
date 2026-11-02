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
    status = data['status']
    status_location = data['location']
    status_reason = data['reason']
    print(status, status_location, status_reason)

    saved_time = set_status(status, status_location, status_reason)

    return {"status": status, "location": status_location, "reason": status_reason, "time": saved_time}
