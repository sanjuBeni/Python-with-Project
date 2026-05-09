
import json
from pathlib import Path


def connection_with_file(is_fetch, data = {}):
    try:
        if not data:
            data = {
                "books" : [],
                "members" : []
            }
        file_name = "Library_Project/library_data.json"
        if Path(file_name).exists() and is_fetch:
            with open(file_name, 'r') as f:
                content = f.read().strip()
                # content = json.loads()
                if content:
                    data = json.loads(content)
        else:
            # Add File with Format
            with open(file_name, 'w') as f:
                json.dump(data, f, indent=4)
    except Exception as err:
        print(f"Some issue with file connection: {err}")
        return []
    

    return data
