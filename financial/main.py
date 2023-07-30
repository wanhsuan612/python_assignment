from fastapi import FastAPI

from financial.routers import router


app = FastAPI(
    title="Python Assignment",
    description="""This project is designed to retrieve and manage financial data for specific stocks (IBM, Apple Inc.) using the [AlphaVantage](https://www.alphavantage.co/documentation/) API. It provides functionality to fetch the recent two weeks of financial data, process and store it in a local database, and offers API endpoints to retrieve records and perform statistical calculations on the stored data. The APIs are implemented using `FastAPI`, enabling a fast and robust interface.""",
)  # Define app
app.include_router(router)  # include sub routers
