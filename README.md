# Overview

We have a simple web application that consists of two primary components:
- A Front-End UI: A web page where a user can input their name and submit it.
        When the user enters a name and clicks the submit button, the name is sent to a Python-based REST API.
        The page then displays a confirmation message with the submitted name.

- A Python REST API (`app.py`): A simple backend built using Flask that accepts POST requests at the endpoint /submit-name. This API accepts a JSON payload with a name field, processes it, and responds with a confirmation message, e.g., { "message": "Name submitted successfully: <name>" }.

Your task is to demonstrate how you would go about testing both the UI and the API. 

Expected Skills to Assess:

- UI Testing: Familiarity with tools like Selenium, Cypress, or Playwright for testing the web page, form validation, and dynamic content rendering.
- API Testing: Understanding of API testing frameworks such as pytest, requests, or Postman, and experience writing tests for REST endpoints.
- End-to-End Testing: Knowledge of how to combine both UI and API testing to simulate real-world scenarios, such as testing form submissions that hit the API.


# Instructions
This exercise is intended to be 1-1.5 hours in duration. Please complete the following tasks and submit your solution by adding the following github accounts to your forked repository:
- sburkequindar
- zachmeza
- MKLeb

Tasks:
- Get the code running locally 
    - These are simple components, but documentation is sparse and we've introduced a couple minor bugs in each
    - Update the Setup instructions below with steps to run frontend and backend
- Utilizing Playwright (and optionally any additional unit-level or other tests you'd  like to add), set up initial testing in this repository to validate behavior of the frontend and backend (please spend no more than 1 hour on this step)
- Update the Testing section of this README to describe
    - Your approach and instructions for testing this app
    - Next steps you would take to bake tests into CI/CD
    - Any feedback you'd like to give the developers on the components you've been given


# Setup

Documentation is somewhat sparse here intentionally. As you get the components running, please update instructions here wtih an improved set of instructions (and feel free to make updates to the repo itself for cleaner setup!).

## Run the Python app
- You'll need to determine and install dependencies in a virtual environment
- Run the app itself with `python app.py`

## Run the frontend
- You'll need to install npm and run `npm install`
- frontend itself can be run with `http .` if you `npm install -g http-server`


# Testing Approach
Your approach here!