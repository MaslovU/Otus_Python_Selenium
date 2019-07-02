#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Python Linux"""

import os


def test_net_interface():
    """ 1. Сетевые интерфейсы"""
    net = os.popen('ifconfig lo')
    data = net.read()
    assert '127.0.0.1' in data
    print('success!')
    print(data)


def test_default_route():
    """2. Маршрут по умолчанию"""
    file = os.popen('ip r | grep default')
    data = file.read()
    assert '192.168.1.1' in data
    print(data)


def test_info_about_processor():
    """3. Информацию о состоянии процессора"""
    proc = os.popen('lscpu')
    for data in proc.readlines():
        if 'Model name' in data:
            assert 'AMD A8-7410 APU with AMD Radeon R5 Graphics' in data
            print(data)


def test_info_about_processes():
    """4. Информацию о процессе"""
    process = os.getpid()
    user = os.getlogin()
    assert 'yury' in user
    print("Process ID: ", process, "\nUser: ", user)


def test_list_all_process():
    """5. Список всех процессов"""
    process_output = os.popen("ps -Af")
    for data in process_output.readlines():
        if 'yury' in data:
            print('Yury is a process')


def test_statistic_net_interface():
    """6. Статистику работы сетевых интерфейсов"""
    net_interface = os.popen('netstat -i')
    for data in net_interface.readlines():
        if 'lo' in data:
            assert 'LRU' in data


def test_working_servise():
    """7. Статус работы какого либо сервиса"""
    service = os.popen('systemctl list-units --type service')
    for data in service.readlines():
        if 'accounts-daemon.service' in data:
            assert 'loaded active' in data


def test_netstat():
    """8. Состояние сетевого порта на сервере (TCP или UDP)"""
    net_tcp = os.popen('netstat -at')
    for data in net_tcp.readlines():
        if 'localhost:mysql' in data:
            assert 'LISTEN' in data
            print("Local address: 'localhost:mysql' with status: LISTEN")


def test_version_packages():
    """9. Версию пакета (имя пакета передается как аргумент)"""
    version_package = os.popen('dpkg -s {}'.format('ubuntu-desktop')).read()
    assert '1.417.1' in version_package
    print(version_package)


def test_list_of_files():
    """10. Список в файлов в директории"""
    list_of_files = os.listdir("/home/yury/Desktop/log")
    assert 'session_logs' in list_of_files
    print(list_of_files)


def test_current_directory():
    """11. Текущую директорию"""
    current_directory = os.getcwd()
    assert '/home/yury/PycharmProjects/selenium_otus/Python_for_linux' in current_directory
    print(current_directory)


def test_vertion_core():
    """12. Vertion core"""
    version_core = os.popen('uname -r').read()
    assert '4.15.0-54-generic' in version_core
    print(version_core)


def test_version_os():
    """13. Версию операционной системы"""
    version_os = os.popen('cat /etc/*-release')
    assert 'DISTRIB_RELEASE=18.04' in version_os.read()
    print('Release version: DISTRIB_RELEASE=18.04')
