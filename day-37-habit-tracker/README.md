# Day 37 - Habit Tracker

This project was created as part of **100 Days of Code: The Complete Python Pro Bootcamp** by **Angela Yu**.

## About the Project

The goal of this project is to build a simple **Habit Tracker** using the **Pixela API**.

The program allows you to create a graph and record daily values to track a habit over time. In this project, I used HTTP requests from Python to communicate with the Pixela API.

## Features

* Create a Pixela user account
* Create a graph for tracking a habit
* Add daily data to the graph
* Update existing data
* Delete data from the graph

## Technologies Used

* Python
* Requests
* REST API
* Pixela API
* JSON
* HTTP requests

## Concepts Practiced

* Making API requests with Python
* Working with REST APIs
* Using `GET`, `POST`, `PUT`, and `DELETE` requests
* Sending request headers and parameters
* Working with JSON data
* Handling API authentication
* Using API endpoints

## Project Structure

```text
Day-37-Habit-Tracker/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and navigate to this project folder.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## API Configuration

This project requires a **Pixela API username and token**.

The project uses environment variables to keep API credentials out of the source code.

Before running the project, create the required environment variables and replace the placeholder values with **your own Pixela credentials**.

Example:

```text
USERNAME=your_pixela_username
TOKEN=your_pixela_token
```

Create your own Pixela account and generate your own token.

## Running the Project

Run the following command:

```bash
python main.py
```

The program will communicate with the Pixela API and perform the requested habit-tracking operations.

## What I Learned

This project helped me understand how applications communicate with external services through APIs.

I also learned how to:

* Read API documentation
* Construct API endpoints
* Send different types of HTTP requests
* Pass data using parameters and JSON
* Authenticate API requests
* Work with responses from external APIs

## Course

**100 Days of Code: The Complete Python Pro Bootcamp**

Instructor: **Angela Yu**

Day: **37 / 100**

**This README.md is AI-generated; perception are not.**
