Title: Basic Webscraper
Date: 2020-11-4 5:00PM
Author: Dean
Tags: Python, Webscraper
Category: Python

##Basic Python Webscraper

In this example we will be using Beautiful Soup to parse HTML and pull out useful data. We will parse through a company job board and only extract "engineering" jobs, then return their location and a link to apply.

Here is the section of our HTML source that we want to focus on. Notice how all Engineering jobs have a department id of "24990":
---
```HTML 
<section class="level-0">
  <h2 id="24990">Engineering</h2>

  <div class="opening" department_id="24990" office_id="17113" data-office-17113="true" data-department-24990="true">
  <a data-mapped="true" href="/sidewalklabs/jobs/2402388">Director, Hardware Engineering Manager</a>
  <br/>
  <span class="location">New York</span>
</div><div class="opening" department_id="24990" office_id="17113" data-office-17113="true" data-department-24990="true">
  <a data-mapped="true" href="/sidewalklabs/jobs/2280796">Senior Systems Engineer, IoT</a>
  <br/>
  <span class="location">New York</span>
</div><div class="opening" department_id="24990" office_id="17113" data-office-17113="true" data-department-24990="true">
  <a data-mapped="true" href="/sidewalklabs/jobs/2233248">Software Engineer</a>
  <br/>
  <span class="location">New York, NY</span>
</div><div class="opening" department_id="24990" office_id="17113" data-office-17113="true" data-department-24990="true">
  <a data-mapped="true" href="/sidewalklabs/jobs/2042449">Software Engineer, Generative Design</a>
  <br/>
  <span class="location">New York, NY</span>
</div>
  
</section>
```
---
Let's start with importing requests and BeautifulSoup.
---
```python
import requests
from bs4 import BeautifulSoup
```
---
Then we can store our HTML as a BeautifulSoup object.
---
```python
url = 'https://boards.greenhouse.io/sidewalklabs#.WAfElZMrIXp'
board = requests.get(url)

soup = BeautifulSoup(board.content, 'html.parser')
```

Now we can find all instances of department 24990 and store them as a ResultSet called eng_jobs.

```python
eng_jobs = soup.find_all(department_id="24990")
```
---
Finally, we can iterate through this list and print out only the data we want to see; Job Title, Location, and a link to apply:
---
```python
for eng_job in eng_jobs:
    title = eng_job.find('a', href_="")
    location = eng_job.find('span', class_="location")
    link = eng_job.find('a')['href']

    print(title.text)
    print(location.text)
    print("https://boards.greenhouse.io{}".format(link))
    print()
```
---
Now, we should get out that looks something like this:
---
Director, Hardware Engineering Manager
New York
https://boards.greenhouse.io/sidewalklabs/jobs/2402388

Senior Systems Engineer, IoT
New York
https://boards.greenhouse.io/sidewalklabs/jobs/2280796

Software Engineer
New York, NY
https://boards.greenhouse.io/sidewalklabs/jobs/2233248

Software Engineer, Generative Design
New York, NY
https://boards.greenhouse.io/sidewalklabs/jobs/2042449
---