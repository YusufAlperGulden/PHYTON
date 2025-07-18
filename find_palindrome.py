# -*- coding: utf-8 -*-
"""Find Palindrome.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wrlyyNIBWxvH5XGqZHqytXTcwLIkwTXN
"""

def isPalindrome(string):
  """
  Checks if a string is a palindrome.

  Args:
    string: The input string.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  # Convert the string to lowercase and remove spaces
  processed_string = string.lower().replace(" ", "")
  # Compare the processed string with its reverse
  return processed_string == processed_string[::-1]

# Test cases
print(f"'kayak' is a palindrome: {isPalindrome('kayak')}")
print(f"'hello' is a palindrome: {isPalindrome('hello')}")
print(f"'Racecar' is a palindrome: {isPalindrome('Racecar')}")
print(f"'A man a plan a canal Panama' is a palindrome: {isPalindrome('A man a plan a canal Panama')}")