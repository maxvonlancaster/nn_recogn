#!/usr/env python3
import http.server as server
import os
import logging
import nn_service

class HTTPRequestHandler(server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.warning('GET REQUEST')
        server.SimpleHTTPRequestHandler.do_GET(self)
        logging.warning(self.headers)

    def do_POST(self):
        logging.warning('POST REQUEST')
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        result = nn_service.process_image(post_data);
        logging.warning(self.headers)


    def do_PUT(self):
        logging.warning('PUT REQUEST')
        """Save a file following a HTTP PUT request"""
        filename = os.path.basename(self.path)

        # Don't overwrite files
        if os.path.exists(filename):
            self.send_response(409, 'Conflict')
            self.end_headers()
            reply_body = '"%s" already exists\n' % filename
            self.wfile.write(reply_body.encode('utf-8'))
            return

        file_length = int(self.headers['Content-Length'])
        with open(filename, 'wb') as output_file:
            output_file.write(self.rfile.read(file_length))
        self.send_response(201, 'Created')
        self.end_headers()
        reply_body = 'Saved "%s"\n' % filename
        self.wfile.write(reply_body.encode('utf-8'))

    


if __name__ == '__main__':
    server.test(HandlerClass=HTTPRequestHandler,port=8080)
    # default port = 8000