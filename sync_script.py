import os
from datetime import datetime
from supabase import create_client
import re
import subprocess
from subprocess import run

# Supabase connection details (use environment variables for security)
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')  # Use the appropriate key for this approach

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# table_name = "leetcode_questions"  # Replace 'your_table_name' with your actual table name
# data = supabase.table(table_name).select('*').execute()

# print(len(data.data))
# # Print the query result
# print(data.data)
# Function to parse the README file and extract the difficulty level
def extract_difficulty(readme_contents):
    # Use a regular expression to search for difficulty within the first few lines
    match = re.search(r'<h3>(Easy|Medium|Hard)</h3>', readme_contents)
    if match:
        # The difficulty level is captured in the first capturing group of the regex
        return match.group(1)
    else:
        # If the difficulty level is not found, return 'Unknown'
        return 'Unknown'

def get_last_commit_date(file_path):
    git_command = f"git log -1 --pretty=format:%cd --date=format:'%Y-%m-%d %H:%M:%S' {os.path.abspath(file_path)}"
    process = subprocess.run(git_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = process.stdout.strip()
    print(f'output - {output}')
    return output

# def get_last_commit_date(file_path):
#     absolute_path = os.path.abspath(file_path)

#     # Check if file exists
#     if not os.path.exists(absolute_path):
#         print(f"Error: File '{absolute_path}' does not exist.")
#         return None

#     # Check if file is untracked
#     if not subprocess.run(["git", "ls-files", absolute_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
#         print(f"Error: File '{absolute_path}' is not tracked in the Git repository.")
#         return None
#     os.chdir(os.path.dirname(os.path.abspath(__file__)))
#     git_command = f"git log -1 --pretty=format:%cd --date=format:'%Y-%m-%d %H:%M:%S' --force-with-lease {absolute_path}"
#     process = subprocess.run(git_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     output = process.stdout.strip()
#     print(f'output - {output}')
#     return output
# Function to parse directory and update database

def parse_and_update(directory):
    language = None
    for root, dirs, files in os.walk(directory):
        # print(f'root : {root}, dirs: {dirs},files: {files}')  
        for file in files:
            print(f'file:{file}')
            if file == 'sync_script.py':
                continue
            if file.endswith('.py'):
                language = 'Python'
            elif file.endswith('.sql'):
                language = 'SQL'
            
            if language:  # Only proceed if the file is a Python or SQL file
                problem_name = root.split('/')[-1]
                print(f'Processing {problem_name}')
                file_name = file[:4]
                readme_path = os.path.join(root, 'README.md')
                difficulty = 'Unknown'  # Default value in case README.md does not exist or difficulty can't be determined

                if os.path.isfile(readme_path):
                    with open(readme_path, 'r') as readme_file:
                # Read the first few lines where the difficulty is expected to be
                        first_lines = ''.join([next(readme_file) for _ in range(2)])
                        difficulty = extract_difficulty(first_lines)

                commit_date = get_last_commit_date(problem_name)
                # print(f"{problem_name} - Committed on: {commit_date}")

                # Prepare data for Supabase
                data = {
                    'question_name': problem_name,
                    'file_name': file_name,
                    'readme_file_name': 'README.md' if 'README.md' in files else None,
                    'commit_date': commit_date,
                    'difficulty': difficulty,
                    'language': language,
                }

                ## Use Supabase to upsert the data (insert or update)
                response = supabase.table('leetcode_questions').upsert(data).execute()


# Run the parser and updater
parse_and_update('.')  # If running locally specify the path, in GitHub Actions the current directory is the root of the repository.
# parse_and_update('/Users/aamirhullur/Documents/Projects/Leetcode Project/Test/Leetcode-test')
