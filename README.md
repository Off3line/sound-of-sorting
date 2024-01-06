# Sound of Sorting Task for the PLP Assignment 2 from the University of Zurich
The project is also available under [GitHub](https://github.com/Off3line/sound-of-sorting)

## How to run the project
Make sure to have the dependencies from the requirements.txt file. Ideally, you can create a virtual environment folder. 


Run this command to create a venv folder:
``python3 -m venv /path/to/new/virtual/environment``

To activate the virtual environment:
``source <venv>/bin/activate``

Install the dependencies: ``pip install -r requirements.txt``

## Important Info
- On Windows WSL, the audio play somehow did not work due to some bugs reported on WSL itself. However, on Mac (Apple Silicon) and generally Linux the audio should play without any major issues.
- I did not manage to make the sound 100% synchronous to the animation. After many hours of debugging, changing libraries, and making adaptions, the changes did not resolve the issue I was having with playing the sound properly. I intentionally kept the sound feature to show that there is actually one playing according to the compiled bar heights (so the calculation is correct), but the sound sometimes finishes before the animation itself has terminated. I, therefore, added a checkbox to disable or enable to play the sound. The higher the amount of n is, the more delay between the animation and the sound.
- I included more than three different algorithms. They should all be working appropriately. Also, I managed to add some customization features.
- Some of the implementations are built together with Christian, as we both sometimes struggled to find solutions. Hence, we pair-programmed several parts a bit to find a solution that was working for both of us.
- A Ms of below 200ms is not really reliable but still can be used. Anything below will result in a vast difference between audio and video output. Nevertheless, any size of n is acceptable and the algorithm, according to my testing, was always showing the correct visual result.

## Recordings
The recording to show that the application is working can be found inside the folder [/videos](/videos/)


