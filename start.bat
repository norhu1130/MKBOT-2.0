@echo off
title mk bot시작
color 0b
goto 시작

:시작
cls
echo 실행할목록번호를입력하세요
echo 1. Run MK BOT
echo 2. Exit
echo 3. 시스템종료(서버생긴뒤사용) (컴퓨터를종료합니다.)
echo 4. pip 업데이트 설치기다운로드
echo 5. 약관동의(관리자도)
echo 제작 컴퓨터의모든팁들
set /p b=입력=
if %b% == 1 goto :Run
if %b% == 2 goto :E-xit
if %b% == 3 goto :종료
if %b% == 4 goto :pip 업그레이드기다운로드
if %b% == 5 goto :약관


:E-xit
exit

:Run
cls
echo 시작준비중
python MK_BOT.py
echo 봇이알수없는이유로종료돼었습니다.
echo 문의 컴퓨터의모든팁들
pause
goto 시작


:종료
shutdown -s -t 0
pause

:pip 업그레이드기다운로드
start /max https://cdn.discordapp.com/attachments/526578413884932127/530657578296803338/pip.bat
goto 시작

:약관
echo 약관
echo 이배치파일의수정을절대하지않습니다.
echo 악용시처벌이있는것을이해했습니다.
echo 개발자가 컴퓨터의모든팁들#6225 인것을확인했습니다.
echo 종료기능을악용하지않습니다.
echo 동의 불동의 여부를골라주세요.
set /p b=입력=
if %b% == 불동의 echo 불동의돼었습니다. 사용이불가능합니다.
if %b% == 동의 echo 동의돼었습니다. 사용이가능합니다.
pause
goto 시작