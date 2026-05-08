import os
from typing import List, Dict, Any

class ResourceLoader:
    """
    Core engine for loading and parsing BOSC Community Library resources.
    """
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.registry = {}

    def scan_resources(self, directory: str) -> List[str]:
        """
        Scans a directory for .bosc resource files.
        """
        resources = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".bosc"):
                    resources.append(os.path.join(root, file))
        return resources

    def load_metadata(self, resource_path: str, visited: set = None) -> Dict[str, Any]:
        """
        Loads metadata from a resource file with recursion protection.
        """
        if visited is None:
            visited = set()
        
        if resource_path in visited:
            return {"error": "Circular reference detected", "path": resource_path}
        
        visited.add(resource_path)
        # Simulation of loading linked resources
        return {"path": resource_path, "status": "indexed", "links": [], "metadata": {}}

    def get_localized_metadata(self, metadata: Dict[str, Any], lang_code: str) -> Dict[str, str]:
        """
        Extracts localized fields for the given language code.
        """
        localized = {}
        for key, value in metadata.get("localizations", {}).items():
            if lang_code in value:
                localized[key] = value[lang_code]
        return localized
