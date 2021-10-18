import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')

doc = lxml.html.fromstring(html.content) #HtmlElement

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0] #returns list of all the divs in the html page with this id
# // these double slashes tell lxml that i want search for all tags in html doc
# / returns only immediate child tags/nodes which match requirements
# div -> we are searching for divs
# @id etc - obvious

titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')

# print(titles)

prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

 #text_content() zwraca html text bez html tagów

tags = [tag.text_content() for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]')]

tags = [tag.split(', ') for tag in tags]

#now its the time for platform

platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

#returning json response and we turn it into web-based API

output = []

for info in zip(titles, prices, tags, total_platforms): #zip: iteruje przez te wszystkie listy
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)

print(output)




# . -> only children of new_releases
# /text() -> returns text