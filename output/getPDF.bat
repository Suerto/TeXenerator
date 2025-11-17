@echo off
REM Compilazione PDF LaTeX con nome file passato come argomento

IF "%~1"=="" (
    echo Uso: getPDF nome_file.tex
    exit /b 1
)

SET FILE=%~1
SET BASENAME=%~n1

echo Compilazione PDF LaTeX per %FILE%...
pdflatex -interaction=nonstopmode -halt-on-error %FILE%
pdflatex -interaction=nonstopmode -halt-on-error %FILE%

echo Pulizia file temporanei...
del %BASENAME%.aux
del %BASENAME%.log
del %BASENAME%.toc
del %BASENAME%.out

echo PDF generato correttamente: %BASENAME%.pdf
pause