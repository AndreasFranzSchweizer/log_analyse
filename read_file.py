def is_connection_entry(text):
	if "New connection from" in text:
		return True
	return False

def remove_port(host_with_port):
	if host_with_port.count('.') == 3 and host_with_port.count(':') == 1:
		return host_with_port.split(':')[0]
	elif host_with_port.count(':') > 1:
		return host_with_port.rsplit(':', 1)[0]
	else:
		return host_with_port

def get_client_ip(text):
	if is_connection_entry(text):
		parts = text.split(' ')
		if len(parts) > 5:
			return parts[4]

ips = {}

with open('log.txt') as file:
	for line in file.readlines():
		if is_connection_entry(line):
			ip = remove_port(get_client_ip(line))
			ips[ip] = ips.get(ip, 0) + 1

for ip, count in ips.items():
	print(f'{ip} had {count} connections')