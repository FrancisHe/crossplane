# -*- coding: utf-8 -*-
import os

from nginx_conf.lex import lex_file

dirname = os.path.dirname(__file__)


def test_simple_config():
    config = os.path.join(dirname, 'configs', 'simple', 'nginx.conf')
    tokens = list(lex_file(config))
    assert tokens == [
        ('events', 1), ('{', 1), ('worker_connections', 2), ('1024', 2),
        (';', 2), ('}', 3), ('http', 5), ('{', 5), ('server', 6), ('{', 6),
        ('listen', 7), ('127.0.0.1:8080', 7), (';', 7), ('server_name', 8),
        ('default_server', 8), (';', 8), ('location', 9), ('/', 9), ('{', 9),
        ('return', 10), ('200', 10), ('foo bar baz', 10), (';', 10), ('}', 11),
        ('}', 12), ('}', 13)
    ]


def test_messy_config():
    config = os.path.join(dirname, 'configs', 'messy', 'nginx.conf')
    tokens = list(lex_file(config))
    assert tokens == [
        ('user', 1), ('nobody', 1), (';', 1), ('events', 3), ('{', 3),
        ('worker_connections', 3), ('2048', 3), (';', 3), ('}', 3),
        ('http', 5), ('{', 5), ('access_log', 7), ('off', 7), (';', 7),
        ('default_type', 7), ('text/plain', 7), (';', 7), ('error_log', 7),
        ('off', 7), (';', 7), ('server', 8), ('{', 8), ('listen', 9),
        ('8083', 9), (';', 9), ('return', 10), ('200', 10),
        ('Ser" \' \' ver\\\\ \\ $server_addr:\\$server_port\\n\\nTime: $time_local\\n\\n', 10),
        (';', 10), ('}', 11), ('server', 12), ('{', 12),
        ('listen', 12), ('8080', 12), (';', 12), ('root', 13),
        ('/usr/share/nginx/html', 13), (';', 13), ('location', 14), ('~', 14),
        ('/hello/world;', 14), ('{', 14), ('return', 14), ('301', 14),
        ('/status.html', 14), (';', 14), ('}', 14), ('location', 15),
        ('/foo', 15), ('{', 15), ('}', 15), ('location', 15), ('/bar', 15),
        ('{', 15), ('}', 15), ('location', 16), ('/\\{\\;\\}\\ #\\ ab', 16),
        ('{', 16), ('}', 16), ('if', 17), ('($request_method', 17), ('=', 17),
        ('P\\{O\\)\\###\\;', 17), ('S', 17), ('T', 17), (')', 17), ('{', 17),
        ('}', 17), ('location', 18), ('/status.html', 18), ('{', 18),
        ('try_files', 19), ('/abc/${uri} /abc/${uri}.html', 19), ('=404', 19),
        (';', 19), ('}', 20), ('location', 21),
        ('/sta;\n                    tus', 21), ('{', 22), ('return', 22),
        ('302', 22), ('/status.html', 22), (';', 22), ('}', 22),
        ('location', 23), ('/upstream_conf', 23), ('{', 23), ('return', 23),
        ('200', 23), ('/status.html', 23), (';', 23), ('}', 23), ('}', 23),
        ('server', 24), ('{', 25), ('}', 25), ('}', 25)
    ]
