import os
from pathlib import Path
import sys
import os.path

from lib.client import get_lifelogs
from lib.format import print_tree
from lib.env import load_env

# Add the parent directory to the path so we can import constants
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import .env files
root_dir = Path(__file__).resolve().parent.parent
load_env(root_dir)

def main():
    # Get transcripts
    lifelogs = get_lifelogs(limit=1, structure="tree", includeMarkdown=False, includeHeadings=True)

    # Print tree
    print_tree(lifelogs)

if __name__ == "__main__":
    main() 
