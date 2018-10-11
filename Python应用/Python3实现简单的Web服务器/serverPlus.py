# coding=utf-8

import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class ServerException(Exception):
    """服务器内部错误"""
    pass
    
    
class case_NoFile(object):
    """该路径不存在"""

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.full_path))


class case_ExistingFile(object):
    """该路径是文件"""

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handle_file(handler.full_path)


class case_AlwaysFail(object):
    """所以情况都不符合的默认处理类"""

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))


class case_DirectoryIndexFile(object):

    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    # 判断目标路径是否是目录&&目录下是否有index.html
    def test(self, handler):
        return os.path.isdir(handler.full_path) and os.path.isfile(self.index_path(handler))

    # 响应index.html的内容
    def act(self, handler):
        handler.handle_file(self.index_path(handler))


class RequestHandler(BaseHTTPRequestHandler):

    Error_Page = """\
    <html>
    <body>
    <h1>Error accessing {path}</h1>
    <p>{msg}</p>
    </body>
    </html>
    """

    # 所以可能的情况
    Cases = [case_NoFile(), case_ExistingFile(), case_DirectoryIndexFile(), case_AlwaysFail()]

    def do_GET(self):
        try:
            # 文件完整路径
            # self.full_path = os.getcwd() + self.path
            self.full_path = os.getcwd() + "\\"

            # 遍历所有的可能情况
            for case in self.Cases:
                # 如果满足该类情况
                if case.test(self):
                    case.act(self)
                    break
        # 处理异常
        except Exception as msg:
            self.handle_error(msg)

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode("utf-8"), 404)

    # def create_page(self):
    #     values = {
    #         'date_time': self.date_time_string(),
    #         'client_host': self.client_address[0],
    #         'client_port': self.client_address[1],
    #         'command': self.command,
    #         'path': self.path
    #     }
    #     page = self.Page.format(**values)
    #     return page

    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def handle_file(self, full_path):
        try:
            print("########### " + full_path)
            with open(full_path, 'rb') as reader:
                print("########### " + full_path)
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
