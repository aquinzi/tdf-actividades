@echo off

ECHO.
echo Iniciando Jekyll...
ECHO.

chcp 65001

ECHO local(l) or build(b)?
set /p INPUT=": "

:: The /I switch makes the comparisons case-insensitive
If /I "%INPUT%"=="l" ( 
	bundle exec jekyll serve --watch --incremental
)
If /I "%INPUT%"=="b" ( 
	bundle exec jekyll build
)
