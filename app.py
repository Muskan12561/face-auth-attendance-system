from flask import Flask, render_template
import os
import csv

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Register face
@app.route("/register")
def register():
    os.system("python register_face.py")
    return "Face registration completed.<br><a href='/'>Go Back</a>"


# Start attendance
@app.route("/attendance")
def attendance():
    os.system("python face_attendance.py")
    return "Attendance process completed.<br><a href='/'>Go Back</a>"


# View attendance (PROFESSIONAL TABLE VIEW)
@app.route("/view-attendance")
def view_attendance():
    rows = []

    with open("attendance.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 4 and row[0] != "":   # strong filter
                rows.append(row)

    if len(rows) == 0:
        return "No attendance records found.<br><a href='/'>Go Back</a>"

    headers = rows[0]
    data = rows[1:]

    return render_template(
        "attendance.html",
        headers=headers,
        data=data
    )



if __name__ == "__main__":
    app.run(debug=True)
