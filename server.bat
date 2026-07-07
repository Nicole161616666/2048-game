@echo off
title 2048游戏服务器

echo 尝试使用 Node.js 启动服务器...
node server.js
if %errorlevel% equ 0 goto :eof

echo Node.js 未找到，尝试使用 Python...
python server.py
if %errorlevel% equ 0 goto :eof

echo Python 未找到，尝试使用 Python3...
python3 server.py
if %errorlevel% equ 0 goto :eof

echo Python 和 Node.js 都未安装，请安装其中一个
pause