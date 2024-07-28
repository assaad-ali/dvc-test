import subprocess
import os


def check_dvc_initialized():
    return os.path.isdir(".dvc")

def check_git_initialized():
    return os.path.isdir(".git")

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

def git_init():
    return run_command("git init")

def dvc_init():
    return run_command("dvc init")

def git_add(path):
    return run_command(f"git add {path}")

def git_commit(message):
    return run_command(f'git commit -m "{message}"')

def dvc_add(path):
    return run_command(f"dvc add {path}")

def git_push():
    return run_command("git push")

def dvc_push():
    return run_command("dvc push")

def git_pull():
    return run_command("git pull")

def dvc_pull():
    return run_command("dvc pull")

def git_status():
    return run_command("git status")

def dvc_status():
    return run_command("dvc status")

def dvc_remote_add(remote_name, url):
    return run_command(f"dvc remote add -d {remote_name} {url}")

def dvc_remote_modify(remote_name, option, value):
    return run_command(f"dvc remote modify {remote_name} {option} {value}")

def dvc_config(option, value):
    return run_command(f"dvc config {option} {value}")

def configure_s3_remote(remote_name, bucket_name, region):
    if dvc_remote_add(remote_name, f"s3://{bucket_name}") != 0:
        print(f"Failed to add remote {remote_name}.")
        return
    if dvc_remote_modify(remote_name, "endpointurl", f"https://s3.{region}.amazonaws.com") != 0:
        print(f"Failed to modify remote {remote_name}.")
        return
    print(f"Configured S3 remote '{remote_name}' for bucket '{bucket_name}' in region '{region}'.")
