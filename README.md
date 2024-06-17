# Soundboard for Raspberry Pi

Simple project that allows playing chosen audio files to be played on numpad key press


## Default design


## Configuration

Directory where the script will be executed is also it's configuration one. You can select sounds played on certain keys by placing one file in each directory with a coresponding key name. They will be created automaticly if they won't be found, however you'll need to restart the script after that. REMEMBER the file that will be played for each key is the one that appears as the first one while listing coresponding directory. The main file of this project is located is `src` directory and it's called `soundboard_listener.py`. Just run it with regular python interpreter (after installing requirements).

