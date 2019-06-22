import paramiko

host = 'localhost'
name = 'admin'
secret = 'admin'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=name, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('ls -l')
data = stdout.read() + stderr.read()
client.close()
