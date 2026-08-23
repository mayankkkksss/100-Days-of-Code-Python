# Day 38 - Workout Tracking

This project was created as part of **100 Days of Code: The Complete Python Pro Bootcamp** by **Angela Yu**.

## About the Project

The goal of this project is to build a **Workout Tracking application** that converts natural-language exercise descriptions into structured workout data.

The project uses the **Nutritionix API** to process exercise information and calculate details such as the exercise name, duration, and calories burned.

The resulting workout data is then sent to a **Google Sheet through the Sheety API**, allowing the workout history to be stored and tracked.

## How It Works

The application follows this basic workflow:

```text
User enters exercise
        ↓
Nutritionix API
        ↓
Exercise information
        ↓
Calories & duration
        ↓
Sheety API
        ↓
Google Sheet
```

For example, a user can enter an exercise in natural language, and the application uses the Nutritionix API to determine the corresponding exercise information.

The application then sends that information to the configured Google Sheet using Sheety.

## Features

* Accepts natural-language exercise descriptions
* Detects exercise type
* Calculates exercise duration
* Calculates calories burned
* Records workout information
* Stores workout data in a Google Sheet
* Adds the current date and time to workout entries

## Technologies Used

* Python
* Requests
* Nutritionix API
* Sheety API
* Google Sheets
* REST APIs
* JSON

## Concepts Practiced

* Working with multiple APIs
* Making HTTP `POST` requests
* Sending JSON data
* Working with API authentication
* Reading API documentation
* Handling API responses
* Working with dates and times
* Connecting Python applications to external services

## Project Structure

```text
Day-38-Workout-Tracking/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## API Configuration

This project requires API credentials for the services used by the application, including:

* Nutritionix API
* Sheety API

The project uses **environment variables** to keep API credentials out of the source code.

Before running the project, create the required environment variables and replace the placeholder values with **your own API credentials**.

For example:

```text
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
SHEETY_AUTHENTICATION=your_sheety_authentication
```

The variable names must match those used in `main.py`.

Create your own accounts/API credentials and replace the placeholder values with your own.

## Running the Project

Run:

```bash
python main.py
```

Enter the exercise information when prompted.

The application will process the input through the Nutritionix API and add the resulting workout information to the configured Google Sheet through Sheety.

## What I Learned

This project gave me practical experience working with multiple APIs in a single Python application.

I learned how to:

* Work with API documentation
* Connect Python to external services
* Send and receive JSON data
* Use authentication headers
* Make `POST` requests
* Process API responses
* Work with dates and times
* Connect Python applications with Google Sheets

## Course

**100 Days of Code: The Complete Python Pro Bootcamp**

Instructor: **Angela Yu**

Day: **38 / 100**

**This README.md is AI-generated; perception are not.**
