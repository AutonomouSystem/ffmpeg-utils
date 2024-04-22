@echo off

rem check if a file with the name output.mp4 exists
if not exist "output.mp4" (
    echo File output.mp4 not found in the current directory.
    pause
    goto :eof
)

rem run the FFmpeg command
"C:\ProgramData\chocolatey\bin\ffmpeg.exe" -i output.mp4 -vf scale=3840:2160:flags=lanczos -c:a copy -c:v hevc_nvenc -preset slow -rc vbr -b:v 400M -cq 1 upscale.mp4


rem C:\ffmpeg\bin\ffmpeg.exe -i input.mp4 -vf scale=3840:2160:flags=neighbor -r 60 -rc constqp -qp 19 -c:a copy output.mp4

rem display the error level (0 means success, non-zero means failure)
echo Error level: %ERRORLEVEL%

rem pause the script execution to allow viewing the error message
pause
