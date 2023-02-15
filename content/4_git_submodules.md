Title: GIT Submodules
Date: 2022-01-22 21:00
Category: tools
Tags: git, submodules
Author: Andrey G
Status: published
Summary: GIT Submodules
Lang: en
---

[TOC]

Git submodules is not simple approach to use to store your code. But this technic is pretty useful then you need to make changes in your project and in shared libraries, or if you would like to use shared libraries or other piece of code directly from your code without builded shared artefacts, libraries etc…

# What is this the git submodule?

It is situation when some git repository, for example “shared_library” added directly in your “application” repository as a subdirectory. For you it seems like you just have “shared_library” in your repository and you can use assets from “shared_library” directly from “application”. But “shared_library” still is a different git repository.

# How we can add submodule?

For example we have:

```text
"applciation" - our application
"shared_library" - our library, will be used as git submodule
```

and finally we would like to have this structure
```text
application/
    my_application.py
    shared_library/
        __init__.py
        best_library.py
```

let’s add submodule to “application” repository. go to “application” repository and run
```shell
git submodule add git@github.com:User/shared_library.git
```

commit changes which will contain information about submodule

After that your application will be linked with desired checkpoint/commit in submodule. Of course you can change this checkpoint in future.

All information about submodules in your “application” repository will be stored in `.gitmodules` file

```text
[submodule "shared_library"]
	path = shared_library
	url = git@github.com:User/shared_library.git
```

> **Note**
>
> If you will remove submodule directory you don’t loose information about submodule because it stored in `.git` directory of your parent repository

Also you can specify which branch (default it is master) from submodule repository will be linked to our repo. Can be configured in `.gitmodules`

```text
[submodule "shared_library"]
	path = shared_library
	url = git@github.com:User/shared_library.git
	branch = master
```

# What if you are going to clone the repository with submodules?

**case 1**

Right after cloning of your parent repository all submodule directories will be empty.

To get submodules you need to use these commands

```shell
# to initialise submodule local configuration
git submodule init

# to get submodule and checkout required checkpoint in submodule
git submodule update
```

**case 2**

use this command to clone parent repository and all submodules recursively

```shell
git clone --recurse-submodules https://github.com/User/Applciation
```

**case 3**

you can perform update with submodule initialisation `git submodule update --init`

or use `git submodule update --init --recursive` to initialise all submodules recursively

# What if you would like to get latest version for submodule code?

Got to submodule directory and execute

```shell
git fetch & git merge
```

But you can use more simplest way to update submodules automatically with commands which are placed below

```shell
# for all submodules
git submodule update --remote

# for one submodule
git submodule update --remote shared_library

# also rebase and merge can be used
git submodule update --remote --rebase
git submodule update --remote --merge
```

Or you can pull changes for parent repository with changes for submodules

```shell
git pull --recurse-submodules
```

# How to check changes in submodules?

```shell
# To show short summary
git config status.submodulesummary 1

# or
git diff --submodule
```

# What if you have some changes in your parent repo and in submodule?

You can commit it separately. First for submodule and after that for parent repository. Or your can use push command with option

this command will check if there is no local (which still not pushed changes) in your submodules and push your parent repository or fail

```shell
git push --recurse-submodules=check

# to push all changes, first submodules and after that parent repository you can use
git push --recurse-submodules=on-demand
```

can be configured with: `git config push.recurseSubmodules on-demand` or `git config push.recurseSubmodules check`

# Interesting abilities

We can run any git commands for each submodules like this:

```shell
git submodule foreach 'git stash'
```

# Conclusion

It is a powerful way to manage your code. But I think it is very exceptional situations when submodules can be used. Because it is not so easy to use submodules, it requires additional manipulations with git and additional attention to keep all code in consistent state.

