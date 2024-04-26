import random

def generate_ips_with_ports(ips, count=20):
    ports = [443, 8443, 2053, 2083, 2087, 2096]
    generated_ips = []

    for _ in range(count):
        # 随机选择一个IP地址
        base_ip = random.choice(ips)
        # 替换最后的0为1-255的一个随机数
        new_ip = base_ip[:-1] + str(random.randint(1, 255))
        # 随机选择一个端口
        port = random.choice(ports)
        # 合并新IP和端口
        generated_ips.append(f"{new_ip}:{port}")

    return generated_ips

# 预定义的IP列表
ips = [
    "172.64.152.0", "104.19.32.0", "104.17.16.0", "104.16.32.0",
    "172.64.159.0", "172.64.147.0", "104.16.192.0", "104.17.48.0",
    "104.18.42.0", "104.17.160.0", "104.18.47.0", "104.16.144.0",
    "104.17.144.0", "104.17.112.0", "104.18.80.0", "104.18.45.0",
    "104.17.208.0", "104.18.46.0", "172.64.156.0", "172.64.155.0"
]

# 生成IP地址
generated_ips = generate_ips_with_ports(ips)

# 将生成的IP地址写入文件
with open('ips.txt', 'w') as file:
    for ip in generated_ips:
        print(ip)
        file.write(ip + '\n')
