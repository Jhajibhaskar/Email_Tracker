# Email_Tracker
To implement the above code, follow these steps:





1.Install the required dependencies by running the command pip install flask sqlite3.

2.Run the email-tracker.py file in VS Code or PyCharm

3.The application should now be running and listening for HTTP requests on the default port 5000.

4.To test the email tracking functionality, open a web browser and navigate to http://localhost:5000/email-open?email=example@example.com, replacing example@example.com with the email address you want to track.

5.The response should be a 1x1 transparent GIF image, indicating that the email open was tracked successfully.

6.To view the tracked data, .db created in the same folder in which email_tracker.py file is available (you can connect to the SQLite database using a tool such as DB Browser for SQLite and run a SELECT query on the email_tracking table).
