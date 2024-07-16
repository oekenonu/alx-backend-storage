#!/usr/bin/env python3
"""
List all documents in a collection
Return an empty list if no document in the collection
"""


def list_all(mongo_collection):
    """
    Function to list all document
    Return an empty list if no document in the collection
    """
    documents = mongo_collection.find()
    return documents
