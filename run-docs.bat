@echo off
call clear-cache.bat
cmd /c "zensical build"
cmd /c "zensical serve"