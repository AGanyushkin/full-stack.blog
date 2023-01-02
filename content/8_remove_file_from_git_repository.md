Title: Remove file from git repository
Date: 2022-02-19 21:00
Category: tools
Tags: git
Author: Andrey G
Status: published
Summary: git remove files from repository entirely
Lang: en
---

Sometimes we need to remove file from git repository, completely remove from repository. For example it can be property file with passwords 🙂

# just remove

this approach will remove file from head of repository, but we still can have access to passwords in history commits.

```shell
git rm application.properties
git commit --amend --no-edit
```

# completely remove

To completely remove file from repository

```shell
git filter-branch --tree-filter 'rm -f application.properties' HEAD
```

it will remove “application.properties” from every commit, but it will <span style="color:red">rewrite all history</span>

use `--prune-empty` to remove empty commits

use `git push --force` to push changes

also can be used as

```shell
git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch application.properties' --prune-empty --tag-name-filter cat -- --all
```

# other approaches

One more way to remove file from git, but keep it on filesystem:

```shell
git rm --cached application.properties
echo application.properties >> .gitignore
git add .gitignore
git commit --amend --no-edit
```

🙂

