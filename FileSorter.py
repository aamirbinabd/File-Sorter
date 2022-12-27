import os
import shutil

def sort_file(filename, origin_dir, destination_dir):
  # Get the file extension of the current file
  file_extension = filename.split('.')[-1]

  # Set the destination folder path based on the file extension
  destination = f'{destination_dir}/{file_extension}'

  # If the destination folder does not exist, create it
  if not os.path.exists(destination):
    os.makedirs(destination)

  # Move the file to the destination folder
  shutil.move(f'{origin_dir}/{filename}', f'{destination}/{filename}')

def main():
  # Get the origin and destination directory from the user
  origin_dir = input('Enter the path to the origin directory: ')
  destination_dir = input('Enter the path to the destination directory: ')

  # Get a list of all the files in the origin directory
  files = os.listdir(origin_dir)

  # Iterate over the list of files
  for filename in files:
    sort_file(filename, origin_dir, destination_dir)

if __name__ == '__main__':
  main()

