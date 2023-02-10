# web-scraping-wos
----------------------

A Python tool to perform systematic literature reviews from searching on Web of Science, get useful information (title, author, year, citations, abstract, journal) and save it in tables (.csv).

## Getting started
-----------------------
### Setting up environment
To run this tools, you'll need to setup a Python environment and install the necessary packages. You can do so by following these steps:
- Make sure you have [Firefox](https://www.mozilla.org/en-US/firefox/new/) installed
- Clone this repository 
- Open the [Anaconda](https://docs.anaconda.com/anaconda/install/index.html) prompt and create a new environment with ``conda create -n <env_name> python=3.9`` oruse virtualenv (for Linux machines) with ``python3 -m venv /path/to/new/virtual/environment``
- cd (change directory) into this repository and install the necessary packages (in the `requirements.txt`):
``pip install -r requirements.txt``

### Running the code
- Once your environment is ready, you can either:
    1. Configure your IDE (e.g., PyCharm) to use the created environment, or 
    2. Activate the environment and run the code through the Anaconda Prompt. To run the code through Anaconda, don't forget to activate the environment by: ``conda activate <env_name>``, cd into your directory containing your script that call the scraper functions, and run the codes by ``python <script_name.py>``. 

- For setting up your search on Web of Science, follow the example provided in the `/example/` folder
- The codes will prompt first a firefox window and then it will keep opening new windows, each for a certain pagination stemming from the web search. You can close them all manually (except for the last-opened window, which is being dynamically scraped) or supress their opening with function arguments of the function `scroll_and_click_showmore` of the module `setup_page`.


