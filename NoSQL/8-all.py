#!/usr/bin/env python3
"""
Function to list all documents in a MongoDB collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents or an empty list if none are found
    """
    return list(mongo_collection.find())
