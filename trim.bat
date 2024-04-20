@echo off

rem check if 1.mp4 exists in the current directory
if not exist "1.mp4" (
    echo File 1.mp4 not found in the current directory.
    pause
    goto :eof
)

rem start timestamp
set /p start_time="Enter start timestamp (e.g., 00:02:13): "

rem end timestamp
set /p end_time="Enter end timestamp (e.g., 00:02:52): "

rem ask time stamps
rem ffmpeg -i 1.mp4 -ss %start_time% -to %end_time% -c:v copy -c:a copy -force_key_frames "00:00:00.000" 2.mp4

ffmpeg -i 1.mp4 -ss %start_time% -to %end_time% -c:v libx264 -c:a aac -strict -2 2.mp4
rem ffmpeg -i 1.mp4 -ss %start_time% -to %end_time% -c:v copy -c:a copy -avoid_negative_ts make_zero 2.mp4

rem ffmpeg -i 1.mp4 -ss %start_time% -to %end_time% -c:v libx265 -c:a libopus -strict -2 2.mp4

rem display the error level (0 means success, non-zero means failure)
echo Error level: %ERRORLEVEL%

rem
pause
