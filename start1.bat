:begin
python main.py 0 -c
set Timer=10
ping -n %Timer% 127.0.0.1>nul
goto begin