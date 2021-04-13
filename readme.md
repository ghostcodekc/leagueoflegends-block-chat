# League Of Legends Block Chat

## Prerequisites
Python Version 3.9

Ensure running scripts on your machine is enabled:
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

Make sure pip is upgraded:
- python -m pip install --upgrade pip

Install venv:
- py -m pip install --user virtualenv

create virtual environment:
- -m venv lol-block-chat

Activate virtual environment:
- .\lol-block-chat\Scripts\Activate.ps1

## Instructions
- Edit the config file for your League of Legends installation directory.
- Edit the config file for your region.
- Enable / Disable chat firewall rule in the config file by setting the 'block_chat' setting. 
    - 0 = Disable / 1 = Enable 
