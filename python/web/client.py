


def application(environ,start_response):

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h3>Hello, web!</h3>']
