"""
Problem 7: Request Routing in a Web Server with a Trie

This module implements an HTTPRouter using a Trie data structure.

The HTTPRouter takes a URL path like "/", "/about", or 
"/blog/2019-01-15/my-awesome-blog-post" and determines the appropriate handler 
to return. The Trie is used to efficiently store and retrieve handlers based on 
the parts of the path separated by slashes ("/").

The RouteTrie stores handlers under path parts, and the Router delegates adding 
and looking up handlers to the RouteTrie. The Router also includes a not found 
handler for paths that are not found in the Trie and handles trailing slashes 
to ensure requests for '/about' and '/about/' are treated the same.

You sould implement the function bodies the function signatures. Use the test 
cases provided below to verify that your algorithm is correct. If necessary, 
add additional test cases to verify that your algorithm works correctly.
"""

from typing import Optional

class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

class RouteTrie:
    def __init__(self, root_handler: str):
        self.root = RouteTrieNode()
        self.root_handler = root_handler

    def insert(self, path_parts: list[str], handler: str) -> None:
        curr_node = self.root
        for path in path_parts:
            if path not in curr_node.children:
                curr_node.children[path] = RouteTrieNode()
            curr_node = curr_node.children[path]
        curr_node.handler = handler


    def find(self, path_parts: list[str]) ->  Optional[str]:
        curr_node = self.root
        for path in path_parts:
            if path not in curr_node.children:
                return None
            curr_node = curr_node.children[path]

        return curr_node.handler

class Router:
    def __init__(self, root_handler: str, not_found_handler: str):

        self.root_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler


    def add_handler(self, path: str, handler: str) -> None:

        path_parts = self.split_path(path)
        self.root_trie.insert(path_parts,handler)

    def lookup(self, path: str) -> str:

        if path == '/':
            return self.root_trie.root_handler
        path_parts = self.split_path(path)
        handler = self.root_trie.find(path_parts)
        return handler if handler else self.not_found_handler
        pass

    def split_path(self, path: str) -> list[str]:

        return [part for part in path.split("/") if part]


if __name__ == '__main__':
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # Edge case: Empty path
    print(router.lookup(""))
    # Expected output: 'not found handler'

    print(router.lookup("/home/contact"))
    # Expected output: 'not found handler'

    # Normal case: Path with multiple segments
    print(router.lookup("/home/about/me"))
    # Expected output: 'not found handler'

    # Normal case: Path with exact match
    print(router.lookup("/home/about"))
    # Expected output: 'about handler'
