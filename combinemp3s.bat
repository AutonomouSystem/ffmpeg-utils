@echo off
:: combine mp3s into one-file to merge into videos
:: set the initial file number
set "count=1"

:: create a text file to store the list of input files
(
    echo This is a dummy line to keep the concat.txt file non-empty.
)> concat.txt

:loop
if exist "%count%.mp3" (
    echo file '%cd%\%count%.mp3' >> concat.txt
    set /a "count+=1"
    goto :loop
)

:: remove the dummy line from concat.txt
setlocal enabledelayedexpansion
for /f "usebackq delims=" %%a in ("concat.txt") do (
    set "line=%%a"
    if not "!line!"=="This is a dummy line to keep the concat.txt file non-empty." (
        echo !line! >> temp.txt
    )
)
move /y temp.txt concat.txt
endlocal

:: combine the MP3 files into a single file
ffmpeg -f concat -safe 0 -i concat.txt -c copy combined.mp3

:: clean up the temporary file
del concat.txt
