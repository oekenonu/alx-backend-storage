#!/usr/bin/env python3
"""
Module to returns list of schools having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
