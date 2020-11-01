import datetime


def current_datetime():
    date_time = datetime.datetime.now().isoformat()
    print("dateTime:[%s]\n" % (date_time))
    return "dateTime:[%s]" % (date_time)
