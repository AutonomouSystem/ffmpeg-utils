@echo off

rem Check if a file with the name 1.mp4 already exists
if exist "1.mp4" (
    echo A file with the name 1.mp4 already exists in this directory.
    echo Please move or rename the existing file before running this script.
    pause
    goto :eof
)

rem Find the first .mp4 file in the current directory
for %%f in (*.mp4) do (
    rem Rename the file to 1.mp4
    ren "%%f" "1.mp4"
    echo File renamed to 1.mp4
    goto :eof
)

echo No .mp4 files found in the current directory.
pause
