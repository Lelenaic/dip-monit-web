from mom.server import Server
from flask import abort


class AuthMiddleware:
    @staticmethod
    def impose(request, verify_ip=True):
        api_key = request.headers.get('Authorization')
        if api_key is None:
            abort(401)
        try:
            srv = Server.get(Server.apiKey == api_key)
            if verify_ip is True and request.remote_addr != srv.ip:
                abort(401)
            return srv
        except:
            abort(401)
