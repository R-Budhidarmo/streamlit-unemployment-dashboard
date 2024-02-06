# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings ----------------------------------------------------------
st.set_page_config(page_title="Unemployment Dashboard",
                   initial_sidebar_state="expanded")

if "input" not in st.session_state:
    st.session_state["input"] = "not done"

def change_state():
    st.session_state["input"] = "done"

st.title(":female-farmer: Unemployment Rate Data :male-factory-worker:")
st.markdown("A dashboard to visualise World Bank unemployment data")

# Load data     ----------------------------------------------------------
df = pd.read_csv("data/unemployment_reshaped.csv")
idx = list(df['Year'].unique())
df1 = pd.read_csv("data/country_code.csv")
df1 = df1.iloc[40:,].reset_index()
df1.drop("index",axis=1,inplace=True)

# Sidebar       ----------------------------------------------------------
with st.sidebar:
    st.header("Input Panel")

    slctd_year = st.selectbox('Select a year to update the map',idx)
    slctd_year_df = df[(df['Year'] == slctd_year)]

    slctd_countries = st.multiselect("Select up to 6 countries to generate a line chart",
                        df1['Country Code'].iloc[40:],max_selections=6)

    if st.checkbox(label="Click for a table of country codes & country names",value=False):
        st.write(df1)

    slctd_data = df.copy()
    slctd_data = slctd_data[slctd_data['Country Code'].isin(slctd_countries)]

    start_year, end_year = st.select_slider("Select a year range to analyse",
                    options=idx,
                    value=(min(idx),max(idx)))
    
# Plots         ---------------------------------------------------------- 
# choropleth
def map_plot(data):
    choropleth = px.choropleth(data,locations='Country Code',
                           color='Unemployment Rate (%)',
                           hover_name='Country Name',
                           color_continuous_scale=px.colors.sequential.YlOrRd,
                           title="")
    return st.plotly_chart(choropleth)

# line chart
def data_plot(data,start_y,end_y):
    fig = px.line(data,x='Year',y='Unemployment Rate (%)',
                  color='Country Code')
    fig.add_vline(start_y,line_dash="dash",line_color="lightgrey")
    fig.add_vline(end_y,line_dash="dash",line_color="lightgrey")
    fig.update_layout(legend=dict(orientation="h",
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="left",
                                  x=0))
    return st.plotly_chart(fig,use_container_width=True)

# Main Panel    ---------------------------------------------------------- 
if st.sidebar.button('Generate Line Chart',on_click=change_state()):
    if st.session_state["input"] == "done":

        col1, col2 = st.columns([1,0.2])
        with col1:
            st.subheader("Unemployment Rate for Selected Countries")
            data_plot(slctd_data,start_year,end_year)

            slctd_df = df1[df1["Country Code"].isin(slctd_data['Country Code'].unique())].reset_index()
            st.table(slctd_df[['Country Code','Country Name']])

        with col2:
            st.caption(f"Data as of {end_year} & Change Since {start_year}")
            for i in slctd_countries:
                start_entry = df['Unemployment Rate (%)'].loc[(df['Year']==start_year) & (df['Country Code']==i)]
                end_entry = df['Unemployment Rate (%)'].loc[(df['Year']==end_year) & (df['Country Code']==i)]
                st.metric(label=f"{i}",
                            value=f'{round(float(end_entry.iloc[0]),3)} %',
                            delta=f'{round(float(end_entry.iloc[0]) - float(start_entry.iloc[0]),3)} %')

map_plot(slctd_year_df)

with st.expander('About', expanded=False):
    st.write('''
        - Data originated from [World Bank](https://www.worldbank.org/en/home) &
                were retrieved from [Kaggle](https://www.kaggle.com/datasets/theworldbank/health-nutrition-and-population-statistics)
        - It does not contain the most recent data.
        - Dashboard was made by Rhesa Budhidarmo (February 2024)
        ''')
    st.markdown('''![Title](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)
                www.linkedin.com/in/rhesa-budhidarmo''')