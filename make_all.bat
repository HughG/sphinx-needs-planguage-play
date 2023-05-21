@ECHO OFF

pushd %~dp0

: call make clean
call make html
call make needs
