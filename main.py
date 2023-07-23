import os
import sys

from search.pdf_gpt_query import search

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No command-line arguments provided, use the default directory path
        directory_path = "./data"
        print("Using the default directory path: ./data")
    elif len(sys.argv) == 2:
        # One command-line argument provided, use it as the directory path
        directory_path = sys.argv[1]
    else:
        sys.exit("Usage: python main.py [<directory_path>]")

    if not os.path.isdir(directory_path):
        sys.exit(f"Error: The specified path '{directory_path}' is not a valid directory.")

    search(directory_path)