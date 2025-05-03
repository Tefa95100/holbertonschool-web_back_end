#!/usr/bin/env python3
"""
Function to update the topics of a school document by name
"""

def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document by name

    Args:
        mongo_collection: pymongo collection object
        name (str): name of the school to update
        topics (list): list of topics to set
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
