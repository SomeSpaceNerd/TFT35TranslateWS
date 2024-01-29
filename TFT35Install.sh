echo TFT35Translate install script by Wil-Sys https://github.com/wil-sys
echo TFT35Translate Creating python Virtual Enviroment...
python -m venv venv
echo TFT35Translate installing python dependancies...
venv/bin/pip install pyserial
venv/bin/pip install requests
venv/bin/pip install gpiozero
venv/bin/pip install websockets
echo TFT35Translate Starting main program...
venv/bin/python3 TFT35.py

