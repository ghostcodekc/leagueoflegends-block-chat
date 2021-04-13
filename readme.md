# League Of Legends Block Chat

## Description
I would like to know how to appear offline in League of Legends, but when I searched there were very specific examples using the specific IP address for the chat servers at that moment in time. In the League of Legends installation directory there is a `system.yaml` configuration file that sets the chat server for the League of Legends client. This python script will resolve the current League of Legends chat server IP address and add it to your local firewall rule to block that functionality. 

## Prerequisites
Python Version 3.9

Ensure running scripts on your machine is enabled:
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

Make sure pip is upgraded:
- python -m pip install --upgrade pip

Install venv:
- python -m pip install --user virtualenv

create virtual environment:
- python -m venv lol-block-chat

Activate virtual environment:
- .\lol-block-chat\Scripts\Activate.ps1

Install requrements:
- pip install -r requirements.txt

## Instructions
- Edit the config file for your League of Legends installation directory.
- Edit the config file for your region.
- Enable / Disable chat firewall rule in the config file by setting the `block_chat` setting. 
    - 0 = Disable / 1 = Enable 

## Running the Python Script
`python main.py`