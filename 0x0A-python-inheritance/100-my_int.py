#!/usr/bin/python3
"""
Magic methods to rebuke the rebellion
"""


class MyInt(int):
    """
    class MyInt that inherits from int
    """

    def __eq__(self, value):
        """Magic method
        Defines behavior for the equality operator, ==
        """

        return super().__ne__(value)

    def __ne__(self, value):
        """Magic method
        Defines behavior for the inequality operator, !=
        """

        return super().__eq__(value)
