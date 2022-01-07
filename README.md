# GenshinArtifactHelper
A python script to automatically asses Genshin Impact artifacts to see which ones are worth keeping.

!!!!!!!!!
!!!!!!!!!
Just noticed that it crashes if it encounters an artifact with less than 4 substats. I will fix this later.
!!!!!!!!!
!!!!!!!!!

Takes input in the form of a JSON file formatted using the Genshin Open Object Description (GOOD) format. More info about the format can be found here:
https://frzyc.github.io/genshin-optimizer/#/doc/

Evaluates each artifact in the file based on set and stats and gives it a score for each character. The scores are based on the information in this document (Community Character Builder by the Genshin Helper Team):
https://docs.google.com/spreadsheets/d/1gNxZ2xab1J6o1TuNVWMeLOZ7TPOqrsf3SshP5DLvKzI/pubhtml?gid=100510092#


Requires Python 3.10 or later to run.
A small test file (TestData.json) containing some data in the GOOD format is included for testing purposes. In order to generate your own list of artifacts I recommend "AdeptiScanner-GI", which can be found here:
https://github.com/D1firehail/AdeptiScanner-GI


The script is a complete mess, but this is mostly a learning exercise for me to learn Python, JSON and programming in general.
