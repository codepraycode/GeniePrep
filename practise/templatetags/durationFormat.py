from django import template


register = template.Library()

# Receives td in minutes and return the mins:secs
@register.filter
def durationVerbose(td):
    td = float(td)
    dur_sec = td * 60
    mins = int(dur_sec // 60)
    secs = int(dur_sec % 60)

    # Add 0 if mins is < 10, and s if mins is > 1
    mins_s = str(mins).zfill(2) + ' minute'
    mins_s += 's' if mins > 1 else ''
    # Add 0 if secs is < 10, and s if secs is > 1
    secs_s = str(secs).zfill(2) + ' second'
    secs_s += 's' if secs > 1 else ''

    return "{}, {}".format(mins_s, secs_s)


@register.filter
def durationDigital(td):
    td = float(td)
    dur_sec = td * 60
    mins = int(dur_sec // 60)
    secs = int(dur_sec % 60)

    mins = str(mins).zfill(2)
    secs = str(secs).zfill(2)

    return "{}:{}".format(mins, secs)


register.filter('durationSent', durationVerbose)
register.filter('durationDigit', durationDigital)
