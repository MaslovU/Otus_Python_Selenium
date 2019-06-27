"""Open SSH"""
import paramiko

from otus_selenium.go_away import HOST, NAME, SECRET, PORT


def connect_to_paramiko_and_stop(command):
    """Function"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=HOST, username=NAME, password=SECRET, port=PORT)
    stdin, stdout, stderr = client.exec_command('sudo service apache2 ' + command + '')
    data = stdout.read() + stderr.read()
    client.close()
    return data


def test_stop_apache_server():
    """Stop server"""
    data = connect_to_paramiko_and_stop('stop')
    assert 'active' not in str(data)


def test_start_apache_server():
    """Start and check status"""
    connect_to_paramiko_and_stop('start')
    data = connect_to_paramiko_and_stop('status')
    assert 'active' in str(data)

