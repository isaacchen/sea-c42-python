import time

poll_rows1 = [{"ID": 1, "State": "WA", "Pollster": "A", "Date": "Jan 07 2010"},
              {"ID": 2, "State": "WA", "Pollster": "B", "Date": "Mar 21 2010"},
              {"ID": 3, "State": "WA", "Pollster": "A", "Date": "Jan 08 2010"},
              {"ID": 4, "State": "OR", "Pollster": "A", "Date": "Feb 10 2010"},
              {"ID": 5, "State": "WA", "Pollster": "B", "Date": "Feb 10 2010"},
              {"ID": 6, "State": "WA", "Pollster": "B", "Date": "Mar 22 2010"}]

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if
    date1 is before date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

s = 'WA'


def most_recent_poll_row(poll_rows, pollster, state):
    date = 'Jan 01 1969'
    result = []
    for row in poll_rows:
        if (row['State'] == state and row['Pollster'] == pollster):
            newdate = row['Date']
            if earlier_date(date, newdate):
                date = newdate
                result = row
    if (result == []):
        return None
    else:
        return result

print(most_recent_poll_row(poll_rows1, 'A', 'WA'))

