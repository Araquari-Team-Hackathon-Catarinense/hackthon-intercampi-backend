import json


class CampusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.campus_id = request.headers.get("X-Campus-Id", None)
        print(request.campus_id)

        if request.method in ["POST", "PUT", "PATCH"]:
            if request.content_type == "application/json":
                body = json.loads(request.body)
                if body.get("campus") is None:
                    body["campus"] = request.campus_id
                    request._body = json.dumps(body).encode("utf-8")
                    request.META["CONTENT_LENGTH"] = len(request._body)
                print(request.body)

        response = self.get_response(request)

        return response
