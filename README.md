# Spotify Top 50 Songs - Philippines [Data]

## Project Overview

- Collect data from a Spotify playlist and store in a data warehouse.
- Playlist: https://open.spotify.com/playlist/37i9dQZEVXbNBz9cRCSFkY
- Sync daily or weekly?

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
      - [ ] Re-check types of data before adding to final table
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
