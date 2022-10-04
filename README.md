# getLoincDescription

I wrote this quickly out of necessity. My job required me to upload 150+ LOINC codes into a database, however, I didn't have any descriptions. Searching LOINC.org for each LOINC was not an option. My search of their website turned up their API so I knew what I had to do. This is very simple and was written to meet my needs but could be easily modified to display any and all information about the LOINC code.

You'll need a free account on LOINC.org to use the API.

Once you have your credentials, create a .env file that looks like this:

```
UN=username
PW=strong password
```

Install the dependencies:

```
py -m pip3 install -r requirements.txt
```

or equivalent command for your environment.

and finally:

```
py lookup_loinc.py
```

Again, I wrote this quickly in a pinch for my day job so there is minimal error checking.
