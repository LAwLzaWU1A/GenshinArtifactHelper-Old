# GenshinArtifactHelper
A python script to automatically asses Genshin Impact artifacts to see which ones are worth keeping.


#What does it do?
This script takes a JSON file formatted using the [Genshin Open Object Description (GOOD) format](https://frzyc.github.io/genshin-optimizer/#/doc/).

It then evaluates each artifact based on the set and stats, gives it a score for each character and then writes the result to a file called "ArtifactResults.txt".
The scores are based on the information in this document [Community Character Builder by the Genshin Helper Team](https://docs.google.com/spreadsheets/d/1gNxZ2xab1J6o1TuNVWMeLOZ7TPOqrsf3SshP5DLvKzI/pubhtml?gid=100510092#) as of January 5 2022.


#Why would I want to use this?
Right now, I got over 1300 artifacts in my inventory. Going through each and every one manually would not only take A LOT of time, but it would also leave room for human error. An artifact that I think looks bad might be good for some character I don't know a lot about. If I am only familiar with Diluc builds, I might think a Crimson Witch artifact with HP is bad even thought it's great for Hu Tao.


#How to Use This Script
First, download the script from this page. I have included a small test file (TestData.json) containing some data in the GOOD format is included for testing purposes.
Then, obtain a list of artifacts you currently got formatted in the GOOD format. I recommend using ["AdeptiScanner-GI"](https://github.com/D1firehail/AdeptiScanner-GI) which automatically scans your inventory.
Once you got the script and the list of artifacts, run the script with the artifact file as an argument. For example:
`python.exe .\GenshinArtifactChecker.py .\TestData.json`
After the script is done executing, open the "ArtifactResults.txt" file. That file contains a list of all artifacts which has a score of 2155 or higher, which is what I would consider good enough to keep.


#Requirements
Requires Python 3.10 or later to run.
Make sure your python environment is 3.10 or later, or else the script will not work.


#Disclaimer
The script is a complete mess, but this is mostly a learning exercise for me to learn Python, JSON and programming in general.
This script does not directly interact with Genshin Impact in any way (although AdeptiScanner does) and as a result it should be completely harmless to your GI account and your PC. However, I am not responsible for any "damage" done to your account, such as the script by mistake labeling a good artifact as bad, causing you to delete it. Use this at your own risk.


#Future Improvements
Because this is my first "major" script, and I am very inexperienced as a developer, there are a lot of room for improvement. For example I want to move away from having the score and characters tied to a specific index in a list. I would also like to rework the script so that there is a central database with characters and which stats they prefer, rather than static "if X, then add score to this character".

Feel free to reach out if you want to help with this project.
