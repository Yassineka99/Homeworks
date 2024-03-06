!pip install scrapy
!scrapy startproject sabahne
%cd sabahnews/sabahnews/spiders
!scrapy genspider alsabahnews https://www.assabahnews.tn/ar/
%%writefile alsabahnews.py
import scrapy
class alsabaahnews(scrapy.Spider):
  name = "sabahnews"
  start_urls=["https://www.assabahnews.tn/ar/"]
  def parse(self,response):
    world_news=response.css('div.ltabs-item')
    for news in world_news :
      yield{'Title':news.css('div.item-title a::text').get(),
            'date':news.css('div.Toplist div.created-date::text').get(),
            'description':news.css('div.introtext::text').get()}
!scrapy crawl sabahnews -o data.json
Out put 
/*
2024-02-18 10:46:58 [scrapy.utils.log] INFO: Scrapy 2.11.1 started (bot: sabahnews)
2024-02-18 10:46:58 [scrapy.utils.log] INFO: Versions: lxml 4.9.4.0, libxml2 2.10.3, cssselect 1.2.0, parsel 1.8.1, w3lib 2.1.2, Twisted 23.10.0, Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0], pyOpenSSL 24.0.0 (OpenSSL 3.2.1 30 Jan 2024), cryptography 42.0.2, Platform Linux-6.1.58+-x86_64-with-glibc2.35
2024-02-18 10:46:58 [scrapy.addons] INFO: Enabled addons:
[]
2024-02-18 10:46:58 [asyncio] DEBUG: Using selector: EpollSelector
2024-02-18 10:46:58 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2024-02-18 10:46:58 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.unix_events._UnixSelectorEventLoop
2024-02-18 10:46:58 [scrapy.extensions.telnet] INFO: Telnet Password: 20851fcfc6e9a43f
2024-02-18 10:46:58 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2024-02-18 10:46:58 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'sabahnews',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'sabahnews.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['sabahnews.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2024-02-18 10:46:58 [scrapy.middleware] INFO: Enabled downloader middlewares:
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
2024-02-18 10:46:58 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2024-02-18 10:46:58 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2024-02-18 10:46:58 [scrapy.core.engine] INFO: Spider opened
2024-02-18 10:46:58 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2024-02-18 10:46:58 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2024-02-18 10:46:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.assabahnews.tn/robots.txt> (referer: None)
2024-02-18 10:47:01 [urllib3.connectionpool] DEBUG: Starting new HTTPS connection (1): publicsuffix.org:443
2024-02-18 10:47:01 [urllib3.connectionpool] DEBUG: https://publicsuffix.org:443 "GET /list/public_suffix_list.dat HTTP/1.1" 200 84471
2024-02-18 10:47:01 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.assabahnews.tn/ar/> (referer: None)
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tمفوض عام الأونروا: إسرائيل تهدف إلى تدمير المنظمة\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأحد، 18 فيفري 2024 11:41\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tاعتبر المفوض العام لوكالة الأمم المتحدة لغوث وتشغيل اللاجئين ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tالثلاثاء.. مجلس الأمن يُصوّت على مشروع جزائري بشأن غزة\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأحد، 18 فيفري 2024 11:21\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0 \r\n قرر مجلس الأمن الدولي التصويت على مشروع القرار الجزائري ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tاتفاق التهدئة في قطاع غزة.. بين شروط إسرائيل ومطالب حماس\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأحد، 18 فيفري 2024 10:24\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0 \r\n \xa0 \r\n \xa0 \r\n لا يزال اتفاق التهدئة في قطاع غزة، ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tلجنة الصحة تعقد جلسة استماع حول مقترح القانون الأساسي المتعلق بحقوق المرضى والمسؤولية الطبية\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالسبت، 17 فيفري 2024 08:19\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0عقدت لجنة الصحة وشؤون المرأة والأسرة والشؤون الاجتماعية وذوي الإعاقة ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tالبرلمان.. لجنة الحقوق والحريات تواصل النظر في أحكام مشروع قانون بطاقة التعريف الوطنية\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالجمعة، 16 فيفري 2024 21:55\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0عقدت لجنة الحقوق والحريات اليوم الجمعة 16 فيفري 2024 جلسة بحضور ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tقبل  التصويت على قانون تجريم التطبيع..اجتماع حاسم لحركة الشعب \t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالجمعة، 16 فيفري 2024 11:02\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0تعقد حركة الشعب الاحد القادم 25فيفري اشغال مجلسها الوطني في دورته ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tتفاصيل قواعد وإجراءات تنظيم انتخابات مجالس الأقاليم والمجلس الوطني للجهات والأقاليم\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالخميس، 15 فيفري 2024 15:24\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tنشرت الهيئة العليا المستقلة للانتخابات القرار عدد 282 لسنة 2024 المؤرخ في ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tلجنة الصناعة والتجارة والثروات الطبيعية والطاقة والبيئة تصادق على تقريريها حول مشروعي قانونين \t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالخميس، 15 فيفري 2024 12:31\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0\r\nعقدت لجنة الصناعة والتجارة والثروات الطبيعية والطاقة والبيئة جلسة ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tالبرلمان يشرع في مناقشة مشروع قانون لإتمام القانون عدد 17 لسنة 2005 للمعادن النفيسة\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأربعاء، 14 فيفري 2024 11:42\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0 شرع مجلس نواب الشعب، خلال جلسة عامة،\xa0الأربعاء، في مناقشة مشروع ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tبورصة تونس تقفل حصة الجمعة على شبه استقرار\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالجمعة، 16 فيفري 2024 17:02\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tأقفل المؤشر المرجعي لبورصة تونس "توننداكس" حصّة، الجمعة، على شبه ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tصدرت بالرائد الرسمي.. معدلات نسب الفائدة الفعلية ونسب الفائدة المشطة التي ...\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالخميس، 15 فيفري 2024 23:22\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0 \r\n صدر بالعدد الأخير من الرائد الرسمي للجمهورية قرار عن وزيرة ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\t تونس حصلت على تمويلات بقيمة 92 مليون أورو من البنك الاوروبي للاستثمار في 2023\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالخميس، 15 فيفري 2024 20:57\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0أعلن البنك الأوروبي للإستثمار من خلال البنك الأوروبي عالم فرعه ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tتراجع عجز الميزان التجاري الطاقي بـ7 بالمائة في 2023\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأربعاء، 14 فيفري 2024 17:36\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0تراجع عجز الميزان التجاري الطاقي بنسبة 7 بالمائة خلال 2023 (مع ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tمفوض عام الأونروا: إسرائيل تهدف إلى تدمير المنظمة\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأحد، 18 فيفري 2024 11:41\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tاعتبر المفوض العام لوكالة الأمم المتحدة لغوث وتشغيل اللاجئين ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tالثلاثاء.. مجلس الأمن يُصوّت على مشروع جزائري بشأن غزة\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأحد، 18 فيفري 2024 11:21\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0 \r\n قرر مجلس الأمن الدولي التصويت على مشروع القرار الجزائري ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tاتفاق التهدئة في قطاع غزة.. بين شروط إسرائيل ومطالب حماس\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأحد، 18 فيفري 2024 10:24\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0 \r\n \xa0 \r\n \xa0 \r\n لا يزال اتفاق التهدئة في قطاع غزة، ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tالطائرات الحربية الإسرائيلية تُنفّذ غارات على جنوب لبنان\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأحد، 18 فيفري 2024 10:20\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0 \r\n \xa0 \r\n تواصل إسرائيلي غاراتها وقصفها على القرى والبلدات ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\t🔴 ماذا وراء قرار الا.حتلا.ل شن هجوم على رفح؟ ما هي رهانات نتنياهو من وراء اصراره على هذا الهجوم؟\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالسبت، 17 فيفري 2024 21:49\t\t\t\t\t', 'description': None}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\t🔴"شنوة الحل؟" يطرح في حلقة جديدة موضوع ارتفاع أسعار الحج والعمرة.. الأسباب والحلول\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالسبت، 17 فيفري 2024 18:49\t\t\t\t\t', 'description': None}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\t🔴حلقة جديدة من برنامج "العين الثالثة "\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالخميس، 15 فيفري 2024 19:52\t\t\t\t\t', 'description': None}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\t🔴"الصباح ديجيتال" تستعرض بعض قصص الحب في حصة خاصة بـ "عيد الحب"\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالخميس، 15 فيفري 2024 08:20\t\t\t\t\t', 'description': None}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\t🔴في "الكلمة ليك".. آراء عدد من المواطنين بمناسبة الاحتفال بعيد الحب\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأربعاء، 14 فيفري 2024 15:29\t\t\t\t\t', 'description': None}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\t🔴بورتريه.. تكريم خاص لوجوه غابت عن الشاشة ولم تغب من الذاكرة\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأربعاء، 14 فيفري 2024 12:51\t\t\t\t\t', 'description': None}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tفيديو/رؤوف بن يغلان ل "الصباح نيوز":لا بد أن يواكب الفنان ...\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالسبت، 17 فيفري 2024 20:49\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tالتقت الصباح نيوز بعد ظهر اليوم على هامش حفل توقيع رواية الكميونة ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tمجلة "أصوات ثقافية" مولود ثقافي إعلامي جديد صادر عن دار ...\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالسبت، 17 فيفري 2024 20:44\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0تعزز المشهد الإعلامي الثقافي بمولود جديد صادر عن دار خريف للنشر ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tالثلاثاء القادم  اخر اجل لتقديم الترشحات..مهرجان الاغنية ...\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالسبت، 17 فيفري 2024 20:41\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0\r\n**مكافات مالية لكل المشاركين في دورة تحتفي بفلسطين\r\n**الغاء ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tوزارة الثقافة تعلن فتح باب الترشح لهذه الخطط\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالجمعة، 30 ديسمبر 2022 14:59\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tأعلنت وزارة الشؤون الثقافيّة، عن فتح باب الترشح للخطط التالية: \r\n ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\t فتح مناظرة لانتداب رقباء أمن بسلك الأمن الوطني والشرطة.. التفاصيل \t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالثلاثاء، 29 نوفمبر 2022 21:39\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tاعلنت وزارة الداخلية عن فتح مناظرة لانتداب رقباء أمن بسلك الأمن ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tانتدابات بالصندوق الوطني للضمان الاجتماعي.. وهذه التفاصيل\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالجمعة، 04 نوفمبر 2022 12:52\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tأعلن الصندوق الوطني للضمان الاجتماعي في بلاغ صدر اليوم الجمعة، عن ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tفتح باب الترشّحات لسدّ الشغور ببعض مراكز الشباب والطفولة.. وهذه التفاصيل\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالجمعة، 28 أكتوير 2022 14:10\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tأعلنت\xa0وزارة الأسرة والمرأة والطفولة وكبار السنّ أنها تعتزم فتح ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tهيئة الانتخابات تنتدب وهذه التفاصيل\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأربعاء، 28 سبتمبر 2022 12:40\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0 \r\n أعلنت الهيئة العليا المستقلة للإنتخابات عن فتح باب الترشّح ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tوزارة الداخلية: مناظرة خارجية للقبول بمرحلة تكوين أساسي لإنتداب حفاظ أمن بالأمن ...\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالجمعة، 22 جويلية 2022 09:29\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tأفادت وزارة الداخلية أنه تقرّر فتح مناظرة خارجية بالاختبارات للقبول ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tفتح مناظرة لانتداب ملازمين أول بسلك الحرس الوطني لسنة 2021 -2022\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأربعاء، 29 جوان 2022 11:45\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t\xa0تعتزم وزارة الداخلية فتح مناظرة لانتداب ملازمين أول بسلك الحرس ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tمناظرة لانتداب عرفاء بسلك الحرس الوطني\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالخميس، 20 ماي 2021 09:28\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tتعتزم وزارة الداخلية فتح مناظرة لانتداب عرفاء بسلك الحرس الوطني لسنة ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tبلاغ بخصوص ” مناظرات الشركة الوطنية للسكك الحديدية التونسية “\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالسبت، 27 مارس 2021 17:59\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tتعلم الشركة الوطنيّة للسّكك الحديديّة التونسيّة أنّه على إثر الإعلان ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tسامسونغ توفر في السوق التونسية المنتج الجديد Galaxy A15\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالجمعة، 16 فيفري 2024 10:56\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tاثر لقاء مع رئيس الدولة..بنك تونس العربي الدولي يتعهد بانجاز مشاريع وطنية ودعم ...\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالأربعاء، 14 فيفري 2024 08:24\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tإثر لقاء جمع رئيس الجمهورية قيس سعيد بمحمد العقربي، عضو مجلس الإدارة ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tهل ستعود تدفقات رؤوس الأموال بقوة إلى الأسواق الناشئة؟ \t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالثلاثاء، 13 فيفري 2024 09:55\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tعلى مدى العامين الماضيين، عانت الأسواق الناشئة من تقلبات كبيرة في ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.assabahnews.tn/ar/>
{'Title': '\r\n\t\t\t\t\t\t\tسامسونج تحصل على ترخيص إدارة الغذاء والدواء الأمريكيّة لميّزة انقطاع التنفّس ...\t\t\t\t\t\t', 'date': '\r\n\t\t\t\t\t\tالإثنين، 12 فيفري 2024 13:03\t\t\t\t\t', 'description': '\r\n\t\t\t\t\t\tحصلت الميّزة المبتكرة من سامسونج لاكتشاف “انقطاع التنفس أثناء ...\t\t\t\t\t'}
2024-02-18 10:47:02 [scrapy.core.engine] INFO: Closing spider (finished)
2024-02-18 10:47:02 [scrapy.extensions.feedexport] INFO: Stored json feed (39 items) in: data.json
2024-02-18 10:47:02 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 451,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 39103,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 2,
 'elapsed_time_seconds': 3.356718,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2024, 2, 18, 10, 47, 2, 204743, tzinfo=datetime.timezone.utc),
 'httpcompression/response_bytes': 218370,
 'httpcompression/response_count': 1,
 'item_scraped_count': 39,
 'log_count/DEBUG': 46,
 'log_count/INFO': 11,
 'memusage/max': 98799616,
 'memusage/startup': 98799616,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/200': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2024, 2, 18, 10, 46, 58, 848025, tzinfo=datetime.timezone.utc)}
2024-02-18 10:47:02 [scrapy.core.engine] INFO: Spider closed (finished)
*/
