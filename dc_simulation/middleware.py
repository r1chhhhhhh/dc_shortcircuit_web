from django.urls import resolve
import logging

logger = logging.getLogger(__name__)

class DebugURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 处理请求前
        resolved_before = None
        if request.path.startswith('/media/'):
            try:
                resolved_before = resolve(request.path_info)
                print(f"DEBUG_MIDDLEWARE (Before Response): Request path: {request.path}")
                if resolved_before:
                    print(f"DEBUG_MIDDLEWARE (Before Response): Resolved view name: {getattr(resolved_before, 'view_name', 'N/A')}")
                    print(f"DEBUG_MIDDLEWARE (Before Response): Resolved func: {getattr(resolved_before, 'func', 'N/A')}")
            except Exception as e:
                print(f"DEBUG_MIDDLEWARE (Before Response): Could not resolve path {request.path}: {e}")


        response = self.get_response(request)

        # 处理响应后
        if request.path.startswith('/media/'):
            print(f"DEBUG_MIDDLEWARE (After Response): Response Content-Type for {request.path}: {response.get('Content-Type')}")
            if resolved_before: # Log resolved view again for context with response
                 print(f"DEBUG_MIDDLEWARE (After Response): View for {request.path} was: {getattr(resolved_before, 'func', 'N/A')}")


        return response