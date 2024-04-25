import math
from pytz import timezone
from datetime import datetime


def format_size(size_in_bytes: int, base: int = 1024) -> str:
    """
    Convert a size in bytes to a human-readable format.

    Args:
        size_in_bytes (int): The size to be converted, in bytes.
        base (int, optional): The base to use for conversion (default is 1024).

    Returns:
        str: A string representing the size in a human-readable format.

    Raises:
        ValueError: If the size is less than or equal to zero.

    Examples:
        >>> format_size(1024)
        '1.00 KB'
        >>> format_size(1000000000)
        '953.67 MB'
        >>> format_size(0)
        '0.00 B'
    """

    if size_in_bytes <= 0:
        return "0.00 B"

    size_abbreviations = "B", "KB", "MB", "GB", "TB", "PB"

    abbreviation_index = int(math.log(size_in_bytes, base))

    power = base ** abbreviation_index

    final_size = size_in_bytes / power

    size_abbreviation = size_abbreviations[abbreviation_index]

    return f'{final_size:.2f} {size_abbreviation}'


def format_date(timestamp: float):
    """
    Convert a UNIX timestamp to a formatted date and time string in the São
    Paulo time zone.

    Args:
        timestamp (float): The UNIX timestamp to be formatted.

    Returns:
        str: A string representing the formatted date and time in the São
        Paulo time zone.

    Examples:
        >>> format_date(1619751461.0)
        '29/04/2021 23:57:41'
        >>> format_date(1620823300.0)
        '12/05/2021 09:41:40'
    """

    zone = "America/Sao_Paulo"
    format = "%d/%m/%Y %H:%M:%S"
    time = datetime.fromtimestamp(timestamp, timezone(zone))
    return time.strftime(format)
