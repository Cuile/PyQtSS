@echo off
@echo 1. 正在建立 SSH Tunnel。
@echo 2. 请不要对窗口进行任务操作。
@echo 3. 关闭窗口，结束 SSH Tunnel。
plink.exe -ssh -2 -4 -C -batch -N ^
			-P 2222 ^
			-D localhost:10808 ^
			-i d:\ssh_key\cuile.key.ppk ^
			linuxserver.io@ss2.cuile.com
