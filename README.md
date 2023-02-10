# web-scraping-wos
----------------------

A Python tool to perform systematic literature reviews from searching on Web of Science (WoS), get useful information (title, author, year, citations, abstract, and journal) and save it in tables (.csv). These codes thus enable dynamic web scraping of WoS, leveraged by `selenium` and statically parsed by `beautifulsoup4`.

## Getting started
-----------------------
### Setting up environment
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


## Debugging
-------------------
### "The code won't start"
Try re-running the code two or tree times. This is because the first cookie prompted by Web of Science may take some time to show up depending on your internet speed.

### "Some abstracts are missing"
This is currently a limitation of the tool and is under investigation. The code automatically scrolls and clicks on the button "Show More", which allows for opening the abstract and thus subsequent parsing of the html. However, the WoS server often notices this systematic behavior and blocks the automated clicking.

### "Why is it so slow?"
Web scraping needs is a beautiful way to extract publicly available that otherwise would need to be done manually and take an eternity. However, any scraping method needs to have sleep times throughout the code (the well-known `time.sleep()`) in order to safely interact with the host's server. If multiple requests are sent simultaneously, the host's server can be compromised and the scraping might damage its functioning. Thus, don’t find it strange that the scraping is taking hours, this is how it should happen.
