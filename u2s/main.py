from pathlib import Path


def main():
    current_dir = Path.cwd()
    list_of_files = [x for x in current_dir.iterdir() if x.is_file()]
    print(f'In {current_dir} there is this files:')
    for x in list_of_files:
        x.rename(delete_underscore(x))
        print(x.name)


def delete_underscore(file):
    filename = str(file)
    new_filename = filename.replace('_', ' ')
    return new_filename


if __name__ == '__main__':
    delete_underscore("Git_для_профессионального_промграммиста_pdf")
    main()
