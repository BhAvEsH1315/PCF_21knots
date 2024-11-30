Instructions to Run the Project

************************************

python manage.py runserver

python pcf_client.py

************************************

URLs and Their Functions

************************************

1. Admin Interface
URL: http://localhost:8000/admin/

Function:
Access the Django Admin Interface.

Use:
Manage the database models, including adding, editing, and deleting records. This is an administrative interface for superusers.

************************************

2. Message API Endpoint
URL: http://localhost:8000/api/messages/

Function:
API endpoint for listing and creating messages.

Use:
GET Request: Retrieve and list all messages stored in the database.
POST Request: Create a new message by sending JSON data containing the product name, carbon footprint, reference start, and reference stop.

************************************

3. Message History Page
URL: http://localhost:8000/api/history/

Function:
Custom page displaying the entire history of received messages in a table format.

Use:
Shows a list of messages with their product name and timestamp.
Clicking "Show Details" toggles the visibility of detailed information, such as carbon footprint, reference start, and reference stop.

************************************

4. Message Form Page
URL: http://localhost:8000/api/message-form/

Function:
Custom form page where users can submit new messages.

Use:
Form Display: Shows a form for users to input product name, carbon footprint, and reference period (start and stop).
Form Submission: Handles form submission, validates the input, adjusts timestamps to the local timezone, and saves the data to the database. Redirects back to the form page or another specified page after submission.
