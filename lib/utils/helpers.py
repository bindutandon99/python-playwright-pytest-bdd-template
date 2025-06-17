from typing import List


class helpers:

    @staticmethod
    def is_sorted_numerically_asc(items: List[float]) -> bool:
        """Checks if a list of numbers is sorted numerically (low to high)."""
        return all(items[i] <= items[i + 1] for i in range(len(items) - 1))
