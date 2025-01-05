import os
import shutil


def static_to_public(current, destination):
    # check if paths exist
    if not os.path.exists(current):
        raise FileNotFoundError("Path does not exists")

    if not os.path.exists(destination):
        os.mkdir(destination)

    # First delete all contents of destination directory
    if len(os.listdir(destination)) != 0:
        shutil.rmtree(destination)
        os.mkdir(destination)
    # copy all files and subdirectories, nested files, etc
    to_copy_dir = os.listdir(current)
    for dir in to_copy_dir:
        if os.path.isfile(os.path.join(current, dir)):
            shutil.copy(os.path.join(current, dir), destination)
            print(f"Copied file: {os.path.join(current, dir)} to {destination}")
        else:
            source_dir = os.path.join(current, dir)
            dest_dir = os.path.join(destination, dir)

            if not os.path.exists(dest_dir):
                os.mkdir(dest_dir)
                print(f"Created directory: {dest_dir}")

            static_to_public(source_dir, dest_dir)
