import tomllib

# This class is used to parse a pyproject.toml file.
# Chris Joakim, 3Cloud/Cognizant, 2026


class PyprojectParser:
    def __init__(self):
        self.data = None

    def parse(self, filename: str = "pyproject.toml") -> dict:
        self.data = dict()
        try:
            with open(filename, "rb") as f:
                self.data = tomllib.load(f)
                return self.data
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_name(self) -> str:
        return self.data["project"]["name"]

    def get_version(self) -> str:
        return self.data["project"]["version"]

    def get_description(self) -> str:
        return self.data["project"]["description"]

    def get_dependencies(self) -> list:
        return (
            self.data["project"]["dependencies"] if "dependencies" in self.data["project"] else []
        )

    def get_dependency_names(self) -> list:
        dep_names = dict()
        for dep in self.get_dependencies():
            # 'aiohttp>=3.11.18'
            s = dep.replace(">", " ").replace("<", " ").replace("=", " ")
            name = s.split(" ")[0].strip()
            dep_names[name] = dep
        return sorted(dep_names.keys())
