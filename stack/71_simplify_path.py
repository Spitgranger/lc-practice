def simplifyPath(path: str) -> str:
    stack = []
    #we use a stack to create the canonical path, push when encounter a directory, pop when ..
    for directory in path.split("/"):
        if directory == "..":
            if stack:
                stack.pop()
            else:
                continue
        elif directory == ".":
            continue
        elif directory == "":
            continue
        else:
            stack.append(directory)
    return "/"+"/".join(stack)

print(simplifyPath("/home//foo/"))