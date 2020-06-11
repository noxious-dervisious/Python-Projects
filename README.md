## Webscrapping

### Introduction - 
**Web Scraping** (also termed Screen Scraping, Web Data Extraction, Web Harvesting etc.) is a technique employed to extract large amounts of data from websites whereby the data is extracted and saved to a local file in your computer or to a database in table (spreadsheet) format.

### Objective - 
Here we are performing a basic webscrapping on the well known website IMDB and we are scapping in all the data regarding the upcoming movies and the top rated movies using [**BeautifulSoup**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - a well known Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.

### Prerequisite - 
```python
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
from subprocess import call
```
These are some of the external py libraries we will be using through out these programs.
