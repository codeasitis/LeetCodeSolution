# LeetCodeSolution
This repository contains all the solution of Leet Code which is generally practice by Students . The implementation is in Python.
1. Problem 1 - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
   
    Two Sum II - Input Array Is Sorted

    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these   two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
  
    The tests are generated such that there is exactly one solution. You may not use the same element twice. Your solution must use only constant extra space.
    
    Solution File Name - Leet167-Two Sums II - Input Array Is Sorted.py 

2. Problem 2 - https://leetcode.com/problems/linked-list-cycle/
 
    Linked List Cycle

    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by       continuously following the next pointer. Internally, pos is used to denote the index of the node that    tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.

    Solution File Name - Leet141- Link List Cycle.py

 3. Problem 3 - https://leetcode.com/problems/palindrome-linked-list/
    
    Palindrome Linked List

    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
    
    Solution File Name - Leet234 - Palindrome Linked List.py

4. Problem 4 - https://leetcode.com/problems/remove-nth-node-from-end-of-list
    
    Remove Nth Node From End of List

    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    
    Solution File Name - Leet19- Remove Nth Node From End of List.py

5. Problem 5 - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    
    Remove Duplicates from Sorted List II

    Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
    
    Solution File Name - Leet82 - Remove Duplicates from Sorted List II.py

6. Problem 6 - https://leetcode.com/problems/spiral-matrix/
    
    Spiral Matrix

    Given an m x n matrix, return all elements of the matrix in spiral order.
    
    Solution File Name - Leet54-Spiral Matrix.py

7. Problem 7 - https://leetcode.com/problems/set-matrix-zeroes/
    
    Set Matrix Zeroes

    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.
    
    Solution File Name - Leet73 - Set Matrix Zeroes.py

7. Problem 8 - https://leetcode.com/problems/validate-binary-search-tree/
    
    Validate Binary Search Tree

    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

       a. The left subtree of a node contains only nodes with keys **less than** the node's key.
       b. The right subtree of a node contains only nodes with keys **greater than** the node's key.
       c. Both the left and right subtrees must also be binary search trees.
    
    Solution File Name - Leet98 - Validate Binary Search Tree.py

8. Problem 235 - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
    
   Lowest Common Ancestor of a Binary Search Tree

   Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    
    Solution File Name - Leet235-Lowest Common Ancestor of a Binary Search Tree.py

9. Problem 235 - https://leetcode.com/problems/trapping-rain-water/
    
   Trapping Rain Water

   Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    
    Solution File Name - Leet42 - Trapping Rain Water.py    

10. Problem 173 - https://leetcode.com/problems/binary-search-tree-iterator/
    
   Binary Search Tree Iterator

   Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.

    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
    
    int next() Moves the pointer to the right, then returns the number at the pointer.
    
    Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

    You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
    
    Solution File Name - Leet173-Binary Search Tree Iterator.py