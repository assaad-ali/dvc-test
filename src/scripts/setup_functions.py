import commands as cmd


def setup_s3():
    try:
        if cmd.check_s3_configured("dvc-project"):
            print("S3 is already configured.")
            return
        
        bucket_name = input("Enter the name of your S3 bucket: ")
        region = input("Enter the region of your S3 bucket: ")
        remote_name = input("Enter the region of your S3 bucket: ")

        if not cmd.check_dvc_initialized():
            cmd.dvc_init()
            
        try:
            cmd.configure_s3_remote(remote_name, bucket_name, region)
        except Exception as e:
            print(f"Failed to configure S3 remote: {e}")
            return
        
    except Exception as e:
        print(f"Failed to setup S3: {e}")
        return
    
    print("Setup complete.")

def setup_git():
    try:
        if cmd.check_git_initialized():
            print("Git is already initialized.")
            return
        
        if cmd.git_init() != 0:
            print("Failed to initialize git.")
            return
        print("Git initialized.")

    except Exception as e:
        print(f"Failed to setup git: {e}")
        return

    print("git setup complete")


def setup_dvc():
    try:
        if cmd.check_dvc_initialized():
            print("DVC is already initialized.")
            return

        if cmd.dvc_init() != 0:
            print("Failed to initialize DVC.")
            return

        print("DVC setup complete")

    except Exception as e:
        print(f"Failed to setup DVC: {e}")
        return