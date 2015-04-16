"""
Lists of constants that can be used in the Notifications subsystem
"""

from django.conf import settings

NOTIFICATION_PRIORITY_NONE = 0
NOTIFICATION_PRIORITY_LOW = 1
NOTIFICATION_PRIORITY_MEDIUM = 2
NOTIFICATION_PRIORITY_HIGH = 3
NOTIFICATION_PRIORITY_URGENT = 4

NOTIFICATION_MAX_LIST_SIZE = getattr(settings, 'NOTIFICATION_MAX_LIST_SIZE', 100)

USER_PREFERENCE_MAX_LIST_SIZE = getattr(settings, 'USER_PREFERENCE_MAX_LIST_SIZE', 100)

# client side rendering via Backbone/Underscore
RENDER_FORMAT_HTML = 'html'

# for future use
RENDER_FORMAT_EMAIL = 'email'
RENDER_FORMAT_SMS = 'sms'
RENDER_FORMAT_DIGEST = 'digest'

NOTIFICATION_BULK_PUBLISH_CHUNK_SIZE = getattr(settings, 'NOTIFICATION_BULK_PUBLISH_CHUNK_SIZE', 100)
NOTIFICATION_MINIMUM_PERIODICITY_MINS = getattr(settings, 'NOTIFICATION_MINIMUM_PERIODICITY_MINS', 60)  # hourly

NOTIFICATION_PURGE_READ_OLDER_THAN_DAYS = getattr(settings, 'NOTIFICATION_PURGE_READ_OLDER_THAN_DAYS', None)
NOTIFICATION_PURGE_UNREAD_OLDER_THAN_DAYS = getattr(settings, 'NOTIFICATION_PURGE_UNREAD_OLDER_THAN_DAYS', None)

MINUTES_IN_A_DAY = 24 * 60
MINUTES_IN_A_WEEK = 7 * 24 * 60

NOTIFICATION_ARCHIVE_ENABLED = getattr(settings, 'NOTIFICATION_ARCHIVE_ENABLED', False)

NOTIFICATIONS_PREFERENCE_DAILYDIGEST_DEFAULT = getattr(
    settings,
    'NOTIFICATIONS_PREFERENCE_DEFAULTS',
    {}
).get('DAILY_DIGEST', 'false')

NOTIFICATIONS_PREFERENCE_WEEKLYDIGEST_DEFAULT = getattr(
    settings,
    'NOTIFICATIONS_PREFERENCE_DEFAULTS',
    {}
).get('WEEKLY_DIGEST', 'false')

NOTIFICATION_NAMESPACE_USER_SCOPE_NAME = 'namespace_scope'

NOTIFICATION_DAILY_DIGEST_PREFERENCE_NAME = 'daily-notification-digest'
NOTIFICATION_WEEKLY_DIGEST_PREFERENCE_NAME = 'weekly-notification-digest'
NOTIFICATION_DAILY_DIGEST_SUBJECT = getattr(
    settings,
    "NOTIFICATION_DAILY_DIGEST_SUBJECT",
    "Please set NOTIFICATION_DAILY_DIGEST_SUBJECT in Django settings"
)
NOTIFICATION_WEEKLY_DIGEST_SUBJECT = getattr(
    settings,
    "NOTIFICATION_WEEKLY_DIGEST_SUBJECT",
    "Please set NOTIFICATION_WEEKLY_DIGEST_SUBJECT in Django settings"
)

NOTIFICATION_BRANDED_DEFAULT_LOGO = getattr(settings, "NOTIFICATION_BRANDED_DEFAULT_LOGO", None)

NOTIFICATION_DIGEST_FROM_ADDRESS = getattr(
    settings,
    "NOTIFICATION_DAILY_FROM_ADDRESS",
    "please_set_NOTIFICATION_DIGEST_FROM_ADDRESS@settings.com"
)
NOTIFICATION_DONT_SEND_EMPTY_DIGEST = getattr(settings, 'NOTIFICATION_DONT_SEND_EMPTY_DIGEST', True)
NOTIFICATION_DIGEST_UNREAD_ONLY = getattr(settings, 'NOTIFICATION_DIGEST_UNREAD_ONLY', True)

# this describes how we want to group together notification types into visual groups
NOTIFICATION_DIGEST_GROUP_CONFIG = getattr(
    settings,
    "NOTIFICATION_DIGEST_GROUP_CONFIG",
    {
        'groups': {
            'announcements': {
                'name': 'announcements',
                'display_name': 'Announcements',
                'group_order': 1
            },
            'group_work': {
                'name': 'group_work',
                'display_name': 'Group Work',
                'group_order': 2
            },
            'leaderboards': {
                'name': 'leaderboards',
                'display_name': 'Leaderboards',
                'group_order': 3
            },
            'discussions': {
                'name': 'discussions',
                'display_name': 'Discussion',
                'group_order': 4
            },
            '_default': {
                'name': '_default',
                'display_name': 'Other',
                'group_order': 5
            },
        },
        'type_mapping': {
            'open-edx.lms.discussions.cohorted-thread-added': 'group_work',
            'open-edx.lms.discussions.cohorted-comment-added': 'group_work',
            'open-edx.lms.discussions.*': 'discussions',
            'open-edx.lms.leaderboard.*': 'leaderboards',
            'open-edx.studio.announcements.*': 'announcements',
            'open-edx.xblock.group-project.*': 'group_work',
            '*': '_default'
        },
    }
)

NOTIFICATION_DIGEST_EMAIL_CSS = getattr(settings, "NOTIFICATION_DIGEST_EMAIL_CSS", None)
