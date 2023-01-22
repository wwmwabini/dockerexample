# About

This is a simple app used for to practice docker.

It consists of 3 apps:
- register - displays a form that allows entry of a name and email. This gets saved on a database in the backend
- users - displays all data saved from register app
- backend database - mysql, postgre or oracle

# Database set up
The register and users app are build from their respective Dockerfiles. As for the database, which requires persistance, you would need to change the docker-compose file to match your database. The database name for this to work is dockerexample. The username is also dockerexample. The password and host are passed as environment variables - DB_PASS and DB_HOST respectively.

The docker-compose file provided runs the the app above using MySQL by default.