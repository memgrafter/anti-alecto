---
url: https://stackoverflow.com/questions/984204/shell-command-to-tar-directory-excluding-certain-files-folders
title: linux - Shell command to tar directory excluding certain files/folders - Stack Overflow
scraped_at: '2026-04-19T07:52:11Z'
word_count: 210
raw_file: raw/2026-04-19_linux-shell-command-to-tar-directory-excluding-certain-files-folders-stack-overf_9b35dec5.txt
tldr: The post asks how to create a tar archive of a directory while excluding specific full-path files/folders, and the accepted practical workaround is to `cd` into the target directory and place `tar --exclude=...` options before the source path.
key_quote: '"the --exclude=''./folder'' MUST be at the beginning of the tar command."'
durability: medium
content_type: mixed
density: high
originality: synthesis
reference_style: refer-back
scrape_quality: good
people:
- Charles Ma
tools:
- tar
- find
- rsync
libraries: []
companies: []
tags:
- tar
- shell-scripting
- backup
- file-exclusion
---

### TL;DR
The post asks how to create a tar archive of a directory while excluding specific full-path files/folders, and the accepted practical workaround is to `cd` into the target directory and place `tar --exclude=...` options before the source path.

### Key Quote
"the --exclude='./folder' MUST be at the beginning of the tar command."

### Summary
- The question is about archiving a directory while skipping certain large subfiles/subfolders that do not need to be backed up.
- The author notes that `tar --exclude=PATTERN` exists, but worries pattern matching may exclude unintended files when the goal is to ignore specific paths exactly.
- They consider using `find` to generate a long exclusion list, but say that approach becomes impractical with “tens of thousands” of files.
- They also consider a two-step workaround:
  - use `rsync --exclude-from=file` to copy only desired content into a temporary directory
  - then tar that temporary directory
- The edit records the working solution from another user:
  - first `cd` into the directory to be backed up
  - run `tar` with `--exclude` entries placed before the archive source `.`

  Example given:
  - `cd /folder_to_backup`
  - `tar --exclude='./folder' --exclude='./upload/folder2' -zcvf /backup/filename.tgz .`
- The note emphasizes a key gotcha: the `--exclude='./folder'` syntax only works correctly when the command is run from inside the directory being archived and the excludes are written relative to that location.

### Assessment
This is a practical Stack Overflow Q&A with moderate durability: the general tar exclusion technique is fairly timeless, but the exact command behavior and path handling can still be version- and invocation-dependent. It is a mixed content type, mainly tutorial/reference, with relatively high density because it includes the problem, rejected alternatives, and a concrete command example. The content is primarily a secondary source built from community advice rather than original research, so it should be treated as a refer-back reference for shell syntax rather than deep study. Scrape quality is good for the text shown, but the thread’s full discussion, comments, and any alternative answers are not included here.
