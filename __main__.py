import os
import argparse
import shutil


def copy_template_folder(new_folder_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_folder = os.path.join(script_dir, "template")
    dest_folder = os.path.join(script_dir, new_folder_name)

    if not os.path.exists(src_folder):
        raise FileNotFoundError(f"'template' folder not found in {script_dir}.")

    if os.path.exists(dest_folder):
        print(f"Destination folder '{dest_folder}' already exists. Deleting it.")
        shutil.rmtree(dest_folder)

    shutil.copytree(src_folder, dest_folder)
    print(f"📁 Folder copied from 'template' to '{new_folder_name}'.")
    return dest_folder

def replace_words_in_file(
    file_path, 
    NAME_CAPITALIZED_SINGULAR,
    NAME_LOWER_SINGULAR,
    NAME_CAPITALIZED_PLURAL,
    NAME_LOWER_PLURAL
):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace both "Entities" and "Entity" (Entities first to avoid double replacement)
        content = content.replace("NAME_CAPITALIZED_SINGULAR", NAME_CAPITALIZED_SINGULAR)
        content = content.replace("NAME_LOWER_SINGULAR", NAME_LOWER_SINGULAR)
        content = content.replace("NAME_CAPITALIZED_PLURAL", NAME_CAPITALIZED_PLURAL)
        content = content.replace("NAME_LOWER_PLURAL", NAME_LOWER_PLURAL)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✏️  Updated: {file_path}")
    except Exception as e:
        print(f"⚠️  Skipped: {file_path} (Reason: {e})")

def process_folder(
    folder_path, 
    NAME_CAPITALIZED_SINGULAR,
    NAME_LOWER_SINGULAR,
    NAME_CAPITALIZED_PLURAL,
    NAME_LOWER_PLURAL
):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pyc"):
                continue  # Skip .pyc files
            
            file_path = os.path.join(root, file)
            replace_words_in_file(
                file_path,
                NAME_CAPITALIZED_SINGULAR,
                NAME_LOWER_SINGULAR,
                NAME_CAPITALIZED_PLURAL,
                NAME_LOWER_PLURAL
            )

def make_plural(word: str) -> str:
    """
    Returns the plural form of a given English word (basic rules).
    """
    if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + 'es'
    elif word.endswith('y') and word[-2] not in 'aeiou':
        return word[:-1] + 'ies'
    elif word.endswith('f'):
        return word[:-1] + 'ves'
    elif word.endswith('fe'):
        return word[:-2] + 'ves'
    else:
        return word + 's'

def rename_files_and_folders(folder_path, replacement_word):
    # Rename files and folders bottom-up to avoid path issues
    for root, dirs, files in os.walk(folder_path, topdown=False):
        # Rename files
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = file
            new_file_name = new_file_name.replace("entity", replacement_word.lower())

            if new_file_name != file:
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"🔁 Renamed file: {old_file_path} → {new_file_path}")

        # Rename directories
        for dirname in dirs:
            old_dir_path = os.path.join(root, dirname)
            new_dir_name = dirname
            new_dir_name = new_dir_name.replace("entity", replacement_word.lower())

            if new_dir_name != dirname:
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(old_dir_path, new_dir_path)
                print(f"📁 Renamed folder: {old_dir_path} → {new_dir_path}")

def ToCamelCase(text: str, separator: str = ' '):
    words = text.strip().split(separator)
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def main():
    parser = argparse.ArgumentParser(description="Example script with command-line arguments.")
    
    # Define a command-line argument: --entity
    parser.add_argument('--entity', type=str, required=True, help='Entity in singular used')
    parser.add_argument('--separator', type=str, required=False, help='Separator used for entity with several words in its name.')

    # Parse the arguments from the command line
    args = parser.parse_args()

    separator = args.separator if args.separator else " "
    
    entity_name = args.entity.lower()
    entity_name_plural = make_plural(entity_name)
    # Use the argument
    print(f"Creating field for {entity_name}")

    entity_name_capitalized = ToCamelCase(entity_name)
    entity_name_plural_capitalized = ToCamelCase(entity_name_plural)

    NAME_CAPITALIZED_SINGULAR = entity_name_capitalized
    NAME_LOWER_SINGULAR = entity_name.replace(" ", "_")
    NAME_CAPITALIZED_PLURAL = entity_name_plural_capitalized
    NAME_LOWER_PLURAL = entity_name_plural.replace(" ", "_")
    
    print("================================================")
    print(f"NAME_CAPITALIZED_SINGULAR: {NAME_CAPITALIZED_SINGULAR}")
    print(f"NAME_LOWER_SINGULAR: {NAME_LOWER_SINGULAR}")
    print(f"NAME_CAPITALIZED_PLURAL: {NAME_CAPITALIZED_PLURAL}")
    print(f"NAME_LOWER_PLURAL: {NAME_LOWER_PLURAL}")
    print("================================================")

    
    # new_folder_name = NAME_LOWER_SINGULAR
    # replacement_word = NAME_LOWER_SINGULAR

    # try:
    #     dest_folder = copy_template_folder(new_folder_name)
    #     rename_files_and_folders(dest_folder, replacement_word)
    #     process_folder(
    #         dest_folder,
    #         NAME_CAPITALIZED_SINGULAR,
    #         NAME_LOWER_SINGULAR,
    #         NAME_CAPITALIZED_PLURAL,
    #         NAME_LOWER_PLURAL
    #     )
    #     # print("✅ All files processed and renamed successfully.")
    # except Exception as e:
    #     print(f"❌ Error: {e}")

 
 
if __name__ == "__main__":
    main()
