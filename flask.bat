@ECHO OFF
set arg1=%1
cd C:\Users\CHRis\Desktop\compreface-sdk-py
flask run --host=%arg1% --port=8001
PAUSE