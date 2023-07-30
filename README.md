# Project Description

This project is designed to retrieve and manage financial data for specific stocks (IBM, Apple Inc.) using the [AlphaVantage](https://www.alphavantage.co/documentation/) API. It provides functionality to fetch the recent two weeks of financial data, process and store it in a local database, and offers API endpoints to retrieve records and perform statistical calculations on the stored data. The APIs are implemented using `FastAPI`, enabling a fast and robust interface.

### Project Structure of API

```php
.
├── Dockerfile            // Contains the Docker configuration for building the project's container.
├── README-1.md
├── README.md             // This file contains all the information about the project.
├── bin
│   ├── db
│   │   └── set-permissions.sh
│   └── financial
│       └── entrypoint.sh
├── docker-compose.yml    // Defines and runs the multi-container Docker applications.
├── financial             // This is the core api module for financial operations. Inside it, you'll find:
│   ├── config            // Configuration files, such as database connection settings.
│   │   └── database.py
│   ├── main.py           // The entry point for the FastAPI application.
│   ├── models            // Defines SQLAlchemy ORM models.
│   │   └── financial_data.py
│   ├── routers           // Handles API routes and endpoints.
│   │   ├── __init__.py
│   │   ├── financial_data.py
│   │   └── statistic.py
│   ├── services          // Interaction with the database and further calculations on data.
│   │   ├── financial_data.py
│   │   └── statistics.py
│   ├── types             // Includes the type definitions and response schemas for the API.
│   │   ├── financial_data.py
│   │   ├── pagination.py
│   │   ├── response.py
│   │   └── statistic.py
│   └── utils             // A collection of utility functions and exception handling.
│       ├── common.py
│       └── exceptions.py
├── get_raw_data.py       // A script to seed the database with initial data of app.
├── pyproject.toml        // Defines the linter's configuration.
├── requirements.txt      // Lists the required Python packages for the project.
└── schema.sql            // Contains the SQL schema definition for the project
```

## Tech Stack

- **API Framework:** FastAPI
   - The fastest framework for building APIs with Python
   - Automatically create Swagger documents
   - Friendly document and resources
- **Database:** MariaDB
   - Familiar with MySQL but the performance of MariaDB is better
   - Open-source
- **Containerization:** Docker
- **Libraries:**
   - SQLAlchemy: ORM recommended by FastAPI
   - Uvicorn: Fast web server recommended by FastAPI
- **Coding Style:** PEP8(Autoformated by isort, black), Google Style Docstring

## Running the Code in Local Environment

Follow these steps to set up and run the project in your local environment:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/wanhsuan612/python_assignment
   ```

2. **Navigate to Project Directory:**
   ```bash
   cd python-assignment
   ```
1. **Set .env:**

   Please refer .env.example to build a `.env` at the root of project folder.

3. **Build and Start the Docker Containers:**
   ```bash
   docker compose up
   ```

4. **Access the FastAPI Documentation:**

   Open your web browser and navigate to `http://localhost:5000/docs`.

## How to managing the AlphaVantage API Key


### Local Development

1. Create a file named `.env` in the project root directory by respecting `.env.example`.
2. Make sure ignoring the `.env` file in .gitignore

### Production Environment

#### Kubernetes Secrets

If deploying in a Kubernetes cluster, you can use Kubernetes Secrets to store the API key.

1. Create a secret containing your AlphaVantage API key
2. Reference the secret in your Kubernetes deployment configuration

#### Git Repository Group's Variables

If you prefer to manage the API key within your Git repository, you can use group's variables and masking, provided that your Git platform supports this feature (e.g., GitLab).
