### Software and Libraries used:
* [Python v3.7](https://www.python.org/downloads/release/python-377/)
* [OpenCV](https://docs.opencv.org/2.4/doc/tutorials/tutorials.html)
`pip install opencv-python`
`pip install opencv-contrib-python`
* [Numpy](https://numpy.org/doc/stable/)
`pip install numpy`
* [PIL](https://pillow.readthedocs.io/en/stable/)
`pip install Pillow`
* [Sqlite3](https://www.sqlite.org/download.html) :
[Installation](https://www.sqlitetutorial.net/download-install-sqlite/)

##### :heavy_exclamation_mark: Before running the main script `jerry.py` cut the Icon folder(located in GUI folder) and paste it into `/home/pi` directory of raspberry pi(if you are running this project on your pc then change the icons path in script accordingly). Also install the fonts present the Fonts folder.

##### :heavy_exclamation_mark: If you have an error of list index (like out of range), then check names_list.txt file. There must not be any redundant spaces present. Or if there are names that get appended in the same line, mind to keep them in the seperate lines.

### Steps: ###

* Right click in the folder where all the above files are located and click Open in terminal.

* Type `python jerry.py` to run the main script.

* A GUI screen will be opened. This is the Sign Up page where you have to register with your name and user id. Note that User Id can be any no. but this no. must be unique for each person.

![Screenshot](/GUI/GUI_img.png)

* After filling both the fields click on Sign Up button.

* Camera screen will get opened, which will capture the face if face is detected.

* Wait for 1-2 minutes, as the face is being captured and trained.

* After your face model is trained completely, screen will dissappear.

* Now you have to login by clicking `Sign In` button. 

* Camera screen will get Opened and if any trained face appear at screen, login page in GUI will be opened.
 

