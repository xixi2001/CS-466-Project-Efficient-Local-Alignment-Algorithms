# CS-466-Project-Efficient-Local-Alignment-Algorithms

This repository contains code for our CS466 final project, in which we implemented multiple space efficient algorithms for counting and printing local alignments. In general, there are two ways to use our code:

## 1. Use the test.py file

The program will first ask the user to input two sequences. Then it will compute local alignment information regarding the two sequences, including the optimal score, one single local alignment in linear space, total number of local alignments, and print out all local alignments.

## 2. Use the frontend user interface

We also implemented a web interface with Python Flask framework that the user can easily interact with. To run the code, follow the below command:

1) Install python flask
2) Run the application. If on Windows, type set FLASK_APP=main.py and then flask run. If on Mac, type export Flask_APP=main.py and then flask run. </br>
3) The application will be running on http://127.0.0.1:5000. Hit the url and interact with the application.


