@echo off
echo Starting Speech-to-Text Application...
echo.

:: Activate the virtual environment
call .\venv\Scripts\activate.bat

:: Run the application
python main.py

:: Deactivate the virtual environment when the application is closed
call deactivate

echo.
echo Application closed.
pause
