@echo off
cd /d %~dp0\video-emulator
..\miniweb.exe -p 8000 -r .
