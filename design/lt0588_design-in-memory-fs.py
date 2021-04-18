import bisect
"""
tree structure
space complexity: O(n) for n is number of files/folders

time complexity 
for ls: O(depth)
for mkdir: O(nlogn) for n is the number of children in that folder
for read: O(1)
"""
class Node:
    def __init__(self, name):
        self.name = name
        self.children_dict = dict()
        self.children = list()

class FileSystem:

    def __init__(self):
        self.root = Node("", )
        self.file_dict = dict()



    def ls(self, path: str) -> List[str]:

        path = path.rstrip("/")
        if path in self.file_dict:
            return[path.split("/")[-1]]
        p = path.split("/")
        if path == "":
            return self.root.children
        folder = self.root
        for d in p[1:]:
            folder = folder.children_dict[d]
        return folder.children

    def mkdir(self, path: str) -> None:
        path = path.rstrip("/")
        p = path.split("/")
        folder = self.root
        for i in p [1:]:
            if i in folder.children_dict:
                folder = folder.children_dict[i]
                continue
            else:
                new_folder = Node( i)
                folder.children_dict[i] = new_folder
                bisect.insort_left(folder.children, i)
                folder = new_folder


    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath in self.file_dict:
            self.file_dict[filePath] += content
        else:
            self.mkdir(filePath)
            self.file_dict[filePath] = content

    def readContentFromFile(self, filePath: str) -> str:
        return self.file_dict[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
