# RSS Feed scraper


 This is a Django-based web application that aggregates RSS feeds. It includes a set of RESTful APIs to allow the front-end to interact with the back-end services.
Getting Started
To run the project, simply clone it from GitHub and use docker-compose to start the service. Follow the steps below:
 1 Clone the repository
 2 In the project directory, run docker-compose up -d --build
 3 Navigate to http://localhost in your web browser

## Endpoints

Once the project is running, the following endpoints can be used to interact with the application.


| endpont                     | methods | description                                                                                                                                                                             |
|-----------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /api/v1/feed/feeds          | GET     | This endpoint returns a list of all feeds currently in the database.
| /api/v1/feed/feed/<pk>      | GET/PUT |This endpoint returns a detail view for the given feed, where pk is the primary key of the feed.
| /api/v1/feed/force-update/  | GET     | This endpoint triggers a Celery task to update all feeds in the database.


## Task Queue

The application uses Celery to support background task processing. The UpdateFeeds task is responsible for retrieving and updating RSS feeds in the database. This task is triggered periodically via a scheduled Celery beat.

## Database
The application uses a PostgreSQL database to store feed data. For development purposes, a SQLite database is used.
