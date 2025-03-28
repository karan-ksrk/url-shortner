## Running the URL Shortener App
Before running the project, ensure the following setup:

1. **For Local Development**:
    - Create a `.env` file in the root directory of the project.
    - Add the following environment variables:
      ```
      DATABASE_URL=<your_database_url>
      POSTGRES_USER=<your_postgres_user>
      POSTGRES_PASSWORD=<your_postgres_password>
      POSTGRES_DB=<your_postgres_db>
      ```
    - Spin up any PostgreSQL server and configure it using the above variables.

2. **For Docker**:
    - Create a `.env.compose` file in the root directory of the project.
    - Add the following environment variables:
      ```
      DATABASE_URL=<your_database_url>
      POSTGRES_USER=<your_postgres_user>
      POSTGRES_PASSWORD=<your_postgres_password>
      POSTGRES_DB=<your_postgres_db>
      ```
      
To run the URL Shortener application using Docker, execute the following command:

```bash
docker-compose up --watch
```

This will start the application and monitor for changes.



