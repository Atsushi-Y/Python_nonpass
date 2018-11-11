import sys
import os


def main():
    directory = sys.argv[1]
    key = sys.argv[2]
    command = sys.argv[3]
    authorized_key = directory + '/authorized_key'
    if os.path.exists(authorized_key):
        pass
    else:
        # ディレクトリがある場合、エラーになる？無視になるかな？
        os.mkdir(directory)
        os.chmod(directory, '600')


        with open(authorized_key, 'a') as f:
            # これだと同じキー書かれていた場合、重複になってしまう
            f.write(command + key)




    pass


if __name__ == '__main__':
    main()
