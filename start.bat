@echo off
title mk bot����
color 0b
goto ����

:����
cls
echo �����Ҹ�Ϲ�ȣ���Է��ϼ���
echo 1. Run MK BOT
echo 2. Exit
echo 3. �ý�������(��������ڻ��) (��ǻ�͸������մϴ�.)
echo 4. pip ������Ʈ ��ġ��ٿ�ε�
echo 5. �������(�����ڵ�)
echo ���� ��ǻ���Ǹ������
set /p b=�Է�=
if %b% == 1 goto :Run
if %b% == 2 goto :E-xit
if %b% == 3 goto :����
if %b% == 4 goto :pip ���׷��̵��ٿ�ε�
if %b% == 5 goto :���


:E-xit
exit

:Run
cls
echo �����غ���
python MK_BOT.py
echo ���̾˼���������������ž����ϴ�.
echo ���� ��ǻ���Ǹ������
pause
goto ����


:����
shutdown -s -t 0
pause

:pip ���׷��̵��ٿ�ε�
start /max https://cdn.discordapp.com/attachments/526578413884932127/530657578296803338/pip.bat
goto ����

:���
echo ���
echo �̹�ġ�����Ǽ��������������ʽ��ϴ�.
echo �ǿ��ó�����ִ°��������߽��ϴ�.
echo �����ڰ� ��ǻ���Ǹ������#6225 �ΰ���Ȯ���߽��ϴ�.
echo ���������ǿ������ʽ��ϴ�.
echo ���� �ҵ��� ���θ�����ּ���.
set /p b=�Է�=
if %b% == �ҵ��� echo �ҵ��ǵž����ϴ�. ����̺Ұ����մϴ�.
if %b% == ���� echo ���ǵž����ϴ�. ����̰����մϴ�.
pause
goto ����