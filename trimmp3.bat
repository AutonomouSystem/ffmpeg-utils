@echo off
:: trim .mp3s to custom timestmaps
rem check if 1.mp3 exists in the current directory
if not exist "1.mp3" (
    echo File 1.mp3 not found in the current directory.
    pause
    goto :eof
)

rem start timestamp
set /p start_time="Enter start timestamp (e.g., 00:25:02): "

rem end timestamp
set /p end_time="Enter end timestamp (e.g., 00:29:40): "

rem trim the audio
ffmpeg -i 1.mp3 -ss %start_time% -to %end_time% -c:v copy -c:a copy 2.mp3

rem display the error level (0 means success, non-zero means failure)
echo Error level: %ERRORLEVEL%

rem pause on error
pause
