# Bot Or Not by SoWeGoOn

In order to help collect sample data for ChronicCoders AI series, I made this small project which helps create test data.

How it works is that it loads a player in the CSV, then outputs it on the index.html page with graphics and icons. You press "bot" if bot or "not" if its not. 

The idea behind this is that you have a visual idea of each player rather han seeing item IDs which.

## Requirements:
 - Python 3
### Dependancies
 - Flask
 - pandas [to load CSV]
 - requests
 - numpy

## Issues
 - Javascript for the index.html needs to be implemented
 - Backend wont respond for some reason. Gets stuck and then crashes with a SystemExit 3