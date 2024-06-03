# Description

This is an educational project developed during Python Academy GlobalLogic in 2024. The project contains Jmeter automated tests.

### Issue
Business has observed that sometimes posts of a second user per current day are missing.

To reproduce:
1. Get the user list from https://gorest.co.in/public/v2/users and find the second user's ID from the list. If the second user is not found, use default ID-10
2. Get user details from https://gorest.co.in/public/v2/users/{id}
3. Get user posts from https://gorest.co.in/public/v2/users/{id}/posts

Expected behavior:

- empty list in the user's post response

Unexpected behavior:

- "Resource not found" response

Additional requirements:

- generate 1 summary report. The data format in report should be mm-dd-yyyy,
- total time to process all requests/threads 46-60sec, 2 users, 3 loops,
- there are no limitations in number of extra requests/threads.


## How to set up the environment locally

### Apache Jmeter installation:
- Install Java - https://www.java.com/en/download/manual.jsp
- Install Apache Jmeter - https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.6.3.zip

### How to run Apache Jmeter
- After unpacking the jmeter .zip file - open your_location_to_jmeter/apache-jmeter-5.6/bin
- Run `jmeter` file (.bat extention)
- Open File -> `test_second_user.jmx`
- Edit `Simple Data Writer` in Test Plan and set where to write the results (your local path)
- Press "Start"

## How to reformat `results` report created by jmeter
To reformat *timeStamp* data to *mm-dd-yyy* format in generated report - `results.csv`, you need to run python script, which generates `reformatted_results`.csv file.

### How to run Python script for reformatting the report
Install:
- Python version 3.11.7 - https://www.python.org/downloads/
- Create virtual environment - https://docs.python.org/3/library/venv.html

Run:

 `scripts/reformat_results.py`

## Structure of framework
`test-plans` - Test plan files used by Apache Jmeter app.

`results` - Jmeter's generated testing results

`scripts` - Reports' postprocessing Python scripts
