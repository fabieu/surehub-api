import re
from logging import getLogger

from requests import Response

logger = getLogger(__name__)

# URLs whose response body must not be logged, e.g. because it contains credentials
BODY_LOG_EXCLUDED_URLS = {
    re.compile(r"/api/auth/login$"),
}


def log_response(response: Response) -> None:
    method = response.request.method
    url = response.request.url
    status_code = response.status_code
    reason = response.reason
    http_version = response.raw.version_string

    if 200 <= status_code < 300:
        logger.info('"%s %s %s" %s %s', method, url, http_version, status_code, reason)
    elif 400 <= status_code < 600:
        logger.error('"%s %s %s" %s %s', method, url, http_version, status_code, reason)

    if url and not any(pattern.search(url) for pattern in BODY_LOG_EXCLUDED_URLS):
        logger.debug("Response body: %s", response.text)
