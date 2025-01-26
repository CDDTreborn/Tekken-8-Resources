@echo off
REM ------------------------------------------------------------------
REM  RenameWithP.bat
REM  This batch file:
REM    1) Prompts for a directory path (removes pasted quotes).
REM    2) Prompts for a file pattern, defaults to *.pak *.utoc *.ucas if blank.
REM    3) Recursively renames each matching file by adding "_P" before the extension,
REM       unless the file already ends with "_P" before the extension.
REM ------------------------------------------------------------------

:: Enable delayed variable expansion
setlocal enabledelayedexpansion

REM Prompt user for the target directory
echo Please enter the full path of the directory containing the files you want to rename:
set /p "targetDir=Directory Path: "

REM Remove any double quotes from the directory path (handles copy/paste with quotes)
set "targetDir=%targetDir:"=%"

REM Check if the directory exists
if not exist "%targetDir%" (
    echo ERROR: The specified directory does not exist: "%targetDir%"
    pause
    exit /b
)

echo.
echo Processing directory: "%targetDir%"
echo.

REM Prompt for file pattern
echo Please specify the file pattern(s) to rename (e.g. *.txt, *.jpg).
echo To use default patterns (*.pak, *.utoc, *.ucas), just press Enter.
set /p "filePattern=Pattern: "

REM If user did not enter anything, default to *.pak *.utoc *.ucas
if "%filePattern%"=="" (
    set "filePattern=*.pak *.utoc *.ucas"
)

echo Renaming files matching: %filePattern%
echo.

REM Use FOR /R to iterate through all subdirectories
for /R "%targetDir%" %%F in (%filePattern%) do (
    REM Extract filename (without extension) and extension
    set "name=%%~nF"
    set "ext=%%~xF"
    set "fullPath=%%~dpF"
    
    REM Check if the filename (without extension) already ends with _P
    if /i "!name:~-2!"=="_P" (
        echo Skipping "%%F" because it already ends with _P.
    ) else (
        REM Construct the new filename
        set "newName=!name!_P!ext!"
        REM Rename the file
        ren "%%F" "!newName!"
        echo Renamed "%%F" to "!newName!"
    )
)

echo.
echo Done! The matching files have been renamed to include "_P" (unless they already had it).
pause
exit /b
