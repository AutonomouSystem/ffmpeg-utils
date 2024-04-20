@echo off

rem Check if a file with the name 1.mp4 exists
if not exist "1.mp4" (
    echo File 1.mp4 not found in the current directory.
    pause
    goto :eof
)

rem Run the FFmpeg command
"C:\ffmpeg\bin\ffmpeg.exe" -i 1.mp4 -vf scale=3840:2160:flags=lanczos -c:a copy -c:v hevc_nvenc -preset slow -rc vbr -b:v 400M -cq 1 2.mp4

rem Display the error level (0 means success, non-zero means failure)
echo Error level: %ERRORLEVEL%

rem Pause the script execution to allow viewing the error message
pause