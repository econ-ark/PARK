from __future__ import annotations

import os
import xml.etree.ElementTree as ET

def consolidate_code_with_filter(
    directory: str,
    file_extension: str,
    search_word: str,
    output_file: str = "repo_prompt.xml", # Changed extension to .xml
    excluded_files: tuple[str, ...] = ("repo_prompt.py", "noxfile.py"),
):
    """Recursively finds files with a specific extension in a directory (excluding hidden dirs and specified files)
    that contain a certain word (case-insensitive) in their name, and consolidates their contents into an XML file.

    Args:
        directory: The root directory.
        file_extension: The desired file extension (e.g., "txt", "js").
        search_word: The word to search for in the filename (case-insensitive).
        output_file: The output XML file.
        excluded_files: Tuple of filenames to exclude.
    """
    root = ET.Element("repository")
    search_word_lower = search_word.lower()

    for root_dir, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for file in files:
            if (
                file.endswith(f".{file_extension}")
                and search_word_lower in file.lower()
                and file not in excluded_files
            ):
                file_path = os.path.join(root_dir, file)
                relative_path = os.path.relpath(file_path, directory)

                try:
                    with open(file_path, encoding="utf-8") as f:
                        file_content = f.read()

                    file_element = ET.SubElement(root, "file")
                    path_element = ET.SubElement(file_element, "path")
                    path_element.text = relative_path
                    content_element = ET.SubElement(file_element, "content")
                    content_element.text = file_content  # Directly insert the content

                except Exception as e:
                    print(f"Error reading or processing {file_path}: {e}")
                    file_element = ET.SubElement(root, "file")
                    path_element = ET.SubElement(file_element, "path")
                    path_element.text = relative_path
                    content_element = ET.SubElement(file_element, "error")
                    content_element.text = str(e)

    # Manual XML generation, bypassing ET's encoding
    xml_string = '<?xml version="1.0" encoding="utf-8"?>\n<repository>\n'
    for file_element in root:
        path = file_element.find('path').text
        content = file_element.find('content').text if file_element.find('content') is not None else file_element.find('error').text
        xml_string += f'  <file>\n    <path>{path}</path>\n    <content>{content}</content>\n  </file>\n'
    xml_string += '</repository>'

    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(xml_string)
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")

if __name__ == "__main__":
    target_directory = input("Enter the directory to scan: ")
    if not os.path.isdir(target_directory):
        print(f"Error: '{target_directory}' does not exist.")
    else:
        file_extension_input = input("Enter the file extension to search for (e.g., py, txt): ")
        search_word_input = input("Enter the word to search for in the filename (case-insensitive): ")
        consolidate_code_with_filter(target_directory, file_extension_input, search_word_input)
        print(f"Successfully created {'repo_prompt.xml'}")