# Part 1, Session 2 - Installing Python and Tooling


## Install Python 3.x

- Please use python.org python, not Anaconda or other distributions
 -[Download](https://www.python.org/downloads/)
 -[YouTube Video](https://www.youtube.com/watch?v=fjzwqEoFTww)

## What are "Package Managers"?

- They allow you to define the third-party libraries in your project, and reconcile their dependencies
- pip, poetry, uv, et al
- This variety of options is typical of open-source
- "Dependency Hell" is where you have incompatible library versions
- By comparison, the Java ecosystem has both Maven and Gradle
- The DotNet ecosystem is much simpler

## Install the uv package manager

- This is a modern and very fast python project manager, implemented in Rust
- It is much faster than the pip tool
- uv is used by Microsoft for their Azure SDK for Python
 -[What is UV?](https://docs.astral.sh/uv/)
 -[Installation Instructions](https://docs.astral.sh/uv/getting-started/installation/)

## Demonstration - Creating a Python Project with uv

- If you can run the following, then you have successfully installed python and uv

```
md| uv init hello-3C, cd hello-3C
```


## pyproject.toml


```
md| inline example
```


## References

 -[venv and Virtual Environments](https://docs.python.org/3/library/venv.html)
 -[Creating Projects with uv](https://docs.astral.sh/uv/concepts/projects/init/)
 -[TOML, A config file format for humans](https://toml.io/en/)
 -[The tomllib standard library](https://docs.python.org/3/library/tomllib.html)
 -[Microsoft Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)

## Wait, what's a "Standard Library"?

- Python is a language, plus a built-in set of standard libraries that are included
 -[The Standard Libraries](https://docs.python.org/3/library/index.html)
- You can also use third-party libraries (covered in the next lesson)
# =============================================================================
