# RouteRover

**Your Adventure Awaits — Discover the Best Routes!**

RouteRover is a desktop road trip planner built with Python and MySQL. It helps travelers discover tourist destinations across the Middle East and put together a realistic, day-by-day itinerary between two cities.

Originally built as a school Computer Science project, then rebuilt with a working database, a fixed itinerary algorithm, and a refreshed UI.

## Features

- **User accounts** — register and log in, passwords hashed with `bcrypt` (never stored in plain text)
- **Tourist location browser** — cities and landmarks stored in MySQL, each with a description and coordinates
- **Realistic trip planning** — instead of assuming one full day per stop, the itinerary is built from:
  - an assumed visit length per location
  - travel time between stops, calculated from real coordinates
  - a fixed touring window per day (e.g. 9 AM–5 PM)
  - locations that don't fit within the requested number of days are listed separately rather than silently overflowing
- **Show/hide password toggles** on login and registration
- Dark, modern UI built with plain `tkinter` (no extra GUI dependencies)

## Tech Stack

- Python 3
- Tkinter (GUI)
- MySQL (via `mysql-connector-python`)
- `bcrypt` (password hashing)

## Setup

1. **Install MySQL** and make sure the server is running locally.
2. **Create the database** by running the included SQL script:
   ```
   mysql -u root -p < database_setup.sql
   ```
   This creates the `RouteRover` database, the `users` and `tourist_locations` tables, and seeds a demo login (`testuser` / `password123`).
3. **Install Python dependencies:**
   ```
   pip install mysql-connector-python bcrypt cryptography
   ```
4. **Set your database credentials** at the top of `RouteRoverApp.py` (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`) to match your local MySQL setup.
5. **Run the app:**
   ```
   python RouteRoverApp.py
   ```

`test_connection.py` is included as a minimal script to sanity-check your database connection on its own, separate from the full app.

## Project Structure

```
RouteRoverApp.py       # main application
database_setup.sql     # creates and seeds the MySQL database
test_connection.py     # standalone DB connection test
.gitignore
```

## Screenshots

*(Add a few screenshots here of the login screen, register screen, and a sample itinerary.)*

## Notes

- Tourist location data currently covers destinations across the UAE, Jordan, Qatar, Kuwait, Bahrain, Oman, Saudi Arabia, Lebanon, and Iraq.
- The itinerary only includes stops in the selected start and end cities (not cities passed through along the way), and travel-time math assumes driving speed — it isn't flight-aware.

## Author

Mohammed Affan Parkar
