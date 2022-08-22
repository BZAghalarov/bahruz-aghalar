# Public Transportation Scheduling Coding Challenge

# Goals/Outcomes
- To test knowledge of building RESTful APIs
- Data modeling and schema design
- Basic understanding and knowledge about backend application hosting

# Pre-requisites
- Download [Hudson Link](https://www.ridehudsonlink.com) public transit dataset package from the official site [511ny.org](https://s3.amazonaws.com/datatools-511ny/public/Hudson_Link.zip) 
- Basic understanding of the de facto Public Transit Scheduling data format - [General Transit Feed Specification](https://en.wikipedia.org/wiki/General_Transit_Feed_Specification) (aka GTFS). See https://gtfs.org for more information.


# Requirements
- Design an entity relation database schema with all necessary tables to map out the relevant data sets in the GTFS package downloaded above. Load the dataset into the database
- Alternatively, load and access the CSV dataset in memory is also acceptable. Please present the design considerations and tradeoffs if you do take this approach.
- Build a simple public transit service RESTful API web application using Python version 3.8 or 3.9 and a common web framework, e.g. Flask, Django.
- The application can be run standalone with framework's building web server or dockerized to be run in Docker Compose locally.
- Bonus points for publish the application in one of the Serverless Cloud Platforms, e.g. Google App Engine, Heroku etc.
- The web application should provide at least one RESTful API service endpoint. The endpoint will take the following parameters, e.g. 
  - Latitude / longitude coordinates that represents where you are, which may or may not be exactly by a public transit stop; this is optional if origin stop ID is given.
  - Closest origin stop ID from where you are; this is optional if latitude / longitude pair is given.
  - Closest destination stop ID to where you want to be.
  ```json
  {"origin_station_id": "TARRYT", "coordinates": {"latitude": "41.066627185831244", "longitude": "-73.8630597690967"}, "destination_station_id": "ARFRN"}
  ```
- The REST API service endpoint will return a JSON response with the upcoming public transit services from origin stop to destination stop and each of their scheduled origin stop arrival time and destination stop arrival time. If there are more than 5 public transit service schedules available, please adding a result set pagination filter, e.g.
  ```json
  {"next_schedules":[{"route_short_name": "H01X", "arrival_time":"2021-11-19 19:19:09"}, {"route_short_name": "H01", "arrival_time":"2021-11-19 19:54:13"},{"route_short_name": "H01", "arrival_time": "2021-11-19 20:50:09"}], "pagination": {"limit": 3, "offset": 0, "order": "asc", "total": 3}}
  ```
- Documentation should be provided to explain how to run the application and basic deployment instructions (if necessary, e.g. containerization, serverless deployment etc.)
- The REST API service should provide typical HTTP response codes, HTTP 200 for available routes round, HTTP 404 for routes not available (within range of 10 miles), HTTP 400 for invalid data input.
- Bonus points for integrating Geocoding APIs (e.g. Google Maps, Mapbox or OpenStreetMaps) to find the closest origin stop to where you are, given a pair of lat/lon coordinates.
- Bonus points for providing unit tests with mock data set.

# FAQ
- Time limit? Do not spend more than 4 hours.
- What to do after code completion? Please submit a Merge Request(MR) to this repo for a code review.
- Have any other questions? Please ask away, reaching out via email. Thanks.


