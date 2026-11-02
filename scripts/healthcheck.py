import sys
import urllib.error
import urllib.request

from app.core.config import settings


def main() -> None:
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{settings.port}/docs", timeout=2)
    except (urllib.error.URLError, TimeoutError):
        sys.exit(1)


if __name__ == "__main__":
    main()
