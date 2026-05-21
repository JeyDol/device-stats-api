from app.core.celery import celery_app


@celery_app.task(name="app.tasks.analytics.calculate_stats")
def calculate_stats(measurements: list[dict]) -> dict:
    values = []
    for m in measurements:
        values.extend([m["x"], m["y"], m["z"]])

    values.sort()

    return {
        "min": min(values),
        "max": max(values),
        "count": len(values),
        "sum": sum(values),
        "median": values[len(values) // 2]
    }