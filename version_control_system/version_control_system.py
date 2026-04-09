import sys
import os
import hashlib
import shutil

VCS_DIR = "vcs"
CONFIG_FILE = os.path.join(VCS_DIR, "config.txt")
INDEX_FILE = os.path.join(VCS_DIR, "index.txt")
LOG_FILE = os.path.join(VCS_DIR, "log.txt")
COMMITS_DIR = os.path.join(VCS_DIR, "commits")

COMMANDS = {
    "config": "Get and set a username.",
    "add": "Add a file to the index.",
    "log": "Show commit logs.",
    "commit": "Save changes.",
    "checkout": "Switch between commits and restore a previous file state."
}


# ---------------------- utils ----------------------

def ensure_vcs():
    os.makedirs(VCS_DIR, exist_ok=True)
    os.makedirs(COMMITS_DIR, exist_ok=True)

    for file in [CONFIG_FILE, INDEX_FILE, LOG_FILE]:
        if not os.path.exists(file):
            open(file, "w").close()


def get_hash(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def read_index():
    with open(INDEX_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]


# ---------------------- commands ----------------------

def help_command():
    print("These are VCS commands:")
    for cmd, desc in COMMANDS.items():
        print(f"{cmd} {desc}")


def config(args):
    ensure_vcs()

    if len(args) == 0:
        with open(CONFIG_FILE) as f:
            name = f.read().strip()
            if name:
                print(f"The username is {name}.")
            else:
                print("Please, tell me who you are.")
    else:
        name = args[0]
        with open(CONFIG_FILE, "w") as f:
            f.write(name)
        print(f"The username is {name}.")


def add(args):
    ensure_vcs()

    if len(args) == 0:
        files = read_index()
        if not files:
            print("Add a file to the index.")
        else:
            print("Tracked files:")
            print("\n".join(files))
    else:
        filename = args[0]
        if not os.path.exists(filename):
            print(f"Can't find '{filename}'.")
            return

        with open(INDEX_FILE, "a+") as f:
            f.seek(0)
            existing = f.read().splitlines()
            if filename not in existing:
                f.write(filename + "\n")

        print(f"The file '{filename}' is tracked.")


def commit(args):
    ensure_vcs()

    if len(args) == 0:
        print("Message was not passed.")
        return

    message = args[0]
    files = read_index()

    if not files:
        print("Nothing to commit.")
        return

    combined_hash = ""

    for file in files:
        if os.path.exists(file):
            combined_hash += get_hash(file)

    commit_id = hashlib.sha256(combined_hash.encode()).hexdigest()
    commit_path = os.path.join(COMMITS_DIR, commit_id)

    if os.path.exists(commit_path):
        print("Nothing to commit.")
        return

    os.makedirs(commit_path)

    for file in files:
        if os.path.exists(file):
            shutil.copy(file, commit_path)

    with open(CONFIG_FILE) as f:
        author = f.read().strip()

    with open(LOG_FILE, "r+") as log:
        old = log.read()
        log.seek(0)
        log.write(f"commit {commit_id}\nAuthor: {author}\n{message}\n\n{old}")

    print("Changes are committed.")


def log():
    ensure_vcs()

    with open(LOG_FILE) as f:
        content = f.read().strip()
        if content:
            print(content)
        else:
            print("No commits yet.")


def checkout(args):
    ensure_vcs()

    if len(args) == 0:
        print("Commit id was not passed.")
        return

    commit_id = args[0]
    commit_path = os.path.join(COMMITS_DIR, commit_id)

    if not os.path.exists(commit_path):
        print("Commit does not exist.")
        return

    for file in os.listdir(commit_path):
        shutil.copy(os.path.join(commit_path, file), file)

    print(f"Switched to commit {commit_id}.")


# ---------------------- main ----------------------

def main():
    args = sys.argv[1:]

    if not args or args[0] == "--help":
        help_command()
        return

    command = args[0]
    if command not in COMMANDS:
        print(f"'{command}' is not a VCS command.")
        return

    if command == "config":
        config(args[1:])
    elif command == "add":
        add(args[1:])
    elif command == "commit":
        commit(args[1:])
    elif command == "log":
        log()
    elif command == "checkout":
        checkout(args[1:])

    if name == "main":
        main()