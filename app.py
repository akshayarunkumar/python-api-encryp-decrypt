from unittest import result
import feedparser
import streamlit as st
from flask import Flask,jsonify



#st.title("LET'S GO...")
# my_range=range(1,21)
# temp= st.sidebar.select_slider("Select number of articles per source",options=my_range,value=5)
# search_choice = st.sidebar.selectbox('Search By Category:', options=['Top Stories',
#                                                             'Entertainment',
#                                                             'Technology',
#                                                             'Sports',
#                                                             'Business & Finance',
#                                                             'Health'], index=0)

app= Flask(__name__)
search_choice="ok"
temp=0

@app.route('/')
def hello_world():
    return 'Hello, World!'

def rss_feed_url(url):

        """given an RSS feed url, extract it's entities"""

        rss_feed_contents = feedparser.parse(url)
        news = rss_feed_contents.entries
        
    
        for idx, curr_news in enumerate(news):
            id = str(idx+1)
            #val = curr_news['pubDate']
            summ = curr_news.summary
           # st.write(f"{curr_news}")
            title = curr_news['title']
            article_published_at = curr_news.published
            actual_link = curr_news['link']
        #cat = curr_news['pubDate']
            content = curr_news['summary'].split('<')[0] if curr_news['summary'].split('<')[0] != '' else 'No article summary available, click on the link to read'
       # pdate = curr_news['pubDate']
            st.header(f"\n({id}) {title}")
            st.write(f"{article_published_at}")
            st.write(f"{content}")
            #st.write(f"{summ}")
            st.write(f"Read full story here: {actual_link}")
        #st.write(f"\n({id}) {title}\n02. News source: {actual_link}\n03. News Summary: {content}")
            st.write("---------------------------------------------------------")

            if idx>temp-2:
                break
# if search_choice == 'Top Stories':
@app.route('/cat/topstories')
def topstories():
    #-------------------------------------------------------------------------------------------------------------
    # search_choice_sub = st.sidebar.selectbox('Search By Category:', options=['India',
    #                                                         'World-wide'], index=0)

    # if search_choice_sub == 'India':
            dict_rss_news_feeds = { 'NDTV - India': "https://feeds.feedburner.com/ndtvnews-india-news"}
                 
            title=[]
            result={}
            content=""
            for channel, webpage in dict_rss_news_feeds.items():
            #   st.title(f"Your News from {channel}: \n")
            #   rss_feed_url(webpage)
              rss_feed_contents = feedparser.parse(webpage)
              news = rss_feed_contents.entries
              for idx, curr_news in enumerate(news):
                id = str(idx+1)
            #val = curr_news['pubDate']
                summ = curr_news.summary
           # st.write(f"{curr_news}")
                title.append(curr_news['title'])
                content = curr_news['summary']
                result={
                    "title":curr_news['title']
                }
            #   print("###########################################################################")
            return jsonify(result)
    # if search_choice_sub == 'World-wide':
    #         dict_rss_news_feeds = { 'Times of India': "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    #                                 'NY Times': "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
    #                                 'Science Daily':"https://www.sciencedaily.com/rss/all.xml"}
                 

    #         for channel, webpage in dict_rss_news_feeds.items():
    #           st.title(f"Your News from {channel}: \n")
    #           rss_feed_url(webpage)
    #           print("###########################################################################")

        

if search_choice == 'Entertainment':
   

    dict_rss_news_feeds = { 'TOI -Entertainment': "https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
                            'CNN - Entertainment': "http://rss.cnn.com/rss/edition_entertainment.rss",
                            'Hollywood - Life':"https://hollywoodlife.com/feed/",
                            'Zee News Entertainment':"https://zeenews.india.com/rss/entertainment-news.xml"}
                 


    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Sports':
   

    dict_rss_news_feeds = { 'Zee Sports': "https://zeenews.india.com/rss/sports-news.xml",
                            'Fox Sports':"https://api.foxsports.com/v1/rss?partnerKey=zBaFxRyGKCfxBagJG9b8pqLyndmvo7UU",
                            'Rot Wire':"https://www.rotowire.com/rss/articles.php"}
                 


    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Business & Finance':
   

    dict_rss_news_feeds = { 'Economic Times': "https://economictimes.indiatimes.com/wealth/rssfeeds/837555174.cms",
                            'India Times':"https://economictimes.indiatimes.com/news/economy/rssfeeds/1373380680.cms",
                            'Money Control':"https://www.moneycontrol.com/rss/economy.xml"}
                 


    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Technology':


    dict_rss_news_feeds = { 'NY -Technology': "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
                            'CNBC Tech':"https://www.cnbc.com/id/19854910/device/rss/rss.html",
                            'Wired Tech':"https://www.wired.com/feed/rss"}
    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if search_choice == 'Health':


    dict_rss_news_feeds = { 'Health News': "http://rssfeeds.webmd.com/rss/rss.aspx?RSSSource=RSS_PUBLIC",
                            'Medical Xpress':"https://medicalxpress.com/rss-feed/",
                            'Science Daily':"https://www.sciencedaily.com/rss/top/health.xml"}
    for channel, webpage in dict_rss_news_feeds.items():
        st.title(f"From {channel}: \n")
        rss_feed_url(webpage)
        print("###########################################################################")

if __name__=="__main__":
    app.run(debug=True)
