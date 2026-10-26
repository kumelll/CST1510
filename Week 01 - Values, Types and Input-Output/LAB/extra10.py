
ip = input("Enter IP address: ")
method = input("Enter HTTP method: ")
path = input("Enter request path: ")
status = input("Enter status code: ")
bytes_sent = input("Enter bytes sent: ")

print(f'{ip} - "{method} {path}" {status} {bytes_sent}')
