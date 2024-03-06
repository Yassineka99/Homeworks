!pip install scrapy
!scrapy startproject aljazeera
%cd aljazeera/aljazeera/spiders
!scrapy genspider aljaziraa https://www.aljazeera.com/
%%writefile aljazeera.py
import scrapy
class scrapaljazeera(scrapy.Spider):
  name = "aljazeera"
  start_urls=["https://www.aljazeera.com/"]
  def parse(self,response):
    news= response.css('a.u-clickable-card__link')
    cards=response.css('article.article-card--small')
    for card in cards :
      yield{'title':card.css('h3.article-card__title span::text').get(),'url':card.css('a').attrib['href']}
    for new in news :
      yield{'Title':new.css('span::text').get()}
!scrapy crawl aljazeera -o data.json
//Output
/*
  2024-02-18 09:39:42 [scrapy.utils.log] INFO: Scrapy 2.11.1 started (bot: aljazeera)
2024-02-18 09:39:42 [scrapy.utils.log] INFO: Versions: lxml 4.9.4.0, libxml2 2.10.3, cssselect 1.2.0, parsel 1.8.1, w3lib 2.1.2, Twisted 23.10.0, Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0], pyOpenSSL 24.0.0 (OpenSSL 3.2.1 30 Jan 2024), cryptography 42.0.2, Platform Linux-6.1.58+-x86_64-with-glibc2.35
2024-02-18 09:39:42 [scrapy.addons] INFO: Enabled addons:
[]
2024-02-18 09:39:42 [asyncio] DEBUG: Using selector: EpollSelector
2024-02-18 09:39:42 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2024-02-18 09:39:42 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.unix_events._UnixSelectorEventLoop
2024-02-18 09:39:42 [scrapy.extensions.telnet] INFO: Telnet Password: c450aa38950bbe6b
2024-02-18 09:39:42 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2024-02-18 09:39:42 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'aljazeera',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'aljazeera.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['aljazeera.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2024-02-18 09:39:42 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2024-02-18 09:39:42 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2024-02-18 09:39:42 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2024-02-18 09:39:42 [scrapy.core.engine] INFO: Spider opened
2024-02-18 09:39:42 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2024-02-18 09:39:42 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2024-02-18 09:39:42 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.aljazeera.com/robots.txt> (referer: None)
2024-02-18 09:39:42 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.aljazeera.com/> (referer: None)
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Qatar PM: Hamas-Is\xadrael talks ‘not very promis\xading’, truce ef\xadforts to go on', 'url': '/news/2024/2/18/qatar-pm-hamas-israel-talks-not-very-promising-truce-efforts-to-go-on'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Pak\xadistan of\xadfi\xadcial ad\xadmits in\xadvolve\xadment in rig\xadging elec\xadtion re\xadsults', 'url': '/news/2024/2/17/pakistan-official-admits-involvement-in-rigging-election-results'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Boos and cheers as Trump launch\xades $399 sneak\xaders line day af\xadter $355m fine', 'url': '/news/2024/2/18/boos-and-cheers-as-trump-launches-399-sneaker-line-day-after-355m-fine'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Thai\xadland’s ex-PM Thaksin leaves hos\xadpi\xadtal af\xadter six months in de\xadten\xadtion', 'url': '/news/2024/2/17/thailands-jailed-ex-pm-thaksin-leaves-police-hospital-witnesses-say'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Is\xadrael’s war on Gaza: List of key events, day 135', 'url': '/news/2024/2/18/israels-war-on-gaza-list-of-key-events-day-135'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Biden says he told Ze\xadlen\xadskyy he’s ‘con\xadfi\xaddent’ US will re\xadnew aid to Ukraine', 'url': '/news/2024/2/18/biden-tells-zelenskyy-hes-confident-us-will-renew-aid-to-ukraine'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'US ‘strong\xadly con\xaddemns’ vi\xado\xadlence in DR Con\xadgo af\xadter al\xadleged drone at\xadtack', 'url': '/news/2024/2/18/us-strongly-condemns-violence-in-dr-congo-after-alleged-drone-attack'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Par\xadal\xadlel sea\xadsons: How Lebanon hides from re\xadal\xadi\xadty', 'url': '/features/longform/2024/2/18/parallel-seasons-how-lebanon-hides-from-reality'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': '‘They give me com\xadfort’: In Rafah, song\xadbirds help Pales\xadtini\xadans cope with war', 'url': '/news/2024/2/17/how-the-songbirds-of-rafah-help-palestinians-cope-with-the-terror-of-war'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': '‘They killed him’: Was Putin’s crit\xadic Naval\xadny mur\xaddered?', 'url': '/news/2024/2/17/they-killed-him-was-putins-critic-navalny-murdered'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Which coun\xadtries are still fund\xading UN\xadR\xadWA amid Is\xadrael’s war on Gaza?', 'url': '/news/2024/2/17/which-countries-are-still-funding-unrwa'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'But\xadter chick\xaden bat\xadtle: How the dish brought two In\xaddi\xadan restau\xadrants to court', 'url': '/features/2024/2/17/butter-chicken-battle-how-the-dish-brought-two-indian-restaurants-to-court'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Alex\xadey Naval\xadny time\xadline: From poi\xadson\xading to prison to death', 'url': '/news/2024/2/16/hold-alexei-navalny-timeline-from-poisoning-to-prison'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Alex\xadey Naval\xadny’s wife urges world to de\xadfeat ‘hor\xadrif\xadic Russ\xadian regime’', 'url': '/program/newsfeed/2024/2/16/alexey-navalnys-wife-urges-world-to-defeat-horrific-russian-regime'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Why is a planned ground at\xadtack in Rafah caus\xading alarm?', 'url': '/program/newsfeed/2024/2/16/why-is-a-planned-ground-attack-in-rafah-causing-alarm'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'Pales\xadtini\xadans are eat\xading weeds to stay alive in Gaza', 'url': '/program/newsfeed/2024/2/16/palestinians-are-eating-weeds-to-stay-alive-in'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': 'How like\xadly is a re\xadgion\xadal con\xadflict in the Mid\xaddle East?', 'url': '/program/inside-story/2024/2/16/how-likely-is-a-regional-conflict-in-the-middle-east'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'title': '‘Systematic torture’: To be Palestinian in an Israeli prison', 'url': '/news/2024/2/18/systematic-torture-to-be-palestinian-in-an-israeli-prison'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': None}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Qatar PM: Hamas-Is\xadrael talks ‘not very promis\xading’, truce ef\xadforts to go on'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Qatar PM: Hamas-Is\xadrael talks ‘not very promis\xading’, truce ef\xadforts to go on'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Pak\xadistan of\xadfi\xadcial ad\xadmits in\xadvolve\xadment in rig\xadging elec\xadtion re\xadsults'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Boos and cheers as Trump launch\xades $399 sneak\xaders line day af\xadter $355m fine'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Thai\xadland’s ex-PM Thaksin leaves hos\xadpi\xadtal af\xadter six months in de\xadten\xadtion'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Is\xadrael’s war on Gaza: List of key events, day 135'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Biden says he told Ze\xadlen\xadskyy he’s ‘con\xadfi\xaddent’ US will re\xadnew aid to Ukraine'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'US ‘strong\xadly con\xaddemns’ vi\xado\xadlence in DR Con\xadgo af\xadter al\xadleged drone at\xadtack'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Par\xadal\xadlel sea\xadsons: How Lebanon hides from re\xadal\xadi\xadty'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': '‘They give me com\xadfort’: In Rafah, song\xadbirds help Pales\xadtini\xadans cope with war'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': '‘They killed him’: Was Putin’s crit\xadic Naval\xadny mur\xaddered?'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Which coun\xadtries are still fund\xading UN\xadR\xadWA amid Is\xadrael’s war on Gaza?'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'But\xadter chick\xaden bat\xadtle: How the dish brought two In\xaddi\xadan restau\xadrants to court'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Alex\xadey Naval\xadny time\xadline: From poi\xadson\xading to prison to death'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Alex\xadey Naval\xadny’s wife urges world to de\xadfeat ‘hor\xadrif\xadic Russ\xadian regime’'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Why is a planned ground at\xadtack in Rafah caus\xading alarm?'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Pales\xadtini\xadans are eat\xading weeds to stay alive in Gaza'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'How like\xadly is a re\xadgion\xadal con\xadflict in the Mid\xaddle East?'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': '‘The tourists have gone’: Jerusalem restau\xadra\xadteur strug\xadgles amid Gaza war'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': None}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'The tri\xadal of Kwoye\xadlo: Fate of LRA rebel com\xadman\xadder di\xadvides north\xadern Ugan\xadda'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': None}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'At Rio’s Car\xadni\xadval pa\xadrades, Yanoma\xadmi ac\xadtivists fight ‘geno\xadcide’ with sam\xadba'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': None}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Re\xadmem\xadber\xading Cousin Aamer, a nurse who loved crab, and was killed by Is\xadrael'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': None}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'In Jerusalem’s Old City, Is\xadraeli ‘siege’ forces Pales\xadtin\xadian shops to close'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': None}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': '‘Systematic torture’: To be Palestinian in an Israeli prison'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Gaza’s Nasser Hospital ‘completely out of service’ amid Israeli siege'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Boos and cheers as Trump launches $399 sneakers line day after $355m fine'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Pakistan official admits involvement in rigging election results'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Why Navalny was hated in the Kremlin and in some Western circles'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Which countries are still funding UNRWA amid Israel’s war on Gaza?'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'No victory without Rafah operation says Netanyahu, as civilians flee north'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Qatar PM: Hamas-Israel talks ‘not very promising’, truce efforts to go on'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Parallel seasons: How Lebanon hides from reality'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Russia claims capture of Avdiivka after Ukraine withdraws from key city'}
2024-02-18 09:39:42 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.aljazeera.com/>
{'Title': 'Thousands take part in pro-Palestine protests across the world'}
2024-02-18 09:39:42 [scrapy.core.engine] INFO: Closing spider (finished)
2024-02-18 09:39:42 [scrapy.extensions.feedexport] INFO: Stored json feed (58 items) in: data.json
2024-02-18 09:39:42 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 446,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 84606,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'elapsed_time_seconds': 0.294482,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2024, 2, 18, 9, 39, 42, 590490, tzinfo=datetime.timezone.utc),
 'httpcompression/response_bytes': 381054,
 'httpcompression/response_count': 2,
 'item_scraped_count': 58,
 'log_count/DEBUG': 63,
 'log_count/INFO': 11,
 'memusage/max': 98705408,
 'memusage/startup': 98705408,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2024, 2, 18, 9, 39, 42, 296008, tzinfo=datetime.timezone.utc)}
2024-02-18 09:39:42 [scrapy.core.engine] INFO: Spider closed (finished) 
*/
