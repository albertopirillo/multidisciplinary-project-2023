# Intersection
Project for the course **Multidisciplinary Project** in the academic year 2022-2023 at Politecnico di Milano, made by:
- Alberto Noris ([@AlbertoNoris](https://github.com/AlbertoNoris))
- Nicole Perrotta ([@NicolePerrotta](https://github.com/NicolePerrotta))
- Alberto Pirillo ([@albertopirillo](https://github.com/albertopirillo))
- Andrea Sinisi ([@AndreaSinisi](https://github.com/AndreaSinisi))
  
Supervised by Dario Chiossi (dario.chiossi@gmail.com).

## Description
This repository contains the source code for a website that leverages Artificial Intelligence to match workers and companies. The goal is to facilitate the process of connecting job seekers with suitable job opportunities. 

## Features
- **Worker Profile Creation**: workers can create profiles by uploading their CVs and providing personal information such as their gender, birth date, or the country they come from
- **Company Profile Creation**: companies can create profiles by providing information such as the country they come from or their description
- **Job Offer Posting**: companies can post job offers, specifying the salary, the duration, and the job description
- **AI Matching Algorithm**: the website relies on an AI model to analyze worker CVs and job offers, providing personalized recommendations and identifying potential matches based on skills, experience, and other factors
- **Interactive Interface**: the website offers a user-friendly interface, allowing workers to browse and apply for job opportunities, and companies to review worker profiles and select suitable candidates
- **List of Job Offers**: workers can view job offers ranked according to their relevance as computed by the AI model, while companies can access a ranked list of applications to their job offers, also determined by the AI model

## Technologies Used
The website was built using the following technologies:
- **Front-end:** HTML, CSS, JavaScript, Bootstrap
- **Back-end:** PHP, Python libraries (FastAPI, pdfplumber, SQLAlchemy, PyTorch, and Poetry)
- **AI Model:** Transformer-based Bi-encoder (Reimers & Gurevych, 2019)
- **Database:** PostgreSQL
- **Deployment:** Railway

## Setup and Configuration
To set up the website locally, follow these steps:
- Clone the repository to your local machine
- Set up a web server environment (such as Visual Studio Code) and configure it to run PHP
- Import the database schema
- Configure the database connection settings in the appropriate PHP files
- Set up and configure the API:
    - Install Python 3.9 and Poetry
    - In the folder "AI Algorithm" run the command `poetry install`
    - Update the API address with the local one in the back-end pages
    - In the folder "AI Algorithm" run the command `uvicorn api:app` to run the API
- Start the web server and access the website through a web browser

## License
Licensed under [MIT License](LICENSE).

___

If you have any questions or suggestions regarding the website or the repository, please feel free to contact the contributors.

We appreciate your interest in the project!
