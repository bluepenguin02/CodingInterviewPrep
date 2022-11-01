"""
https://leetcode.com/problems/insert-interval/description/

LeetCode 57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        new_intervals = []
        add_interval = []
        added_new_interval = False
        for start, end in intervals:
            if end < newInterval[0]:
                new_intervals.append([start, end])
            elif newInterval[1] < start:
                if not added_new_interval:
                    if not add_interval:
                        add_interval = newInterval
                    new_intervals.append(add_interval)
                    added_new_interval = True
                new_intervals.append([start, end])
            else:
                if not add_interval:
                    add_interval = [min(newInterval[0], start), -1]
                add_interval[1] = max(newInterval[1], end)
            
        if not added_new_interval:
            if not add_interval:
                new_intervals.append(newInterval)
            else:
                new_intervals.append(add_interval)
            
        return new_intervals
