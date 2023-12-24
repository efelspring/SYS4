import telnetlib 
HOST = "192.168.100.1"

t = telnetlib.Telnet(HOST, 80, 5)
t.write("GET / HTTP/1.1\r\n".encode("ascii"))
t.write("Host: pi-1\r\n".encode("ascii"))
t.write("\r\n".encode("ascii"))

data = ''
while data.find("</html>") == -1:
    data += t.read_very_eager().decode('UTF-8')
print(data)