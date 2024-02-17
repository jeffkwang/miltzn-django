import logging

class LogIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Configure your logger here
        self.logger = logging.getLogger("django")

    def __call__(self, request):
        # Log the IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        self.logger.info(f"Request from IP: {ip}")

        response = self.get_response(request)
        return response
