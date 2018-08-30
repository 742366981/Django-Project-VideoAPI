from rest_framework.renderers import JSONRenderer


class MyJsonRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if isinstance(data, dict):
            msg = data.pop('msg', '请求成功')
            code = data.pop('code', 0)
        else:
            msg = '请求成功'
            code = 0
        res = {
            'data': data,
            'msg': msg,
            'code': code,
        }
        return super().render(res, accepted_media_type=None, renderer_context=None)
