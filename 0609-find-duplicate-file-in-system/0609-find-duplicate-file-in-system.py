class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for path in paths:
            parts = path.split(" ")
            dir_path = parts[0]

            for con_file in parts[1:]:
                file_name, content = con_file.split("(")
                content = content[:-1]
                full_path = f"{dir_path}/{file_name}"
                dictionary[content].append(full_path)
        
        return [group for group in dictionary.values() if len(group) > 1]