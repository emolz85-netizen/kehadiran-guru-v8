from django.conf import settings

def school_settings(request):
    return {
        "SCHOOL_LATITUDE": settings.SCHOOL_LATITUDE,
        "SCHOOL_LONGITUDE": settings.SCHOOL_LONGITUDE,
        "SCHOOL_RADIUS_METERS": settings.SCHOOL_RADIUS_METERS,
    }
