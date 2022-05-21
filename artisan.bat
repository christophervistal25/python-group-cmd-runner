@ECHO OFF
set arg1=%1
cd C:\laragon\www\facial-recog-api
php -S %arg1%:8000 -t public
PAUSE