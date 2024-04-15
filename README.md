# Spotify Top 50 Songs - Philippines [Data]

## Project Overview

- Collects data from a Spotify playlist and stores in a Postgres database.
- Playlist: https://open.spotify.com/playlist/37i9dQZEVXbNBz9cRCSFkY
- Syncs daily

**Disclaimer:** In accordance with Spotify API's Terms and Conditions, collected data may not be used for profit or commercial purposes.

### Web Application Progress

![AppUI](/archive/app-ui-progress/2024-04-15_20-19-21.png)

- TODO: Titles not linked to song's web URL
- TODO: Deploy via Render

## Tasks:

- [x] Create project, setup virtual environment
- [x] Get data from playlist

  - [x] Establish connection to Spotify API
  - [x] Store data in a Postgres database
    - [x] Create database
    - [x] Create staging table
      - [x] Store raw API data in table
    - [x] Create final table
    - [ ] Add clean data to final table
      - [ ] VALIDATE:
        - [] Re-check types of data before adding to final table
        - [ ] Check null values
        - [ ] Convert to data types to valid ones (e.g. Date in Album Release Date must have YYYY-MM-DD format)

- [ ] Store data in a cloud data warehouse (use DataBricks, Data Factory)
  - [ ] Design datawarehouse schema (?)
- [ ] Set schedule for fetching data
  - https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-scheduled-function
- [ ] Create website that shows data (with Flask: HTML/CSS/JavaScript)
  - [ ] Show Top 5 (Big), the rest (list)
  - [ ] Able to download data
    - [ ] ALL
    - [ ] By Date
    - [ ] By Date Range
- [ ] Deploy website

## References:

- Create a Flask app: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
- CSS Naming Convention: https://www.freecodecamp.org/news/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849/
- Deploy Flask app: https://docs.render.com/deploy-flask

## Other learning references:

- Add HTML elements to DOM via JavaScript: https://dev.to/dcodeyt/how-to-append-multiple-elements-at-once-in-javascript-dom-39eg
- How to create an API: https://www.moesif.com/blog/technical/api-development/Building-RESTful-API-with-Flask/
