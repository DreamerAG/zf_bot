@echo off
set PAUSE_ERRORS=1
call bat\SetupSDK.bat
call bat\SetupApplication.bat

echo.
echo Starting AIR Debug Launcher...
echo.
::echo %APP_XML%
::echo %APP_DIR%
::echo %FLEX_SDK%
::set L_PATH = %FLEX_SDK%\%APP_DIR%\adl
::@echo %L_PATH%
%FLEX_SDK%\%APP_DIR%\adl "%APP_XML%" "%APP_DIR%"
::pause
if errorlevel 1 goto error
goto end

:error
#pause

:end