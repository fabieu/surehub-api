import itertools
from datetime import datetime, timedelta, timezone

from surehub_api.config import settings
from surehub_api.entities import official
from surehub_api.services import api
from surehub_api.utils import response_handler


def get_timeline_of_household(household_id: int, from_datetime: datetime | None = None) -> list[official.Timeline]:
    uri = f"{settings.endpoint}/api/timeline/household/{household_id}"

    if from_datetime is None:
        from_datetime = datetime.now(timezone.utc) - timedelta(hours=24)

    result: list[official.Timeline] = []
    fetch_size = 100

    # Upstream returns entries newest first and reports a placeholder count,
    # so page until an entry is older than the requested range or a page is empty.
    for page in itertools.count(1):
        payload = {'page_size': fetch_size, 'page': page}
        response = api.get(uri, params=payload)
        entries = response_handler.parse(response, model=list[official.Timeline])

        result += [e for e in entries if e.created_at and e.created_at >= from_datetime]

        if not entries or (entries[-1].created_at and entries[-1].created_at < from_datetime):
            break

    return result
