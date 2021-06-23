 # Getting Synthetic Data
 
 
To train a model, you need images. You can most certainly download them by hand, possibly even somewhere in batch, but I think there is a much more enjoyable way. We have  used Python and some web scraping techniques to download images from google images.

## Using [Selenium]((https://selenium-python.readthedocs.io/))


Selenium can be used to automate web browser interaction with Python (also other languages). In layman’s term, selenium pretends to be a real user, it opens the browser, “moves” the cursor around and clicks buttons if you tell it to do so. The initial idea behind Selenium, as far as I know, is automated testing. However, Selenium is equally powerful when it comes to automating repetitive web-based tasks.

Here’s a little rundown of the steps I took in order to scrape the images using Selenium-

* Getting ChromeDriver.
The first step will be to get your version of Chrome that you are currently running. Go to Chrome settings, then click “About Chrome” at the bottom of the sidebar. It’ll display your current version. Proceed to the [ChromeDriver](https://chromedriver.chromium.org/downloads) link to download, which is needed to run with Selenium. It’ll tell you which version to download based on your current Chrome version. Unzip that to get the chromedriver.exe.

* Show hidden files — usr/local/bin
With ChromeDriver downloaded, you will need to place it in a hidden folder. The typical way to show hidden folders in your Finder window is typing Cmd + Shift + . (dot).

* Use Selenium in your notebook.
Set up and import.
Now in a Jupyter notebook, you can pip install selenium, and import webdriver, then instantiate it.
Then, just run the code in the notebook. It will give you two prompts-

1) What do you want to search for?
2) How many images do you want?




## Using [Parsehub](https://www.parsehub.com/)

Automatic web scraping can be simple but also complex at the same time. But once you understand and get the hang of it, it’ll become a lot easier to understand. For this project, we are going to extract images using  ParseHub. 

First, download Parsehub.You’ll need to set up ParseHub on your desktop so here’s the guide to help you: [Downloading and getting started](https://help.parsehub.com/hc/en-us/articles/115002520634-Lesson-1-Downloading-and-Getting-Started)

Once ParesHub is ready, we can now begin scraping data.

1. Open up ParseHub and create a new project by selecting “New Project”
   will put img here
   
2. Copy the URL and place it in the text box on the left-hand side and then click on the “Start project on this URL” button.
   will put image here
   
3. Once the page is loaded on ParseHub there will be 3 sections:

   Command Section
   The wbe page you're extracting from
   Preview of what the data will look like
   
 The command section is where you will tell the software what you want to do, whether this is a click making a selection, or the advanced features ParseHub can do.

4. To begin extracting data, you will need to click on what exactly you want to extract, in this case, image titles. Click on the first image title you see.
Once clicked, the selection you made will turn green. ParseHub will then make suggestions of what it thinks you want to extract.
The suggested data will be in a yellow container. Click on a title that is in a yellow container then all image titles will be selected. 
   Scroll down a bit to make sure there is no blog title missing.

Now that you have some data, you can see a preview of what it will look like when it's exported.

5. Let’s rename our selection to something that will help us keep our data organized. To do this, just double click on the selection, the name will be highlighted and you can now rename it. 

Now that all image titles are selected.

6. On the left sidebar, click the PLUS (+) sign next to the blog name selection and choose the Relative Select command.

7. Now that we have everything we want to be extracted; we can now let ParseHub do its magic. Click on the “Get data” button.

8. You’ll be taken to this page.
   insert image here
   
You can test your extraction to make sure it’s working properly. For bigger projects, it is  recommended doing a test run first. But for this project let's press “run” so ParseHub can extract the online data.

9. This project shouldn’t take too long, but once ParseHub is done extracting the data, you can now download it and export it into a CSV/Excel, JSON, or API. But we just need a CSV/ Excel file for this project.
  insert img here
  
  
