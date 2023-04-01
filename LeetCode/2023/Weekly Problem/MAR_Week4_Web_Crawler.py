# https://leetcode.com/problems/web-crawler/

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        queue, result = [startUrl], set([startUrl])
        name = startUrl.split('/')[2]

        while queue:
            url = queue.pop(0)
            for x in htmlParser.getUrls(url):
                if x not in result and name == x.split('/')[2]:
                    result.add(x)
                    queue.append(x)

        return list(result)
