import commands as cmd
import setup_functions as sf

def main():
    sf.setup_git()
    sf.setup_dvc()
    sf.setup_s3()
    cmd.dvc_add("src/datasets/sales")
    cmd.git_add("src/datasets/sales")
    cmd.git_push()
    cmd.dvc_push()

if __name__ == "__main__":
    main()

