# Country Capital Quiz

A Python quiz application that uses a country/capital API to generate True or False questions.

The project was built using Python, Tkinter, OOP, API requests, and a multi-file project architecture.

---

## Features

* Fetches country and capital data from an external API
* Cleans and prepares API data for the quiz
* Generates True / False country-capital questions
* Randomizes question order
* Creates both correct and incorrect capital questions
* Prevents multiple fast clicks on answer buttons
* Tracks and displays the current score
* Shows visual feedback with green/red canvas color
* Uses a Tkinter graphical user interface
* Separates the project into multiple Python files using OOP

---

## What I practiced

* Working with APIs using `requests`
* Using `response.json()` to convert API data into Python data structures
* Cleaning raw API data before using it in the application
* Creating custom classes with OOP
* Building a question model class
* Creating a quiz brain class for logic and scoring
* Passing objects between files
* Using `random.choice()` and `random.shuffle()`
* Building a Tkinter user interface
* Using buttons, labels, canvas, images, and `after()`
* Preventing repeated button clicks during UI feedback
* Structuring a Python project across multiple files

---

## Project structure

```text
Country-Capital-Quiz/
├── main.py
├── data.py
├── country_model.py
├── quiz_brain.py
├── ui.py
├── images/
│   ├── true.png
│   └── false.png
├── README.md
└── .gitignore
```

---

## How to run

Run the project with:

```bash
python main.py
```

---

## Technologies used

* Python
* Tkinter
* Requests
* REST API
* OOP
* Random module
* Git / GitHub

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

The original course project was a Quiz API application. This version was rebuilt as a separate custom project using country and capital data from an API, with a similar architecture but different logic and topic.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.
