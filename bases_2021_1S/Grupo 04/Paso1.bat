@echo off
@echo **INSTALANDO CHOCOLATEY
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
@echo **INSTALANDO PYTHON
::choco install python --pre
choco install python --version=3.9
@echo **INSTALANDO NODEJS
choco install -y --force nodejs
@echo Finalizado
pause