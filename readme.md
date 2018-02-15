Use python 2.7 to launch this project.

# Installation
Clone the repository in a folder then go in the cloned folder with your terminal.

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cp files/settings.example.yaml files/settings.yaml
    python2 mom/install.py
    python2 main.py

NB: Edit the files/settings.yaml files to adapt database settings.

Mom uses SQLite and support MySQL too. Please use MySQL if you can for better performances.