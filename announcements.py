import sys
import icalendar
import requests
import pytz
from datetime import datetime, timedelta
from libs import post_text
from icalendar import Calendar

r = requests.get(sys.argv[2])
icsData = r.text

cal = Calendar.from_ical(icsData)

for evt in cal.subcomponents:
    start = evt.decoded('DTSTART')
    now = datetime.now(tz=pytz.utc)
    time_left = start - now
    if timedelta(minutes=0) < time_left < timedelta(minutes=10):
        raw_text = evt.decoded('SUMMARY')
        search = re.search(r"([^ ]+)\s(.+)", raw_text)
        (nname, message) = search.groups('1')
        bot_id = find_bot_nname(nname)[0][0]
        if not bot_id:
            bot_id = sys.argv[1]
            post_text("I was supposed to post " + message + " to " + nname, bot_id)
        else:
            post_text(message, bot_id)
