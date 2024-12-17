import os
import subprocess

def get_user_input():
    repo_url = input("Enter the repository URL: ")
    try:
        num_commits = int(input("Enter the number of commits: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for commits.")
        return None, None
    return repo_url, num_commits

def commit_to_repo(repo_url, num_commits):
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        if not os.path.exists(repo_name):
            subprocess.run(['git', 'clone', repo_url])
        os.chdir(repo_name)
        for i in range(num_commits):
            file_name = f'file_{i}.txt'
            with open(file_name, 'w') as f:
                f.write(f'This is commit number {i+1}')
            subprocess.run(['git', 'add', file_name])
            subprocess.run(['git', 'commit', '-m', f'Add {file_name}'])

            if os.path.exists(file_name):
                os.remove(file_name)
                
            subprocess.run(['git', 'rm', file_name])
            subprocess.run(['git', 'commit', '-m', f'Remove {file_name}'])

        subprocess.run(['git', 'push'])
            

def main():
    repo_url, num_commits = get_user_input()
    if not (repo_url and num_commits):
        print("Invalid Input - Exiting...")
        return 1

    commit_to_repo(repo_url, num_commits)

if __name__ == "__main__":
    main()