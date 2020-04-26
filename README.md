# Bot Or Not by SoWeGoOn

In order to help collect sample data for ChronicCoders AI series, I made this small project which helps create test data.

How it works is that it loads a player in the CSV, then outputs it on the index.html page with graphics and icons. You press "bot" if bot or "not" if its not. 

The idea behind this is that you have a visual idea of each player rather han seeing item IDs which.

## Start The Server
To start it, open up a console and navigate to the folder that this respitory has been cloned too. Then type:
```
python server.py
```
If you have a Linux system or have multiple versions of Python, you may need to type:
```
python3 server.py
```

## Requirements:
 - Python 3
### Dependancies
 - Flask
 - pandas [to load CSV]
 - requests
 - numpy
