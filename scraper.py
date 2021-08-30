import bs4
import urllib.request as urllib_request
import pandas as pd

df = pd.read_html('data.html')
print(df.columns)