@echo off
:: original idea from tens, fake-upscaling to 4k for better YouTube codec
:: check if a file with the name output.mp4 exists
if not exist "output.mp4" (
    echo File output.mp4 not found in the current directory.
    pause
    goto :eof
)

::  run the FFmpeg command
:: "C:\ProgramData\chocolatey\bin\ffmpeg.exe" -i output.mp4 -vf scale=3840:2160:flags=lanczos -c:a copy -c:v hevc_nvenc -preset slow -rc vbr -b:v 400M -cq 1 upscale.mp4

:: crf 17, 120fps, libx265
::"C:\ProgramData\chocolatey\bin\ffmpeg.exe" -i output.mp4 -c:v libx265 -preset slower -crf 17 -r 120 -vf scale=3840x2160:flags=lanczos -pix_fmt yuv420p upscale.mp4

:: nvenc test, 120fps, h.265
"C:\ProgramData\chocolatey\bin\ffmpeg.exe" -i output.mp4 -c:v hevc_nvenc -preset slow -rc vbr -cq 19 -r 120 -s 3840x2160 -pix_fmt yuv420p upscale.mp4

:: alternate methods
:: C:\ProgramData\chocolatey\bin\ffmpeg.exe -i input.mp4 -vf scale=3840:2160:flags=neighbor -r 60 -rc constqp -qp 19 -c:a copy output.mp4
:: libx264 (H.264)
:: ffmpeg -i output.mp4 -c:v libx264 -preset slow -crf 18 -r 120 -s 3840x2160 -pix_fmt yuv420p upscale.mp4
:: libx265 (H.265/HEVC)
:: ffmpeg -i output.mp4 -c:v libx265 -preset slow -crf 20 -r 120 -s 3840x2160 -pix_fmt yuv420p upscale.mp4
:: libvpx-vp9 (VP9)
:: ffmpeg -i output.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 -r 120 -s 3840x2160 -pix_fmt yuv420p upscale.webm
:: nvenc (H.264)
:: ffmpeg -i output.mp4 -c:v h264_nvenc -preset slow -rc vbr -cq 19 -r 120 -s 3840x2160 -pix_fmt yuv420p upscale.mp4
:: nvec (H.265)
:: ffmpeg -i output.mp4 -c:v hevc_nvenc -preset slow -rc vbr -cq 19 -r 120 -s 3840x2160 -pix_fmt yuv420p upscale.mp4

rem display the error level (0 means success, non-zero means failure)
echo Error level: %ERRORLEVEL%

rem pause the script execution to allow viewing the error message
pause
