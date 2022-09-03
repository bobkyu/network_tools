import os
import sys
import re

url = sys.argv[1]

curl_cmd = f'curl {url}  -w "DNS_TIME:%{{time_namelookup}}   TCP_CONNECT_TIME:%{{time_connect}}   SSL_CONNECT_TIME:%{{time_appconnect}}   START_HTTP_TIME:%{{time_pretransfer}}    FIRST_PACKET_TIME:%{{time_starttransfer}}    TOTAL_TIME:%{{time_total}}\n" -s -o /dev/null'

curl_result = os.popen(curl_cmd).readlines()
# DNS解析时间
dns_time = re.findall('DNS_TIME:(\d+.\d+)', str(curl_result))
# TCP建立连接时间
tcp_connect_time_ls = re.findall('TCP_CONNECT_TIME:(\d+.\d+)', str(curl_result))
tcp_connect_time = round(float(tcp_connect_time_ls[0]) - float(dns_time[0]), 3)
# SSL建立连接时间
ssl_connect_time_ls = re.findall('SSL_CONNECT_TIME:(\d+.\d+)', str(curl_result))
ssl_connect_time = round(float(ssl_connect_time_ls[0]) - float(tcp_connect_time_ls[0]), 3)
# HTTP开始请求时间
start_http_time_ls = re.findall('START_HTTP_TIME:(\d+.\d+)', str(curl_result))
start_http_time = round(float(start_http_time_ls[0]) - float(ssl_connect_time_ls[0]), 3)
# 整体总耗时
total_time_ls = re.findall('TOTAL_TIME:(\d+.\d+)', str(curl_result))
total_time = total_time_ls[0]
# 首包响应时间
first_packet_time_ls = re.findall('FIRST_PACKET_TIME:(\d+.\d+)', str(curl_result))
first_packet_time = round(float(first_packet_time_ls[0]) - float(start_http_time_ls[0]), 3)
# HTTP请求总耗时
http_total_time =  round(float(total_time_ls[0]) - float(start_http_time_ls[0]), 3)


print(curl_result,'\n')
print('====网络性能====')
print(f'DNS解析时间为：{dns_time[0]} 秒')
print(f'TCP建连时间为：{tcp_connect_time} 秒')
print(f'SSL建连时间为：{ssl_connect_time} 秒')
print('\n====系统性能====')
print(f'建连后开始请求时间：{start_http_time} 秒')
print(f'HTTP首包响应时间：{first_packet_time} 秒')
print(f'HTTP请求总耗时：  {http_total_time} 秒')
print(f'\n总体耗时：{total_time} 秒')
