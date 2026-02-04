@echo off
title Chrome CDP Launcher
echo ============================================
echo Chrome CDP Launcher for DeepSeek Automation
echo ============================================
echo.

:: Check if CDP already running
curl -s http://localhost:9222/json/version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Chrome CDP already running on port 9222
    echo Ready to use.
    pause
    exit /b 0
)

:: Check if Chrome is running without CDP
tasklist /FI "IMAGENAME eq chrome.exe" 2>NUL | find /I "chrome.exe" >NUL
if %ERRORLEVEL% EQU 0 (
    echo Chrome is running without CDP.
    echo Closing Chrome...
    taskkill /F /IM chrome.exe >nul 2>&1
    ping -n 4 127.0.0.1 >nul
)

:: Launch Chrome with CDP
echo Launching Chrome with CDP on port 9222...
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir="C:\Users\cresc\ChromeCDP" --no-first-run --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-renderer-backgrounding https://chat.deepseek.com

:: Wait for CDP
echo Waiting for CDP to be ready...
set /a count=0
:wait_loop
if %count% GEQ 30 goto timeout
curl -s http://localhost:9222/json/version >nul 2>&1
if %ERRORLEVEL% EQU 0 goto ready
ping -n 2 127.0.0.1 >nul
set /a count+=1
goto wait_loop

:ready
echo.
echo Chrome CDP is ready on port 9222!
echo DeepSeek tab should be open.
echo.
pause
exit /b 0

:timeout
echo.
echo ERROR: CDP did not start within 30 seconds.
echo.
pause
exit /b 1
