'''
Fall2020
CS 5001 HW5
Yici Zhu
it's a program getting directions
on Seattle Link light rail
'''


LINK_STATIONS = ("University of Washington", "Capitol Hill",
                 "Westlake", "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")


def is_valid_station(station):
    '''
    Function -- is_valid_station
        Checks if a given string is a valid Seattle light rail station.
        Provided station must match a station name exactly. For example, "mount
        baker" would not be valid because the case doesn't match.
    Parameter:
        station -- The string to check
    Returns:
        True if a given string is a valid Seattle light rail station
        name, False otherwise.
    '''
    if station in LINK_STATIONS:
        return True
    else:
        False


def get_direction(start, end):
    '''
    Function -- get_direction
        Given start and end station names, determines if the direction is
        Northbound or Southbound.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        "Northbound" if the end station is north of the start station, or
        "Southbound" if the end station is south of the start station. If
        either station is invalid, or start and end stations are the same,
        return "No destination found".
    '''
    if not is_valid_station(start) or not is_valid_station(end):
        return "No destination found"
    if LINK_STATIONS.index(start) < LINK_STATIONS.index(end):
        return "Southbound"
    elif LINK_STATIONS.index(start) > LINK_STATIONS.index(end):
        return "Northbound"
    else:
        return "No destination found"


def get_num_stops(start, end):
    '''
    Function -- get_num_stops
        Calculates the number of stops from start to end.
    Parameters:
        start - The starting station name
        end - The ending station name.
    Returns:
        The number of stops from start to end. If either station is invalid
        or both stations are the same, return 0.
    '''
    if not is_valid_station(start) or not is_valid_station(end):
        return 0
    start = LINK_STATIONS.index(start)
    end = LINK_STATIONS.index(end)
    num = end - start
    if end - start < 0:
        num = 0 - num
    return num
