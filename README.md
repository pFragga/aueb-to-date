# aueb-to-date

My [university's website](https://aueb.gr) is terrible.

## Dependencies

* [Beautiful Soup][1]

## Usage

```
$ [python] aueb-to-date [filename]
```
You may want to schedule a cronjob to do this automatically on a regular basis.
Here's an [example script][2] that I run in my crontab.

## Backstory

I am subscribed to my university's RSS feeds that inform me about all the
latest announcements and changes to the semester schedule (this happens quite
often, unfortunately). It works very well until you find out that whenever they
update the schedule, they *don't* create a new announcement, so you ***don't
get notified***. Ever since I got into uni, I had to *manually* check for this
every 2-3 days, each time having to go through 6 tons of javascript and other
bloat just to get a piece of information I *should* already be getting through
RSS. Now I finally sat down to solve this silly little problem.

[1]: https://beautiful-soup-4.readthedocs.io/en/latest/#
[2]: https://github.com/pFragga/dotfiles/blob/master/scripts/.scripts/get_semester
