zf_bot
======

hacking up a better interface to a popular game

Установка.
1. качаем и устанавливаем AIRSDK
текущий линк http://www.adobe.com/devnet/air/air-sdk-download.html (или в гугле обычно 1я строка в поиске по AIRSDK)
2. Качаем и устанавливаем Java
Текущий линк https://java.com/ru/download/ или в гугле аналогично 1я строка поиска.
3. Запуск или st.cmd или start1.bat
в start1.bat строка python main.py 0 -c
вместо "0" укажите номер перса из settings.ini отсчет начинаеться с 0 если у вас 1 перс ничего не меняйте.
ереименовываем settings.custom.ini в settings.ini и настраиваем под себя.


Описание настроек settings.ini (может быть не полным)
[global_settings] - часть глобальных настройки.
ignore_errors = true
log_all = false
default_user = -1

[USER1] - часть настройки бота для перса.
setting_view = {'pickup':True,'location_send':True} - настройка отображения действий бота.
is_seed = f - включение модуля сеятеля. если НЕРАВЕН t то отключен.
seed_item = {u'main':'P_58','other':'P_58'} - настройка сеялки на каком острове что сеять.
cook_item = {u'main':'@RECIPE_54', 'other':'@RECIPE_5'} - настройка готовки.
locations_only = []
Если сдесь указать локации то бот будет переходить только по ним
locations_nfree = [u"isle_01", u"isle_small", u"isle_star", u"isle_large", u"isle_moon", u"isle_giant", u"isle_xxl", u"isle_desert"]
locations_nwalk = [u"un_0"+str(x+1) for x in range(9)]
locations_nother = []
Это стандартные запреты островов, по умолчанию на платные острова не ходит а так же в пещеры

sell_item = {u'S_49':10,u'S_06':5000,u'S_58':1000,u'S_15':1000} - настройка продажи
user_email = Логин
user_password = Пароль
site = vk
