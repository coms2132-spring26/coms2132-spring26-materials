import importlib.util
import sys
import os
from collections import deque
import subprocess

def load_module(file_path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def grade_linked_list():
    module = load_module("linked_list.py", "linked_list")
    LinkedList = module.DoubleLinkedList
    
    score = 0
    ll = LinkedList()
    target = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for val in target: 
        ll.append(val)
    
    # Test flip_pairs method with even and odd sizes
    ll.flip_pairs()
    expected_even = ["B", "A", "D", "C", "F", "E", "H", "G", "J", "I"]
    if [ll.get(i) for i in range(ll.__len__())] == expected_even:
        score += 2
    else: 
        print("Flip pairs didn't work with even number of items. -5")
    
    ll.append("K")
    ll.flip_pairs()
    expected_odd = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    if [ll.get(i) for i in range(ll.__len__())] == expected_odd:
        score += 3
    else: 
        print("Flip pairs didn't work with odd number of items. -5")
    

    # Test iterator
    iterator = iter(ll)
    if next(iterator) == "A":
      score += 2 
      print("iter and next work")

    target = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K"]

    i = 0 
    okay = True
    for item in ll: 
      if item != target[i]:
        okay = False
      i += 1
    if okay: 
      score += 3
      print("items returned in correct order and stopping")

    return score

def grade_browser_history():
    module = load_module("browser_history.py", "browser_history")
    BrowserHistory = module.BrowserHistory
    
    score = 0
    bh = BrowserHistory()
    urls = ["google.com", "wikipedia.org", "github.com", "stackoverflow.com", "reddit.com"]
    for url in urls:
        bh.visit(url)
    

    bh.back()
    bh.back()
    bh.back()
    if bh.forward() == "github.com" and bh.forward() == "stackoverflow.com":
        score += 5
    else:
        print("Failed 1st BrowserHistory Test Case" )
    
    bh.back()
    bh.visit("newsite.com")
    if bh.forward() is None:
        score += 5
    
    if set(["google.com", "wikipedia.org", "github.com", "newsite.com"]).issubset(bh.recently_visited()):
        score += 5
    else:
        print("Failed 2nd BrowserHistory Test Case" )
    
    return score

def grade_file_tree():
    module = load_module("file_tree.py", "file_tree")
    FileTree = module.FileTree
    File = module.File
    
    score = 0
    ft = FileTree()
    
    # Add directories and files
    ft.add_directory("/subdir")
    ft.add_directory("/subdir/nested")
    ft.add_file("/file1.txt", 100)
    ft.add_file("/subdir/file2.txt", 200)
    ft.add_file("/subdir/nested/file3.txt", 300)

    ft.print_tree(ft.root)
    print("+5 if tree looks correct")
    
    # Test total size calculation
    if ft.total_size_recursive(ft.root) == 600:
        print("total_size_recursive okay")
        score += 5
    
    # Test hierarchical updates
    ft.add_file("/subdir/nested/file4.txt", 150)
    #May need to change total_size attribute to whatever name they used
    if ft.root.size == 750:
        print("size okay")
        score += 5
    
    return score

def grade_counting_out():
    score = 0
    test_cases = [(9, 4, "1 wins"), (7, 3, "4 wins"), (10, 2, "5 wins")]
    
    for n, k, expected in test_cases:
        try:
            result = subprocess.run(["python3", "counting_out.py"], input=f"{n}\n{k}\n", text=True, capture_output=True, timeout=5)
            output = result.stdout.strip().split("\n")
            if output and expected in output[-1]:
                score += 5
            print(output)
        except Exception:
            pass
    
    return score

def main():
    ll_score = grade_linked_list()
    bh_score = grade_browser_history()
    ft_score = grade_file_tree()
    co_score = grade_counting_out()
    total_score = ll_score + bh_score + ft_score + co_score
    
    print(f"Linked List Score (CHECK PART C MANUALLY): {ll_score}/15")
    print(f"Counting Out Score: {co_score}/15")
    print(f"Browser History Score: {bh_score}/15")
    print(f"File Tree Score (CHECK PART C OUPUT MANUALLY): {ft_score}/15")
    
    print(f"Final Score: {total_score}/60")

if __name__ == "__main__":
    main()
