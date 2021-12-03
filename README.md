# P7_GrandPyBot_OC

This repository contains the code of OpenClassRooms' project 7.

This web application allows you to ask for direction and the bot answers with an address and a bit of trivia about the place.

## Requirements 
- Python 3.8.12
- Git

## Installation

### 1. Change current directory to be where you want the project to be
    cd <future project folder> 
 
### 2. Clone the github project
    git clone https://github.com/Shriukan33/P7_GrandPyBot_OC.git

### 3. Get into the project's folder
    cd P7_GrandPyBot_OC

### 4. Create a virtual environnement (recommended)
    python -m venv venv

### 5. Activate your virtual environnement (if you went through step 4)
#### Windows
    venv/Scripts/activate
#### Linux / MacOS
    . venv/bin/activate

### 6. Install project's depedencies
    pip install -r requirements.txt

### 7. Add FLASK_SECRET_KEY and MAPS_API_KEY to your environnement variables
Any flask secret key will do, as long as it's not null.
You need to provide your own API key for it to work.

Use the following syntax : 
    `export FLASK_SECRET_KEY=MYTOPSECRETKEY`

### 8. Add FLASK_APP and FLASK_ENV to your environnement variables

    export FLASK_APP=main
    export FLASK_ENV=development

### 9. Run flask and go to 127.0.0.1:5000
    cd src/
    flask run

## Use cases
You can then ask (in french !) the bot for an address using the inputfield on the webpage. 
For example : 
![image](https://user-images.githubusercontent.com/70256364/144620082-cb919d04-6f76-4681-9b78-b4e2fbf96624.png)

After a few seconnds of thoughts, the bot comes up with an answer and updates the question, adding some trivia to it. 

![use_case_grandpybot](https://user-images.githubusercontent.com/70256364/144620564-85d82af7-f747-4224-b07d-11b5e0dd3e95.gif)

Also works on mobile : 

![use_case_mobile](https://user-images.githubusercontent.com/70256364/144622254-dc5c258b-77d8-4b8b-91aa-e5bb90ae3539.gif)
