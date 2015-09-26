import time

poll_rows1 = [{"ID": 1, "State": "WA", "Pollster": "A", "Date": "Jan 07 2010"},
              {"ID": 2, "State": "WA", "Pollster": "B", "Date": "Mar 21 2010"},
              {"ID": 3, "State": "WA", "Pollster": "A", "Date": "Jan 08 2010"},
              {"ID": 4, "State": "OR", "Pollster": "A", "Date": "Feb 10 2010"},
              {"ID": 5, "State": "WA", "Pollster": "B", "Date": "Feb 10 2010"},
              {"ID": 6, "State": "WA", "Pollster": "B", "Date": "Mar 22 2010"}]

rows1 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
rows2 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
         {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
rows3 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
         {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
         {'State': 'WA', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'},
         {'State': 'CA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'IPSOS'}]
rows4 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
         {'State': 'WA', 'Dem': '1.0', 'Rep': '10.3', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'}]
rows5 = [{'State': 'WA', 'Dem': '1.0', 'Rep': '0.1', 'Date': 'Nov 05 2008', 'Pollster': 'PPP'},
         {'State': 'CA', 'Dem': '2.1', 'Rep': '3.2', 'Date': 'Nov 04 2008', 'Pollster': 'PPP'},
         {'State': 'OR', 'Dem': '9.1', 'Rep': '7.1', 'Date': 'Nov 05 2008', 'Pollster': 'IPSOS'}]


def row_to_edge(row):
    """
    Given an *ElectionDataRow* or *PollDataRow*, returns the
    Democratic *Edge* in that *State*.
    """
    return (float(row["Dem"]) - float(row["Rep"]))


def state_edges(election_result_rows):
    """
    Given a list of *ElectionDataRow*s, returns *StateEdge*s.
    The input list has no duplicate *States*;
    that is, each *State* is represented at most once in the input list.
    """
    d = {}
    for row in election_result_rows:
        state = row['State']
        d[state] = row_to_edge(row)
    return d


def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if
    date1 is before date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))


def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of *PollDataRow*s, returns the most recent row with the
    specified *Pollster* and *State*. If no such row exists, returns None.
    """
    date1 = 'Jan 01 1969'
    result = []
    for row in poll_rows:
        if (row['State'] == state and row['Pollster'] == pollster):
            date2 = row['Date']
            if earlier_date(date1, date2):
                    date1 = date2
                    result = row
    if (result == []):
        return None
    else:
        return result


def unique_column_values(rows, column_name):
    # Create a set of values from PollDataRow
    values = set()
    for row in rows:
        if (row[column_name]) not in values:
            values.add(row[column_name])
    return values


def pollster_predictions(poll_rows):
    pollsters = unique_column_values(poll_rows, 'Pollster')
    states = unique_column_values(poll_rows, 'State')
    pp = {}
    for p in pollsters:
        pp[p] = {}
        for s in states:
            if most_recent_poll_row(poll_rows, p, s):
                edge = state_edges([(most_recent_poll_row(poll_rows, p, s))])
                pp[p][s] = edge[s]
    return pp

print(pollster_predictions(rows3))
