#!/usr/bin/env python3
"""
Module to insert a new document in a collection based on kwargs
Returns new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in collection
    Returns the new _id
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
