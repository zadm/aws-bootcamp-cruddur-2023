from datetime import datetime, timedelta, timezone

from opentelemetry import trace

tracer = trace.get_tracer("api.notification.activities")

class NotificationsActivities:
    @tracer.start_as_current_span("api.notifications.activities.run")
    def run():
        span = trace.get_current_span()
        now = datetime.now(timezone.utc).astimezone()
        results = [
            {
                "uuid": "68f126b0-1ceb-4a33-88be-d90fa7109eee",
                "handle": "coco",
                "message": "I am zk15",
                "created_at": (now - timedelta(days=2)).isoformat(),
                "expires_at": (now + timedelta(days=5)).isoformat(),
                "likes_count": 5,
                "replies_count": 1,
                "reposts_count": 0,
                "replies": [
                    {
                        "uuid": "26e12864-1c26-5c3a-9658-97a10f8fea67",
                        "reply_to_activity_uuid": "68f126b0-1ceb-4a33-88be-d90fa7109eee",
                        "handle": "Zohir",
                        "message": "Create successfully notifications",
                        "likes_count": 0,
                        "replies_count": 0,
                        "reposts_count": 0,
                        "created_at": (now - timedelta(days=2)).isoformat(),
                    }
                ],
            }
        ]
        span.set_attribute("app.result_length", len(results))
        span.set_attribute(
            "app.reply_to_activity_uuid", "68f126b0-1ceb-4a33-88be-d90fa7109eee"
        )
        return results
