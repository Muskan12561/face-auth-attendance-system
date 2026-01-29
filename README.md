
---

## Requirements

- Python 3.9 or above  
- Webcam  
- Windows OS (tested on Windows)  

---

## How to Use (Step by Step)

### Step 1: Copy the Project

Option 1: Clone using Git
```bash
git clone https://github.com/Muskan12561/face-auth-attendance-system.git


Option 2: Download ZIP

Click Code → Download ZIP

Extract the folder


Step 2: Place the Project in a Simple Path (Recommended)

Move the extracted folder to a simple path like:
C:\Projects\Face-Attendance-System


Step 3: Open Terminal in the Project Folder
cd C:\Projects\Face-Attendance-System

Step 4: Install Required Libraries
pip install flask
pip install opencv-python
pip install numpy

Step 5: Run the Application
python app.py


You should see output like:

Running on http://127.0.0.1:5000

Step 6: Open the Web Interface

Open a browser and go to:

http://127.0.0.1:5000




 Click "Register Face"
   - Camera opens
   - Face images are captured for registration

 Click "Start Attendance"
   - Camera opens
   - Face is recognized
   - Punch-In / Punch-Out is recorded

 Click "View Attendance"
   - Attendance records are displayed in a table
