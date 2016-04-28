@echo off

ECHO.
echo Iniciando Jekyll...
ECHO.

chcp 65001
REM --safe because GitHub Pages runs it like that (no plugins, ignore symbolic links)
bundle exec jekyll serve --safe --watch --incremental
