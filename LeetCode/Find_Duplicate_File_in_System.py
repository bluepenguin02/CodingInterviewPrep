"""
609. Find Duplicate File in System

Given a list paths of directory info, including the directory path, and all the files with contents in this
directory, return all the duplicate files in the file system in terms of their paths. You may return the
answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"
It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content)
respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the
directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of
the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"
"""


from collections import defaultdict

def duplicate_files(paths: list) -> list:
  all_files = defaultdict(list)
  duplicates = []

  for dir in paths:
    tokens = dir.split(' ')
    path = tokens[0]
    for file in tokens[1:]:
      par_start = file.index('(')
      par_end = file.index(')')
      fname = file[:par_start]
      content = file[par_start+1:par_end]
      all_files[content].append(path+'/'+fname)

  for files in all_files.values():
    if len(files) > 1:
      duplicates.append(files)

  return duplicates

if __name__ == '__main__':
  print(duplicate_files(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))