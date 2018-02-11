from mom.server import Server
from flask import abort
from mom.utils import Utils


class AuthMiddleware:
    @staticmethod
    def impose(request, verify_ip=True):
        api_key = request.headers.get('Authorization')
        if api_key is None:
            abort(401)
        try:
            srv = Server.get(Server.apiKey == api_key)
            if verify_ip is True and Utils.get_client_ip() != srv.ip:
                abort(401)
            return srv
        except:
            abort(401)
