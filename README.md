# aueb-to-date

My [university's website](https://aueb.gr) is terrible.

## Requirements

* python-requests (you probably already have this installed)
* [Beautiful Soup][1]

## Usage

To fetch the latest spring semester schedule, do:
```
$ python aueb-to-date.py
```
This will dump the pdf in your current directory, with the default name
provided on the website (usually Spring\_Semester\_yyyymmdd.pdf).

If you're like me, you probably rename files to something shorter (e.g.
spring2024.pdf). To do that, just run:
```
$ python aueb-to-date.py spring2024.pdf
```
You may want to schedule a cronjob to do this automatically on a regular basis.

## Backstory

I am subscribed to my university's RSS feeds that inform me about all the
latest announcements and changes to the semester schedule (this happens quite
often, unfortunately). It works very well until you find out that whenever they
update the schedule, they *don't* create a new announcement, so you ***don't
get notified***. Every since I got into uni, I had to *manually* check for this
every 2-3 days, each time having to go through 6 tons of javascript and other
bloat just to get a piece of information I *should* already be getting through
RSS. Now I finally sat down to solve this silly little problem.

[1]: https://beautiful-soup-4.readthedocs.io/en/latest/#
