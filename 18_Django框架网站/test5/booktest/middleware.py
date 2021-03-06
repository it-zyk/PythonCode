from django.http import HttpResponse


class BlockedIPSMiddleware(object):
    '''中间件类'''
    EXCLUDE_IPS = ['10.2.34.36']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('Forbidden')


class TestMiddleware(object):
    '''中间件类'''

    def __init__(self):
        '''服务器重启之后，接收第一个请求调用'''
        print("------------init-------------")

    def process_request(self, request):
        '''产生request 对象之后，url 匹配之前调用 '''
        print('----------------process_request------------')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''url匹配之后，视图函数调用之前调用'''
        print('---------------process_view-------------')

    def process_response(self, request, response):
        '''视图函数调用后，内容返回浏览器之前'''
        print('------------------process_response--------')
        return response


class ExceptionTest1Middleware(object):

    def process_exception(self, request, exception):
        '''视图函数发生异常时调用'''
        print('------------process_exception1-------')


class ExceptionTest2Middleware(object):
    def process_exception(self, request, exception):
        '''视图函数发生异常时调用'''
        print('------------process_exception2-------')
