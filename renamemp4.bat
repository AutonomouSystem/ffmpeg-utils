@echo off
setlocal enabledelayedexpansion

set "count=1"

rem Loop through all the .mp4 files in the current directory
for %%f in (*.mp4) do (
    rem Check if a file with the current count already exists
    if exist "!count!.mp4" (
        echo A file with the name !count!.mp4 already exists in this directory.
        echo Please move or rename the existing file before running this script.
        pause
        goto :eof
    )
    
    rem Rename the file to the current count
    ren "%%f" "!count!.mp4"
    echo File renamed to !count!.mp4
    
    rem Increment the count
    set /a "count+=1"
)

rem Check if any .mp4 files were found
if "%count%"=="1" (
    echo No .mp4 files found in the current directory.
    pause
)

endlocal
