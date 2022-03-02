<!-- This is a README file for a project. -->

# Metadata
- <ins>Project Owner</ins>: [@dark-teal-coder](github.com/dark-teal-coder)
- <ins>First Published Date</ins>: 2022-03-02
- <ins>Last Modified Date</ins>: 2022-03-02

# About Project 
<ins>Title</ins>: Washington Post WebScraper  
<ins>Difficulty</ins>: <span style="color: gray">Easy</span> 
<ins>Scale</ins>: Small 

# Description 
The project uses Python to scrape newspaper article content from [Washington Post](https://www.washingtonpost.com/). The article used here is *["87 percent of websites are tracking you. This new tool will let you run a creepiness check"](https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/)* and the scraped items are the newspaper article title, author, date and body. The original idea is taken from *["Web scraper to get news article content"](https://www.codementor.io/projects/tool/web-scraper-to-get-news-article-content-atx32d46qe)* by [DevProjects](https://www.codementor.io/projects) [@codementor](https://www.codementor.io/@codementor). 

# Installation 

## Tools
- Text Editor or Integrated Development Environment (IDE)
  - You can [download the famous text editor Notepad++](https://notepad-plus-plus.org/downloads/). 
  - Or, you can [download the popular IDE Visual Studio Code (VS Code)](https://code.visualstudio.com/download). 
- Python 3
  - You can [install Python 3 from python.org](https://www.python.org/downloads/). 
- Python Package Installer/Manager `pip`
  - If you installed Python from [python.org](https://www.python.org/), you should already have `pip`. If it is not installed, you can use the command `py -m ensurepip --default-pip` to bootstrap it from the standard library. If you are using Linux, you will have to [install the package manager separately](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/). You can find out more about the `pip` tool [here](https://pip.pypa.io/en/stable/getting-started/). 
- Command-line interface (CLI) 
  - You can [install the open-source PowerShell on Windows, Linux and macOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) if you do not have or want to use a pre-installed CLI on your local machine. 

## Description
Check if you have Python installed using the command `python --version`, or simply, `python version`, in the CLI. [Git-clone the project repository from Github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to the local machine. Use the command `py -m pip install package_name` to install the necessary Python libraries. Check out [pip documentation](https://pip.pypa.io/en/stable/cli/pip_install/) to learn more about `pip install`. Check the top part of the `.py` script file for the list of libraries required. For example, you may need `requests` and `beautifulsoup4` libraries if you see the following lines in the top part of the script file: 
```
import requests
from bs4 import BeautifulSoup
```
If `pip` fails to locate the relevant packages, you may find it at [Python Package Index (PyPI)](https://pypi.org/). Use `python file_name.py` to run the script in a CLI. Or, use an IDE, such as VS Code, to run the script. There will usually be a [Run] button in the top right corner of the opened script file. 

# Credits 

## Contributors 
1. [@dark-teal-coder](github.com/dark-teal-coder)

## References 
### Lecture Materials:
N/A
### Data: 
1. 87 percent of websites are tracking you. This new tool will let you run a creepiness check: https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/
### Documentations: 
N/A
### Tutorials: 
2. XPath Tutorial: https://www.w3schools.com/xml/xpath_intro.asp
3. Beautiful Soup: Build a Web Scraper With Python: https://realpython.com/beautiful-soup-web-scraper-python/
### Solutions: 
N/A
