@echo off
setlocal

REM This batch file is a simple wrapper to execute the fetch-genesis.py Python script.
REM It passes all command-line arguments to the Python script.

echo Calling the Python script to fetch genesis...

REM Check if a virtual environment exists and activate it.
set "VENV_PYTHON=%~dp0.venv\Scripts\python.exe"
if exist "%VENV_PYTHON%" (
    echo Found virtual environment. Using its Python interpreter.
    "%VENV_PYTHON%" "%~dp0scripts\fetch-genesis.py" %*
) else (
    echo No virtual environment found. Using default 'python' from PATH.
    python "%~dp0scripts\fetch-genesis.py" %*
)

echo.
echo Done.

endlocal
