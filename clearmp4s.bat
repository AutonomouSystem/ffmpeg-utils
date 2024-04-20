@echo off

rem check if any *mp4 files exist, if not, exit

if not exist "*.mp4" (
    echo No .mp4 files found in the current directory.
    pause
    goto :eof
)

rem clear all .mp4 files in the current directory

for %%f in (*.mp4) do (
    del "%%f"
    echo File deleted: %%f
)

