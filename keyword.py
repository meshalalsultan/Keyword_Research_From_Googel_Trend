import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

#Keyword Interest By Region

trends.build_payload(kw_list=["Data Science"])
data = trends.interest_by_region()
print(data.sample(20))

#Values ​​are calculated on a scale of 0 to 100, where 100 is the most popular location as a fraction of the total searches for that location, a value of 50 indicates a location half as popular.
#Now let’s visualize the above search results to get better insights:

df = data.sample(15)
df.reset_index().plot(x="geoName", y="Data Science", figsize=(20,8), kind="bar")
plt.show()
df.to_csv('sampel_data|_since_quiry.csv')

'''
Keyword Research with Python for Daily Search Trends
Now let’s take a look at the top daily search trends around the world.
To do this, we need to use the trending_searches () method:
'''

data = trends.trending_searches(pn="united_states")
print(data.head(10))
data.to_csv('trends.csv')

# Get Google Hot Trends data
today_searches_df = trends.today_searches(pn='US')
print(today_searches_df.head(20))
today_searches_df.to_csv('today_searches_df.csv')

#Get Google Keyword Suggestion
#Let’s get a suggestion for the keyword “diet” and “vegan“

# Get Google Keyword Suggestions
suggestions_dict = trends.suggestions(keyword='diet')
print(pd.DataFrame(suggestions_dict).drop('mid', axis=1))

suggestions_dict = trends.suggestions(keyword='vegan')
print(pd.DataFrame(suggestions_dict).drop('mid', axis=1))
suggestions_dict.to_csv('suggestions_dict.csv')

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() &amp; related_queries()
trends.build_payload(kw_list=['coronavirus'])
 
# Interest Over Time
interest_over_time_df = trends.interest_over_time()
print(interest_over_time_df.tail(10))
interest_over_time_df.to_csv('interest_over_time_df.csv')

# Interest by Region
interest_by_region_df = trends.interest_by_region()
print(interest_by_region_df.sort_values(['coronavirus'], ascending=False).head(20))

#Get the Related Queries
#Let’s get the related queries of the keyword “coronavirus“

# Related Queries, returns a dictionary of dataframes
related_queries_dict = trends.related_queries()
print(related_queries_dict['coronavirus']['top'].head(20))
print(related_queries_dict['coronavirus']['rising'].head(20))

#Google Keyword Suggestion
#Now, let’s see how we can get the google keywords suggestion for keyword research with python.
#Keywords are those words that are mostly typed by users in the search engine to find about a particular topic:

keyword = trends.suggestions(keyword="Data Analisis")
data = pd.DataFrame(keyword)
data.to_csv('keyword.csv')
print(data.head())