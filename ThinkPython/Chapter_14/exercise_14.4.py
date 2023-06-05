from os import path, popen, listdir
from hashlib import md5


def walk(directory: str='.', suffix: str='.mp3', result: list=[]) -> list:
    for name in listdir(directory):
        some_file= path.join(directory, name)
        if path.isfile(some_file):
            if some_file[len(some_file)-len(suffix):] == suffix:
                result.append(some_file)
        else:
            result = walk(some_file, suffix, result)
    
    return result


def recognise_duplicates_linux(files: list) -> dict:
    files_sums = {}

    for file in files:
        cmd = 'md5sum ' + file
        fp = popen(cmd)
        res = fp.read()
        files_sums[file] = res.split(" ")[0]

    unique_files_amount = len(set(list(files_sums.values())))
    print(f"There are {unique_files_amount} unique files in selected directory.")

    return files_sums


def recognise_duplicates(files: list) -> dict:
    files_sums = {}

    for file in files:
        sum = md5(open(file,'rb').read()).hexdigest()
        files_sums[file] = sum

    unique_files_amount = len(set(list(files_sums.values())))
    print(f"There are {unique_files_amount} unique files in selected directory.")

    return files_sums


def main() -> None:
    """
        Main function that's working when running the script directly.
    """
    files = walk(directory="C:/Users/werty/Downloads/Telegram Desktop/", suffix=".mp3")
    files_sums = recognise_duplicates(files)
    print(files_sums)
    #files_sums = recognise_duplicates_linux(files)



if __name__ == "__main__":
    main()
