#!/usr/bin/env python3

from dev_aberto import hello
import datetime
import babel.dates
import gettext

if __name__ == "__main__":
    gettext.install("cli", localedir="locale")
    date, name = hello()
    # Parse date from string.
    date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").date()
    print(_("Last commit at:"), babel.dates.format_datetime(date), _("authored by"), name)
