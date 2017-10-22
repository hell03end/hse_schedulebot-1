LESSON_SCHEMA = {
    'beginLesson': str,
    'endLesson': str,
    'discipline': str,
    'kindOfWork': str,
    'lecturer': str,
    'building': str,
    'auditorium': str,
    'date': str,
    'dayOfWeek': int
}

TABLE_MAPPING = (
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
)

MESSAGE_SCHEMA = \
    "{time}\n**{name}**\n__{type}__\n{teacher}\n{room}, `{place}`"

POST_SCHEMA = "**{date}**\n~~~~~~~~~~~~~~~\n{messages}"

LESSONS_TIMETABLE = {
    'moscow': {
        '09:00': "1",
        '10:30': "2",
        '12:10': "3",
        '13:40': "4",
        '15:10': "5",
        '16:40': "6",
        '18:10': "7",
        '19:40': "8",
    },
    'other': {
        '09:00': "1", '08:40': "1", '09:30': "1",
        '10:30': "2", '11:10': "2", '10:00': "2", '10:35': "2",
        '12:10': "3", '12:40': "3", '12:00': "3",
        '13:40': "4",
        '15:10': "5", '14:10': "5", '15:40': "5", '15:20': "5", '14:20': "5",
        '15:00': "5",
        '16:40': "6", '16:50': "6", '16:00': "6", '15:50': "6",
        '17:10': "6 7",
        '18:10': "7", '18:20': "7",
        '19:40': "8", '19:00': "8", '19:50': "8"
    }
}

CITIES = {
    'moscow',
    'piter',
    'novgorod',
    'perm'
}

DAYS = (
    "Undefined",
    "Пн",
    "Вт",
    "Ср",
    "Чт",
    "Пт",
    "Сб",
    "Вс"
)

DAY_MAPPING = (
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота"
)