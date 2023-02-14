# web-scraping-wos
----------------------

A Python tool to perform systematic literature reviews from searching on Web of Science (WoS), get useful information (title, author, year, citations, abstract, and journal) and save it in tables (.csv). These codes thus enable dynamic web scraping of WoS, leveraged by `selenium` and statically parsed by `beautifulsoup4`.

## Getting started
-----------------------
### Setting up the Python environment
To run this tool, you'll need to setup a Python environment and install the necessary packages. You can do so by following these steps:
- Make sure you have [Firefox](https://www.mozilla.org/en-US/firefox/new/) installed
- Clone this repository 
- Open the [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) prompt and create a new environment with ``conda create -n <env_name> python=3.9`` or use virtualenv (for Linux machines) with ``python3 -m venv /path/to/new/virtual/environment``
- cd (change directory) into this repository and install the necessary packages (in the `requirements.txt`):
``pip install -r requirements.txt``

### Running the code
- Once your environment is ready, you can either:
    1. Configure your IDE (e.g., PyCharm) to use the created environment, or 
    2. Activate the environment and run the code through the Anaconda Prompt. To run the code through Anaconda, don't forget to activate the environment by: ``conda activate <env_name>``, cd into your directory containing your script that call the scraper functions, and run the codes by ``python <script_name.py>``. 

- For setting up your search on Web of Science, follow the example provided in the `/example/` folder
- The codes will prompt first a firefox window and then it will keep opening new windows, each for a certain pagination stemming from the web search. You can close them all manually (except for the last-opened window, which is being dynamically scraped) or supress their opening with function arguments of the function `scroll_and_click_showmore` of the module `setup_page`.

## Usage
--------
Currently, this tool is not yet packaged (no pip install). Thus, to call the modules, you can easily use the `\example\` folder and use it as template for your project. Go to `main.py`and adapt the code as following:

   ```python
   from wos_scraper import setup_page
   from wos_scraper import parse_soup
   
   # Grovide the link to the search, for instance:
   search = 'https://www.webofscience.com/wos/woscc/summary/ff7d7f65-1ac6-4213-b788-f3caf673d7fd-6c336e02/relevance/1'

   # Get and save htmls of each pagination from 1 to 49.
   # This code line will save the html files corresponding to each page 
   # (from 1 to 49 in this case) in the same folder.
   html_list, html_save_files = setup_page.get_html_through_paginations(search, range(1, 50))  
   
   # Parse htmls and produce tables with author, title, abstracts, etc
   # Here, the html files will be parsed and tables for each html will be saved in the current folder.
   for f in html_save_files:
        htmlfile = open(f, 'r', encoding='utf-8').read()
        df = parse_soup.parse_html_get_table(htmlfile)
        df.to_csv('df-{}.csv'.format(f))
   ```


## Troubleshooting
-------------------
### "The code won't start"
Try re-running the code two or tree times. This is because the first cookie prompted by Web of Science may take some time to show up depending on your internet speed.

### "Some abstracts are missing"
This is currently a limitation of the tool and is under investigation. The code automatically scrolls and clicks on the button "Show More", which allows for opening the abstract and thus subsequent parsing of the html. However, the WoS server often notices this systematic behavior and blocks the automated clicking.

### "Why is it taking so long?"
Web scraping is an elegant way to extract publicly available that otherwise would need to be done manually and take an eternity. However, any scraping method needs to have sleep times throughout the code (the well-known `time.sleep()`) in order to safely interact with the host's server. If multiple requests are sent simultaneously, the host's server can be compromised and the scraping might damage its functioning. Thus, don’t find it strange that the scraping is taking hours, this is how it should happen.

### "Stopped scraping at pagination p"
If you were running the code to loop through n pages (``range(1, n+1)``) and the program is terminated at certain page p, simply restart the function ``setup_page.get_html_through_paginations()`` setting the arg ``pags`` to ``range(p, n+1)``. That will continue the web scraping and then you can parse the htmls with ``parse_soup.parse_html_get_table()``.


## Submit an issue!
-------------------
Please submit your issues, possible improvements, and bugs by openning an [issue](https://github.com/beatriznegreiros/web-scraping-wos/issues). Answers should not take more than a day.
