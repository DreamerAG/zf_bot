zf_bot
======

hacking up a better interface to a popular game

���������.
1. ������ � ������������� AIRSDK
������� ���� http://www.adobe.com/devnet/air/air-sdk-download.html (��� � ����� ������ 1� ������ � ������ �� AIRSDK)
2. ������ � ������������� Java
������� ���� https://java.com/ru/download/ ��� � ����� ���������� 1� ������ ������.
3. ������ ��� st.cmd ��� start1.bat
� start1.bat ������ python main.py 0 -c
������ "0" ������� ����� ����� �� settings.ini ������ ����������� � 0 ���� � ��� 1 ���� ������ �� �������.
�������������� settings.custom.ini � settings.ini � ����������� ��� ����.


�������� �������� settings.ini (����� ���� �� ������)
[global_settings] - ����� ���������� ���������.
ignore_errors = true
log_all = false
default_user = -1

[USER1] - ����� ��������� ���� ��� �����.
setting_view = {'pickup':True,'location_send':True} - ��������� ����������� �������� ����.
is_seed = f - ��������� ������ �������. ���� ������� t �� ��������.
seed_item = {u'main':'P_58','other':'P_58'} - ��������� ������ �� ����� ������� ��� �����.
cook_item = {u'main':'@RECIPE_54', 'other':'@RECIPE_5'} - ��������� �������.
locations_only = []
���� ����� ������� ������� �� ��� ����� ���������� ������ �� ���
locations_nfree = [u"isle_01", u"isle_small", u"isle_star", u"isle_large", u"isle_moon", u"isle_giant", u"isle_xxl", u"isle_desert"]
locations_nwalk = [u"un_0"+str(x+1) for x in range(9)]
locations_nother = []
��� ����������� ������� ��������, �� ��������� �� ������� ������� �� ����� � ��� �� � ������

sell_item = {u'S_49':10,u'S_06':5000,u'S_58':1000,u'S_15':1000} - ��������� �������
user_email = �����
user_password = ������
site = vk
