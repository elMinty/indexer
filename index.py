from abc import abstractclassmethod
import os
import io
import json




# Two databases:
#
# 1. doc attribute index:  "doc_id" : {url, category}
# 2. word index: "word" : {json file}
#
# Json file contains the positions and doc_id and positions of that word within the document.
# Json file and attributes stored locally until batch update
# 
# @TODO:
# VITAL: set up SERVER
#
# 1. Setup db structures
# 2. Create index pipeline (reversing BOW index)
# 3. Update and Modify DB functions
# 4. JSON editors



class IndexDOC:

    def __init__(self, url, BOW, category, sentiment):

        self.docID = None
        

    # main index function
    def index(self, url, BOW):
        self.docID = hash(url)
        self.update_dai()

        self.


    # updater for doc attribute index
    def update_dai(self):
        
        # TODO :set values




