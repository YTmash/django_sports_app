Sports in Manitoba App

Overview

This Django-based web application provides information on various sports that can be played in Manitoba. Users can explore different sports, learn about local teams, and find locations to participate in their favorite activities.

Features

List of sports available in Manitoba

Information on local teams and leagues

Search and filter options for sports and locations

User authentication for personalized experiences

Ability to save favorite sports and teams

Database Structure

Field Name

Data Type

Description

Player's Last Name

VARCHAR(255)

Player's surname

Age

INT

Player's age

Position

VARCHAR(255)

Player's position

Deployment

Push the project to a cloud hosting service (e.g., AWS, Heroku, DigitalOcean).

Configure the database and environment variables.

Run migrations and collect static files:

python manage.py migrate
python manage.py collectstatic

Restart the server and access the application via your domain.

Future Enhancements

Implement live match tracking.

Add leaderboards and rankings.

Integrate data visualization for player stats.

Enhance social sharing features.

Include a sports event calendar.

Provide real-time weather updates for outdoor sports.

Contact

For any inquiries or contributions, feel free to reach out to [your email] or visit the GitHub repository.
