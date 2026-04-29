# https://www.acmicpc.net/problem/5052
# 2026-02-01
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key):
        self.key = key          
        self.children = {}      
        self.flag = False   

class Trie:
    def __init__(self):
        self.head = Node(None) 

    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            
            curr_node = curr_node.children[char]
            
            if curr_node.flag:
                return False
        curr_node.flag = True 
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    phone_book = []
    for _ in range(n):
        phone_book.append(input().strip())
    
    trie = Trie()
    phone_book.sort(key=len) 
    
    consistent = True
    for phone in phone_book:
        if not trie.insert(phone): 
            consistent = False
            break
            
    if consistent:
        print("YES")
    else:
        print("NO")