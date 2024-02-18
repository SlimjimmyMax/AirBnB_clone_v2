#!/usr/bin/python3
# 
# 
class FileStorage:
    # Existing code...

    def close(self):
        """Calls reload() method for deserializing the JSON file to objects"""
        self.reload()
