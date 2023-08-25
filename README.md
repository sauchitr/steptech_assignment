# steptech_assignment



## Setup
1. Install all the requirements using:
  pip install -r requirements.txt

2. Clone this repository:
  https://github.com/sauchitr/steptech_assignment.git

3. Navigate to the project directory:


## Running the Application
1. Run the Django development server:

2. Access the application in your web browser at `http://localhost:8000`.

## Database Schema
The MySQL database contains a `users` table with the following columns:
- `id` (int, primary key)
- `name` (varchar)
- `email` (varchar)
- `role` (varchar)

## Populating Sample Data
To populate the database with sample data, you can use Django's management commands:
  python manage.py makemigrations
  python manage.py migrate
  python manage.py loaddata sample_data.json

Replace `sample_data.json` with the name of your fixture file.

## Git Workflow and Contributing
We follow a Git workflow for this project. Here's how to contribute:
1. Fork the repository.
2. Clone your forked repository.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them.
5. Push your changes to your forked repository.
6. Create a pull request from your branch to the main repository.
