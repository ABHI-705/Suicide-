import numpy as np
import pandas as pd
import streamlit as st
import pandas_profiling
import matplotlib.pyplot as plt
import pywedge as pw
from IPython.display import display as ds
from streamlit_pandas_profiling import st_profile_report
#st.title('SUICIDE IN INDIA DURING 2001 TO 2012')
#data=pd.read_csv("C:/Users/User37/Downloads/Suicides_in_India.csv")
#data

#df=pw.Pywedge_Charts(data, c=None, y='Year')
#df
import pandas as pd
df = pd.read_csv("C:/Users/User37/Downloads/Suicides_in_India.csv")
df.describe(include='all')
from pandas_profiling import ProfileReport
profile = ProfileReport(df)
profile
import pandas as pd

import pandas_profiling

import streamlit as st

from streamlit_pandas_profiling import st_profile_report

from pandas_profiling import ProfileReport

df = pd.read_csv("C:/Users/User37/Downloads/Suicides_in_India.csv", na_values=['='])

profile = ProfileReport(df,title="sucide Data")

st.title("Pandas Profiling in Streamlit!")

st.write(df)

st_profile_report(profile)





