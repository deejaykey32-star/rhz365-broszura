@echo off
title Generator Broszur A5 - Rozaniec Historii Zbawienia (RHZ365)
cd /d "%~dp0"
echo =====================================================================
echo  ROZANIEC HISTORII ZBAWIENIA (RHZ365) - GENERATOR BROUSZUR A5 & KDP
echo  Serwis: widokinaraj.pl
echo =====================================================================
echo.
echo Uruchamianie serwera aplikacji na http://localhost:3456...
start http://localhost:3456
python server.py
pause
