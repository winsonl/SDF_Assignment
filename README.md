# Winson Li Submission


## Thought Process
To preface this, I have not really worked with building web APIs in production for fun or during my work experience. In order for me to start thinking about what libraries to use; I thought about what libraries I could use to make this easier and more readible. 

The one thing I knew about building web api's involved flask and flask is in python, so decided to go with that. Since we only have 2 hours to build this "web api" and provide documentation I went through some simple flask builiding examples and went through documentation here: https://flask-restful.readthedocs.io/en/latest/

I used several other libraries to help me such as requests, and several libraries from flask_restful to make this solution simiplier, such as not hardcoding the json data for the response text and using builtin python functions to get the time needed to extend the timeout. 

## How to Run
```sh
>> python app.py
>> curl -X POST -H "Content-Type: application/json" -d '{"name":"recipe", "expires_in": 30, "snippet":"1 apple"}' http:{default host given}/snippets
```

## Production Concerns
I don't think I would ever implement this into production without major code review and debugging sessions. The expected result from the curl POST command outputted a string instead of a JSON. There was some issue parsing the data on my end and did not have time to troubleshoot the error due to the time constraints. (Note figured it out couple minutes afterwards regarding the resulting text)

```sh
curl -X POST -H "Content-Type: application/json" -d '{"name":"recipe", "expires_in": 30, "snippet":"1 apple"}' http://127.0.0.1:5000/snippets
{"url": "https://example.com/snippets", "name": "recipe", "expires_at": "2022-05-27 18:39:20.892242", "snippet": "1 apple"}
```

## Error Handling
Error handling was handled by the request parser, making the name, expires_in and snippet arguments required. There could have been some errors bundled together and handled all at once if the arguements took a while to process, it'd be easier to just spit out the errors all at once to the client.

## Things that did not work
I tried making use of the request library post function to make the POST request to a web page, and return the response text, however I could not get that to work. If I were to successfully implement it, it would then have added the x number of seconds to the timeout. Wasn't sure how to get the api to have a 'https://' host, so everything was tested with the default host that the app was running on.

## Improvement
Spend some time figuring out the requests.post() to work in order to extend the timeout. 
