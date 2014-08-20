:user_configuration

:: Path to Flex SDK
::set FLEX_SDK=C:\Users\NBK\AppData\Local\FlashDevelop\Apps\ascsdk\14.0.0
For /F "Delims=" %%I In ('WHERE /R c:\users airsdk.xml') Do Set FLEX_SDK=%%~I
echo %FLEX_SDK%
set FLEX_SDK=%FLEX_SDK:\airsdk.xml=%
echo %FLEX_SDK%
#pause
:validation
if not exist "%FLEX_SDK%" goto flexsdk
goto succeed

:flexsdk
echo.
echo ERROR: incorrect path to Flex SDK in 'bat\SetupSDK.bat'
echo.
echo %FLEX_SDK%
echo.
#if %PAUSE_ERRORS%==1 pause
exit

:succeed
set PATH=%PATH%;%FLEX_SDK%\bin

