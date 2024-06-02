# Description

This is an educational project owned by Weronika Strzelczyk. It is in development, during Python Academy GlobalLogic in 2024. The project contains automated tests in Jmeter.

### Task details
Business observed that sometimes posts of a second user per current day are missing.

To check this, You should:

Create 3 requests:
1. First request - should open https://gorest.co.in/public/v2/users and find second user on page (no id2, but second from the page)
2. Second request - should open single user info (second user from previous request, if second user not found , use default id - 10)
3. Third request - should open a single post page of the "second" user. Response shouldn’t contain “Resource not found" message.
4. Generate 1 summary report for all requests. Data format in report should be mm-dd-yyyy
5. Total time to process all requests/threads 46-60sec
2 users, 3 loops.
There are no limitations in number of extra requests/threads


## How to set up the environment locally

### Apache Jmeter installation:
- Install Java - https://www.java.com/en/download/manual.jsp
- Install Apache Jmeter - https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.6.3.zip

### How to run Apache Jmeter
- After unpacking the jmeter .zip file - open your_location_to_jmeter/apache-jmeter-5.6/bin
- Run `jmeter` file (.bat extention)
- Open File -> `test_second_user.jmx`
- Press "Start"

## How to reformat `results` report created by jmeter
To reformat *timeStamp* data to *mm-dd-yyy* format in generated report - `results.csv`, you need to run python script, which generates `reformatted_results`.csv file.

### How to run Python script for reformatting the report
Install:
- Python version 3.11.7 - https://www.python.org/downloads/
- Create virtual environment - https://docs.python.org/3/library/venv.html
- Run `scripts/reformat_results.py`

## Structure of framework
`test-plans` - Test plan files used by Apache Jmeter app.

`results` - Jmeter's generated testing results

`scripts` - Reports' postprocessing Python scripts

 ## Other info
 Ignored folders for git:
 - `venv`