#from github import Github

#async def async_(it, *args):
#    return (await asyncio.get_event_loop().run_in_executor(None, it, *args))

import asyncio
import aiohttp
import async_timeout
import json

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def fetch_tags(owner,repo):
    url = "https://api.github.com/{}/{}/tags".format(owner, repo)

    async with aiohttp.ClientSession(loop=asyncio.get_event_loop()) as session:
        response = await fetch(session, url)

        data = json.loads(response)

        tag = data[0]['name']
        zipball_url = data[0]['zipball_url']

    #    tag = "foo"
    #    zipball_url = "bar"
        return tag, zipball_url


async def check_update():
#    g = Github()
#    repo = g.get_user('FAForever').get_repo('client')
#
#    print("getting tags")
#    tags = repo.get_tags()
#
#    tag = tags[0]
#
#    zipball_url = tag.zipball_url

    tag = "foo"
    zipball_url = "bar"

    return tag, zipball_url



