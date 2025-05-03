#!/usr/bin/env python3
"""
Function to insert a document into a MongoDB collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection

    Args:
        mongo_collection: pymongo collection object
        **kwargs: keyword arguments representing document fields

    Returns:
        The _id of the new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
