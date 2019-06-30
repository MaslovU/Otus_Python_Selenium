"""Open SSH"""
import paramiko

from otus_selenium.go_away import HOST, NAME, SECRET, PORT

transport = paramiko.Transport((HOST, PORT))
transport.connect(username=NAME, password=SECRET)
sftp = paramiko.SFTPClient.from_transport(transport)

first_path = '/home/yury/PycharmProjects/selenium_otus/ssh_test/first_path/first.py'
second_path = '/home/yury/PycharmProjects/selenium_otus/ssh_test/second_path/second.py'

"""Copy a remote file (``remotepath``) from the SFTP server to the local host as ``localpath``"""
sftp.get(first_path, second_path)

"""Copy a local file (``localpath``) to the SFTP server as ``remotepath``"""
sftp.put(second_path, first_path)

sftp.close()
transport.close()
