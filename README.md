# GeniePrep Post UTME Practise APP (web) 
![Bootstrap-5.1.0](https://img.shields.io/badge/Bootstrap-5.1.0-blue "Bootstrap-5.1.0")
![Django==3.1.4](https://img.shields.io/badge/Django-3.1.4-green "Django==3.1.4")

![JQuery](https://img.shields.io/badge/JQuery-2.2.4-yellow "JQuery-2.2.4")

> An Online Web Based Post Utme Practise APP
> This version is specifically for FEDRAL UNIVERSITY OF TECHNOLOGY(FUTA) Aspirants
<hr>


# Table of Contents
* [Introduction](#Introduction)
* [Setup](#Setup)
* [Testing Practise](#Testing)
* [How it works](#How-it-works)
* [Upcoming improvements](#Upcoming-improvements)
<hr>

## Introduction
This web application offers an online Post UTME practise. It was built to give the visual effect for Aspirants using the app to practise for FUTA post UTME. This are what it can do:

  * `Register/Login/Logout` > you can create an account on the app, and it will keep records of your practise.

  * `Practise` > you can take live test, set your question range, set time, and start the test right away.

  * `Instant Marking and Result`  > As soon as you push the submit button during test, the app marks it instantly, shoe you your result, and correction.
  
  Note: You always have to fill every field during the practise setup to avoid errors, also your browser must be cookie eneabled for better and smooth experience.

## Setup
<hr>
1. _[required]_ Install the requirements file by doing ```python -m pip install -r requirements.txt```
2. _[optional]_ During production, it is advisable to set Django module setting in your enviroment variable `.env` file to production as explained in the [configuration section](Configuration Variables) but can be skipped during testing as the default will be in development.

3. _[required]_ start the app by running ```python manage.py runserver``` at the console.

# How it Works


####  Genie User

* When a user visits the page, user must login, or register, which is neccessary.
* The user is then directed to the dashboard, where all the navigations, past practise records, and so on is.

####  Genie Practise

* When a user clicks the `Take Practise Test` button
* He/she is directed to the practise setup page, select subjects, fills the `from` which is the start question number and `to` which is the stop question number, set the `duration` and clicks the continue button.
* Read instructions and press the start button, Make sure you have an internet connection at least when you are about to submit.



## Marking And Scoring

<hr>
The App has an answer data set into it, which is used as the marking guide for every test submit. After marking then the app records it to the database and redirects to the result page.

The app follows the real-life model of examination.
<hr>

## Configuration Parameters

The following are the configuration of `Environment variables`.

Note: You'll have to create an `.env` file in the same directory with this readme file.


Variable  | Type / Default | Description
---------- | - | -------
DJANGO_SETTINGS_MODULE | String of project's mode (either `GeniePrep.settings.development` or `GeniePrep.settings.production`. defaults to  `GeniePrep.settings.development`) | The settings of this app is splitted into development and production, on seperate concerns, (Debug, Database, e.t.c).files are located at `GeniePrep.settings` directory.
SECRET_KEY | String offered by  django project | App Secret key required for the application to work :).

<hr>

## Upcoming Improvements
(An evolving list)
* Question Integration.
* Inclusion of Other Schools, so Other school aspirants can Pratise with Genie Prep.
* Any further progress on this project, will be implemented and will reflect in this ReadMe file :).
