# This file was generated by liblab | https://liblab.com/

from enum import Enum


class Sort(Enum):
    """An enumeration representing different categories.

    :cvar NEWEST: "newest"
    :vartype NEWEST: str
    :cvar OLDEST: "oldest"
    :vartype OLDEST: str
    :cvar RELEVANCE: "relevance"
    :vartype RELEVANCE: str
    """

    NEWEST = "newest"
    OLDEST = "oldest"
    RELEVANCE = "relevance"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Sort._member_map_.values()))
