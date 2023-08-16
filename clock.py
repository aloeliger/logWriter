import urwid
import datetime
import pytz

parisTimezone = pytz.timezone('Europe/Paris')

clockText = urwid.Text('', align='center')
clock = urwid.LineBox(clockText)

def update_time(loop, user_data=None):
    clockText.set_text(
        datetime.datetime.now(parisTimezone).strftime("CMS Local Time: %H:%M:%S")
    )
    loop.set_alarm_in(1, update_time)
