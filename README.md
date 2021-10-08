# GHC Archive
Scraper to help understand GHC sponsor values
----

### Environment Setup
Open up Anaconda Powershell. Go to your project directory using `cd Path\to\project.` 
Run `conda create --name web_scraper` to create a new python environment called `web_scraper.` Alternatively, you can use Anaconda if you prefer using a GUI. Then run `conda activate web_scraper` and you should see `(web_scraper)` at the beginning of every line in the terminal. You've entered your python environment for our project.


The reason of using this environment is to contain library dependents that are specific to our project. This way if you are working on multiple projects that
use libraries of different versions, there won't be any conflicts!  

Now to actually import the libraries run `pip install -r requirements.txt.` Note that if `pip` is not recognized, then run `conda install pip` before running `pip install...` 

---
### Core Values
<img src='word_cloud.PNG' title='word_cloud' width='' alt='word_cloud' />
