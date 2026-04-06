class File:
  def __init__(self, name, size): 
    self.name = name
    self.size = size

  def __repr__(self): 
    return f"{self.name} ({self.size})"


class Directory: 
  def __init__(self, name): 
    self.name = name
    self.children = []
    self.size = 0

  def __repr__(self): 
    return self.name

  def add_child(self, child_node): 
    self.children.append(child_node)


class InvalidPath(Exception): 
  pass


class FileTree: 

  def __init__(self): 
    
    self.root = Directory("")
    self.size = 0
       
  def _find_directory(self, path, node=None):
    if not node: 
      node = self.root

    if path == []: 
      return node
    else: 
      for n in node.children: 
        if n.name == path[0]:
          return self._find_directory(path[1:], n)

      raise InvalidPath
    
  def add_directory(self, path):
    parts = path.split("/")[1:]
    new_dir_name = parts[-1]
    path_list = parts[:-1]
    new_dir = Directory(new_dir_name)  
    self._find_directory(path_list).add_child(new_dir)
  
  def add_file(self, path, size): 
    self.better_add_file(path, size)
    ##parts = path.split("/")[1:]
    #new_file_name = parts[-1]
    #path_list = parts[:-1]
    #new_file = File(new_file_name, size) 
    #self._find_directory(path_list).add_child(new_file)

  def print_tree(self, node=None, level=0):

    if node == None: 
      self.print_tree(self.root, level) 
      return

    print(level * " " + "+-"+str(node))
    if isinstance(node, Directory): 
      for child in node.children:
        print((level+1) * " " + "|")
        self.print_tree(child, level+1)

  def total_size_recursive(self, node=None):
    '''
    Compute the sum of all file sizes in the tree.
    '''
    if node == None: 
      return self.total_size_recursive(self.root)
      
    if isinstance(node, File): 
      return node.size
    
    # otherwise, it's a directory
    total = 0
    for child in node.children: 
      total += self.total_size_recursive(child)
    return total
    
  # new method added for part c) 
  def _better_add_recursive(self, new_file, path, node=None):
    if not node: 
      node = self.root          

    node.size += new_file.size # add size to current directory before moving to one of the children

    if path == []: 
      node.add_child(new_file) # found directory, add child
    else: 
      for n in node.children: 
        if n.name == path[0]:           
          return self._better_add_recursive(new_file, path[1:], n)

      raise InvalidPath

  def better_add_file(self, path, size): 
    '''
    Insert the file and update the total size for each subtree. 
    '''
    pass #TODO, replace this pass to implement the method

    parts = path.split("/")[1:]
    new_file_name = parts[-1]
    path_list = parts[:-1]
    new_file = File(new_file_name, size) 
    self._better_add_recursive(new_file, path_list)

if __name__ == "__main__":

  tree = FileTree()
  tree.add_file("/hello.txt",100)
  tree.add_directory("/subdir")
  tree.add_file("/subdir/nested.txt", 200)
  tree.add_directory("/subdir/another_subdir")
  tree.add_file("/subdir/another_subdir/world.txt", 50)
  tree.add_file("/subdir/nested.txt", 150)
  tree.print_tree()
  print(f"Total size: {tree.total_size_recursive()}")

  tree = FileTree()
  tree.better_add_file("/hello.txt",100)
  tree.add_directory("/subdir")
  tree.better_add_file("/subdir/nested.txt", 200)
  tree.add_directory("/subdir/another_subdir")
  tree.better_add_file("/subdir/another_subdir/world.txt", 50)
  tree.better_add_file("/subdir/nested.txt", 150)

  print(f"Total size with better_add_file: {tree.root.size}")

