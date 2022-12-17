# CS-466-Project-Efficient-Local-Alignment-Algorithms

This repository contains code for our CS466 final project, in which we implemented multiple space efficient algorithms for counting and printing local alignments. In general, there are two ways to use our code:

## 1. Use the test.py file

The program will first ask the user to input two sequences. Then it will compute local alignment information regarding the two sequences, including the optimal score, one single local alignment in linear space, total number of local alignments, and print out all local alignments. Below is a sample output:


<img width="358" alt="Screen Shot 2022-12-17 at 4 22 35 PM" src="https://user-images.githubusercontent.com/22482899/208268030-a233a4c4-df35-4fba-83e2-3574d078b74b.png">

## 2. Use the frontend user interface

We also implemented a web interface with Python Flask framework that the user can easily interact with. To run the code, follow the below command:

1) Install python flask
2) Run the application. If on Windows, type `set FLASK_APP=main.py` and then `flask run`. If on Mac, type export `Flask_APP=main.py` and then `flask run`. </br>
3) The application will be running on `http://127.0.0.1:5000`. Hit the url and interact with the application.

Below is a sample output:

<img width="703" alt="Screen Shot 2022-12-17 at 4 24 05 PM" src="https://user-images.githubusercontent.com/22482899/208268063-d74c944f-4055-43b4-84cd-c2b735fcc370.png">
