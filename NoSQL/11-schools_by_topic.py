#!/usr/bin/env python3
"""
Function to find schools by a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school documents that include the given topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        List of matching documents
    """
    return list(mongo_collection.find({ "topics": topic }))
