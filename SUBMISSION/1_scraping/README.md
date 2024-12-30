### Folder structure

`dataset_finding`
- Has the notebooks and the data to produce the table of how many papers were found relating to our topic, 'Scrapes_All.csv'

`x_research_papers_save`
- Contains the notebooks and all the data in order to get the full texts from the papers we found in 'Scrapes_All.csv'

 `x_research_papers_save\1_raw_files`
 - contains papers in html from science direct

### TO Run:
1) Run the 6 notebooks in "dataset_finding" in ascending order and then the merge notebook. This creates 'Scrapes_All.csv' in the 1_scraping folder.
2) Run the notebooks in "x_research_papers_save" in ascending order. This will produce 3 files in the "xx_results" which contain the full texts from each source.
3) Run the "AllFullTextsTOCSV" notebook to merge the 3 files produced in the previous step into "FullTextscrapes.csv" which will be under the "/1_scraping/" folder




```
 📦1_scraping
 ┣ 📂1_scrapers
 ┣ 📂xx_results
 ┃ ┗ 📜01_scraped_papers.csv
 ┣ 📂x_research_papers_save
 ┃ ┣ 📂1_raw_files
 ┃ ┣ 📜01_scraper_science_direct.ipynb
 ┃ ┣ 📜headers.py
 ┃ ┗ 📜sciencedirect_papers_status.csv
 ┣ 📜nothing.txt
 ┗ 📜README.md
```
