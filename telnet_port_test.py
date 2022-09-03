import telnetlib
import pysnooper

"""
ip_and_port.txt example

192.168.100.10:50001
192.168.100.11:50002
...
"""

def ips():
        """获取IP地址及端口信息"""
        host_ip_list = []
        host_port_list = []
        with open('ip_and_port.txt') as f:
                for line in f.readlines():
                        line_split = line.split(':')
                        host_ip = line_split[0]
                        host_port = line_split[1].strip('\n')
                        host_ip_list.append(host_ip)
                        host_port_list.append(host_port)
        return host_ip_list, host_port_list


# @pysnooper.snoop()
def telnet_test(host_ip_list, host_port_list):
        """telnet测试端口"""
        connect_failed_list = []
        for ip, port in zip(host_ip_list, host_port_list):
                try:
                        tn = telnetlib.Telnet(host=ip, port=port, timeout=0.5)
                        print(f'{ip}:{port} 状态： up')
                        tn.close()
                except:
                        print(f'{ip}:{port} 状态： down')
                        connect_failed_list.append(f'{ip}:{port}')
        return connect_failed_list


if __name__ == '__main__':

        host_ip_list, host_port_list = ips()
        results = telnet_test(host_ip_list, host_port_list)
        print('\n==============================================================\n')
        print('以下IP端口连接失败：\n')
        for i in results:
                print(i)
        print('\n连接失败的数量：', len(results))
