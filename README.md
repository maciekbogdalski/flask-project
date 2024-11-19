# DVD Rental App

A simple Flask-based web application for browsing, searching, and viewing details about movies from a DVD rental database.

## Features
- Responsive UI built with **Bootstrap**.
- Search movies by title or keywords.
- View detailed information about each movie.
- Pagination support for easy navigation.
- Backend powered by Flask and PostgreSQL.

## Requirements
- Python 3.7+
- PostgreSQL database
- Docker (for deployment)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/dvd-rental-app.git
   cd dvd-rental-app
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file for environment variables:
   ```bash
   DATABASE_URL=your_postgresql_database_url
   ```

5. Run the application locally:
   ```bash
   python -m flask run
   ```

## Deployment

This app uses Docker for deployment on platforms like Heroku.

### Deploy on Heroku

1. Build and push the Docker container:
   ```bash
   heroku container:push web --app your-app-name
   ```

2. Release the container:
   ```bash
   heroku container:release web --app your-app-name
   ```

3. Open the app:
   ```bash
   heroku open --app your-app-name
   ```


## Tech Stack
- **Frontend**: HTML, CSS, Bootstrap 5
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Deployment**: Docker, Heroku (Containerized)

## License

This project is licensed under a Proprietary License. All Rights Reserved. Unauthorized copying, modification, or distribution of this software is strictly prohibited.
