import os
import subprocess
import sys


def main():
    directory = sys.argv[1]
    if os.path.exists(directory + '/id_rsa.pub'):
        pass
    else:
        # ディレクトリがある場合、エラーになる？無視になるかな？
        os.mkdir(directory)
        os.chmod(directory, '600')
        os.chdir(directory)
        subprocess.call('ssh-keygen')

if __name__ == '__main__':
    main()


