import numpy as np
import pandas as pd
from PIL import Image
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

from pathlib import Path

class PartA:
    def __init__(self):
        self.selected = option_menu(
            menu_title=None,
            options = ['Data Info', 'A) Preparation', 'B) Analysis'],
            icons = ['caret-down', 'caret-down', 'caret-down'],
            menu_icon=None,
            orientation='horizontal',
            default_index=0,
        )
        self.cwd = Path().parent.absolute()
        self.data_fld = self.cwd / 'Data' / 'Part-A'
        self.data_dict = self.load_analysis_data()

    @staticmethod
    @st.cache
    def airline_options(flights, airlines):
        x = flights['airline_id'].sort_values()
        y = x.map(airlines[['id', 'name']].set_index('id').squeeze())
        airline_options = list(x.str.cat(y, ' | ').unique())
        return airline_options

    @st.cache
    def min_max_years(self):
        years = self.data_dict['dates']['year'].sort_values().unique()
        _min = int(years.min())
        _max = int(years.max())
        return _min, _max

    @st.cache
    def load_analysis_data(self):
        data_dict = {
            'flights': pd.read_csv(self.data_fld / 'flights.zip', keep_default_na=False, na_values='', encoding='utf-8'),
            'airlines': pd.read_csv(self.data_fld / 'airlines.zip', keep_default_na=False, na_values='', encoding='utf-8'),
            'airports': pd.read_csv(self.data_fld / 'airports.zip', keep_default_na=False, na_values='', encoding='utf-8'),
            'countries': pd.read_csv(self.data_fld / 'countries.zip', keep_default_na=False, na_values='', encoding='utf-8'),
            'dates': pd.read_csv(self.data_fld / 'dates.zip', keep_default_na=False, na_values='', encoding='utf-8'),
            'days': pd.read_csv(self.data_fld / 'days.zip', keep_default_na=False, na_values='', encoding='utf-8'),
            'months': pd.read_csv(self.data_fld / 'months.zip', keep_default_na=False, na_values='', encoding='utf-8'),
            'seasons': pd.read_csv(self.data_fld / 'seasons.zip', keep_default_na=False, na_values='', encoding='utf-8'),
        }
        return data_dict
    
    def display_info_page(self):
        st.markdown(f"### Data preparation and analysis on U.S. International Air Traffic data(1990-2020):")
        col1, col2, = st.columns(2)
        with col1:
            st.markdown(f"#### Data sources:")
            st.markdown(f"""
                - [01. U.S. International Air Traffic data(1990-2020)](https://www.kaggle.com/datasets/parulpandey/us-international-air-traffic-data?resource=download)
                - [02. Airport Codes](https://datahub.io/core/airport-codes#resource-airport-codes_zip)
                - [03. IATA Codes](https://github.com/cmpolis/lets-explore-dataset-1/blob/master/data/iata-codes.csv)
                - [04. Carrier Codes](https://github.com/cmpolis/lets-explore-dataset-1/blob/master/data/carrier-codes.csv)
                - [05. More Files](http://www.lsv.fr/~sirangel/teaching/dataset/index.html) (Aircrafts, Airlines, Airports, Distance, Schedule)
            """)
        with col2:
            st.markdown(f"#### Usefull links:")
            st.markdown(f"""
                - **Airlines**
                  - [Airline codes (IATA, ICAO)](https://en.wikipedia.org/wiki/Airline_codes)
                  - [Airline codes (IATA, ICAO) - List](https://en.wikipedia.org/wiki/List_of_airline_codes)
                  - [Airline vs Carrier](https://diffsense.com/diff/air%20carrier/airline)
                - **Airports**
                  - [Airport code IATA](https://en.wikipedia.org/wiki/IATA_airport_code)
                  - [Airport code ICAO](https://en.wikipedia.org/wiki/ICAO_airport_code)
                  - [Airport codes (IATA, ICAO) - List](https://en.wikipedia.org/wiki/Lists_of_airports_by_IATA_and_ICAO_code)
                  - [Data Column Description](https://ourairports.com/help/data-dictionary.html) | [Other usefull info](https://ourairports.com/help/#legend)
                - **IATA/ICAO codes**
                  - [IATA codes search](https://www.iata.org/en/publications/directories/code-search/)
                  - *IATA codes*
                    - airline: **2**-letter ([Wiki 1](https://en.wikipedia.org/wiki/Airline_codes), [Wiki 2](https://en.wikipedia.org/wiki/List_of_airline_codes))
                    - airport location: **3**-letter ([Wiki 1](https://en.wikipedia.org/wiki/IATA_airport_code), [Wiki 2](https://en.wikipedia.org/wiki/Lists_of_airports_by_IATA_and_ICAO_code))
                  - *ICAO codes*
                    - airline: **3**-letter ([Wiki 1](https://en.wikipedia.org/wiki/Airline_codes#ICAO_airline_designator), [Wiki 2](https://en.wikipedia.org/wiki/List_of_airline_codes))
                    - airport location: **4**-letter ([Wiki 1](https://en.wikipedia.org/wiki/ICAO_airport_code), [Wiki 2](https://en.wikipedia.org/wiki/Lists_of_airports_by_IATA_and_ICAO_code))
                - **Countries**
                  - [Country ISO codes](https://www.iban.com/country-codes)
                
            """)

    def display_preparation_page(self):
        st.markdown(f"## Final Tables diagram")
        st.markdown(f"[Draw SQL free online tool](https://drawsql.app/teams/akotronis-team/diagrams/project-1)")
        part_a_img = Image.open(self.cwd / 'resources' / 'PartA-diagram.jpg')
        st.image(part_a_img, caption='Tables diagram')

        st.markdown(f"## Steps")

        st.markdown(f"### Fact table (flights)")
        st.markdown(f"We use **passengers** and **departures** datasets from [here](https://www.kaggle.com/datasets/parulpandey/us-international-air-traffic-data?resource=download)")
        st.markdown(f"**date**, **airports** (usa-foreign) and **carrier** columns uniquely identify entries of each dataframe. We join the dataframes on these keys")

        st.markdown(f"### Dimension 1 (dates)")
        st.markdown(f"We use the **data_dte** column of the fact table to make the dimension table for dates")
        st.markdown(f"From the date we create new columns for the dimension table which we will use for our analysis")
        st.markdown(f"We create new tables **seasons**, **days**, **months** and use integer foreign keys in the dates table")

        st.markdown(f"### Dimension 2 (airlines)")
        st.markdown(f"We use **carrier-codes.csv** from [here](https://github.com/cmpolis/lets-explore-dataset-1/blob/master/data/carrier-codes.csv) and **Airlines.csv** from [here](http://www.lsv.fr/~sirangel/teaching/dataset/airlines.txt)")
        st.markdown(f"The above IATA/ICAO code entries cover 93.0% of our fact table entries (**carrier** column) so we also use [wiki page](https://en.wikipedia.org/wiki/List_of_airline_codes) to reach 95.7%")
        st.markdown(f"We use **countries** information from [here](https://www.iban.com/country-codes) for the country key")

        st.markdown(f"### Dimension 3 (airports)")
        st.markdown(f"We ue data from [here](https://datahub.io/core/airport-codes#resource-airport-codes_zip) and also from [here](http://www.lsv.fr/~sirangel/teaching/dataset/airports.txt)")
        st.markdown(f"We use **countries** information from [here](https://www.iban.com/country-codes) for the country key")

        st.markdown(f"""
            We make sure:
            - **airports** table has no null **coutry_id** and **name** entries
            - **airlines** table has no null **coutry_id** and **name** entries
            - **flights** table has no null entries
            - **flights** table has all entries with **airport** and **airline** ids in the corresponding dimension tables
        """)      

        st.markdown(f"### All steps in code")
        html_fld = self.data_fld.parent.parent / 'resources'
        with open(html_fld / 'DIT161-Project-PartA.html', encoding='utf-8') as f:
            content = f.read()
        components.html(content, height=800, scrolling=True)

    def display_analysis_sc1(self):
        airports = self.data_dict['airports']
        dates = self.data_dict['dates']
        flights = self.data_dict['flights'].copy()

        flights['year'] = flights['date_id'].map(dates[['id', 'year']].set_index('id').squeeze())
        ################################################################
        ######################## 1 TOP AIRPORTS ########################
        ################################################################
        st.title('Scenario 1', anchor='PABSc1')
        st.markdown("##### A US company wants to open a new duty free store and looks for the busiest airports in US")
        st.markdown(" We use the **passengers** information")
        st.markdown("""
            - Filter for year range
            - Group by US airports
            - Sum passengers
            - Sort descending
            - Keep top results
        """)

        _min, _max = self.min_max_years()
        year_values_1 = st.slider('Select a range of years:', _min, _max, (_min, _max), key='sld1')
        min_year_1, max_year_1 = year_values_1
        nlargest_airports = st.number_input("Enter number for top busiest US airports (1-20):", min_value=1, max_value=20, step=1, value=5, format="%i", key='lrg1')
        
        df = flights.copy()
        df = df.loc[df['year'].isin(range(min_year_1, max_year_1 + 1))]
        keep_columns = [
            'year',
            'airport_usa_id',
            'psg_total_flights',
        ]
        df = df[keep_columns]
        df_grouped_year = df.groupby(['airport_usa_id', 'year']).sum()
        df_grouped_tot = df_grouped_year.groupby(['airport_usa_id']).sum()
        df_grouped_tot = df_grouped_tot.nlargest(nlargest_airports, 'psg_total_flights').reset_index()
        df_grouped_tot['airport_name'] = df_grouped_tot['airport_usa_id'].map(airports[['id', 'name']].set_index('id').squeeze())
        df_grouped_tot = df_grouped_tot.rename(columns={'psg_total_flights':'Passengers (N)', 'airport_usa_id':'Airports'})

        df_grouped_year = df_grouped_year[df_grouped_year.index.get_level_values(0).isin(df_grouped_tot['Airports'])].reset_index()
        df_grouped_year = df_grouped_year.rename(columns={'year':'Year', 'psg_total_flights':'Passengers (N)', 'airport_usa_id':'Airports'})
        airport_dict = pd.Series(df_grouped_tot['Airports'].index.values, index=df_grouped_tot['Airports'])
        df_grouped_year['sort'] = df_grouped_year['Airports'].map(airport_dict)
        df_grouped_year = df_grouped_year.sort_values(['sort', 'Year'])
        
        year_range = f"{min_year_1}-{max_year_1}" if min_year_1 != max_year_1 else f"{min_year_1}"
        airports_title_tot = f"{nlargest_airports} busiest US airports in {year_range}" if nlargest_airports > 1 else f"Busiest US airport in {min_year_1}-{max_year_1}"
        st.markdown(f"### {airports_title_tot}")
        airports_figure_tot = px.bar(
            df_grouped_tot,
            x='Airports',
            y='Passengers (N)',
            color='Passengers (N)',
            template='plotly_white',
            title='',
        )
        st.plotly_chart(airports_figure_tot)
        top_airports = df_grouped_tot[['Airports', 'airport_name']].apply(lambda r: f"{r['Airports']}: {r['airport_name']}", axis='columns')
        top_airports = top_airports.reset_index(drop=True)
        top_airports.index = top_airports.index + 1
        top_airports = top_airports.index.map(lambda x : f"| {str(x).zfill(2)}").str.cat(top_airports.values, sep=' | ')
        st.markdown("### Airport Ranking:")
        st.markdown('\n\n'.join(top_airports))

        if min_year_1 != max_year_1:
            airports_title_by_year = f"{nlargest_airports} busiest US airports in {year_range}" if nlargest_airports > 1 else f"Busiest US airport in {min_year_1}-{max_year_1} by year"
            st.markdown(f"### {airports_title_by_year}")

            airports_figure_by_year = px.line(
                df_grouped_year,
                x="Year",
                y="Passengers (N)",
                color='Airports',
                template="plotly_white",
                markers=True,
            )
            airports_figure_by_year.update_traces(
                line=dict(width=3.0),
                marker=dict(size=6.0),
            )
            st.plotly_chart(airports_figure_by_year)

    def display_analysis_sc2(self):
        airlines = self.data_dict['airlines']
        dates = self.data_dict['dates']
        months = self.data_dict['months']
        seasons = self.data_dict['seasons']
        flights = self.data_dict['flights'].copy()

        flights['month'] = flights['date_id'].map(dates[['id', 'month']].set_index('id').squeeze()).map(months[['id', 'month']].set_index('id').squeeze())
        flights['year'] = flights['date_id'].map(dates[['id', 'year']].set_index('id').squeeze())
        flights['season'] = flights['date_id'].map(dates[['id', 'season_id']].set_index('id').squeeze()).map(seasons[['id', 'season']].set_index('id').squeeze())
        ################################################################
        ####################### 2 FLIGHT TYPES #########################
        ################################################################
        st.title('Scenario 2', anchor='PABSc2')
        st.markdown("##### An airline wants to inspect the average number of flights per type and month/season level for ticket distribution planning")
        st.markdown("""
            - Filter for year range and airline
            - Group by period type and by year
            - Sum flight type
            - Group by period type
            - Mean aggregate flight type
            - (If no flight type is selected it is assumed total)
        """)

        _min, _max = self.min_max_years()
        year_values_2 = st.slider('Select a range of years', _min, _max, (_min, _max), key='sld2')
        min_year_2, max_year_2 = year_values_2

        selected_period_type = st.selectbox(
            'Select period type:',
            ('Month', 'Season'),
            key='slb1',
        )
        selected_period_type = selected_period_type.lower()

        selected_flight_type = st.multiselect(
            'Select flight type:',
            ('Charter', 'Scheduled'),
            default=('Charter', 'Scheduled'),
            key='ms1',
        )
        selected_flight_type = selected_flight_type[0].lower() if len(selected_flight_type) == 1 else 'total'
        
        airline_options = PartA.airline_options(flights, airlines)
        selected_airline = st.selectbox(
            'Select airline:',
            airline_options,
            key='slb2',
        )

        df = flights.copy()
        mask1 = df['year'].isin(range(min_year_2, max_year_2 + 1))
        mask2 = df['airline_id'] == selected_airline.split('|')[0].strip()
        df = df.loc[mask1 & mask2]
        keep_columns = [
            'year',
        ]
        keep_columns.extend([selected_period_type, f"dep_{selected_flight_type}_flights"])
        df = df[keep_columns]
        df_grouped = df.groupby([selected_period_type, 'year']).sum().groupby(selected_period_type).mean().round(0).applymap(int).reset_index()
        y_axis = f"{selected_flight_type.title()} (avg)"
        df_grouped = df_grouped.rename(columns={
            selected_period_type: selected_period_type.title(),
            f"dep_{selected_flight_type}_flights": y_axis,
        })
        df_grouped = df_grouped.sort_values(y_axis, ascending=False)
        
        selected_flight_type_title = '' if selected_flight_type == 'total' else f" {selected_flight_type}"
        flight_type_title = f"Average{selected_flight_type_title} flights per {selected_period_type} in {min_year_2}-{max_year_2} | {selected_airline}"
        st.markdown(f"### {flight_type_title}")
        airports_figure = px.bar(
            df_grouped,
            x=selected_period_type.title(),
            y=y_axis,
            color=y_axis,
            template='plotly_white',
            title='',
        )
        st.plotly_chart(airports_figure)

    def display_analysis_sc3(self):
        dates = self.data_dict['dates']
        flights = self.data_dict['flights'].copy()

        flights['year'] = flights['date_id'].map(dates[['id', 'year']].set_index('id').squeeze())
        ################################################################
        ##################### 3 US/FOREIGN AIRLINES ####################
        ################################################################
        st.title('Scenario 3', anchor='PABSc3')
        st.markdown("##### US government wants to know the representation of US domestic airlines in flights with one US airport endpoint")
        st.markdown("""
            - Filter for year range
            - Group by year and us/foreign
            - Sum aggregate
            - Percents within groups
        """)

        _min, _max = self.min_max_years()
        year_values_3 = st.slider('Select a range of years', _min, _max, (_min, _max), key='sld3')
        min_year_3, max_year_3 = year_values_3

        df = flights.copy()
        keep_columns = [
            'year',
            'us_foreign_airline',
        ]
        df = df[keep_columns]
        df = df.loc[df['year'].isin(range(min_year_3, max_year_3 + 1))]

        # By year
        df['US/Foreign'] = df['us_foreign_airline'].map({0:'Foreign', 1:'US'})
        df_grouped = df.groupby(['year', 'US/Foreign']).count().reset_index()
        df_grouped = df_grouped.rename(columns={'us_foreign_airline':'count'})
        df_grouped['US/Foreign (%)'] = (100 * df_grouped['count'] / df_grouped.groupby('year')['count'].transform('sum')).round(0)

        us_airline_title_1 = f"US/Foreign airline representation per year in {min_year_3}-{max_year_3}"
        st.markdown(f"### {us_airline_title_1}")
        us_airline_figure_1 = px.bar(
            df_grouped,
            x="year",
            y="US/Foreign (%)",
            color="US/Foreign",
            title=''
        )
        st.plotly_chart(us_airline_figure_1)

        # Total
        df_grouped = df_grouped[['US/Foreign', 'count']].groupby(['US/Foreign']).sum().reset_index().sort_values('US/Foreign', ascending=False)
        us_airline_title_2 = f"US/Foreign airline representation in {min_year_3}-{max_year_3}"
        st.markdown(f"### {us_airline_title_2}")
        us_airline_figure_2 = px.pie(
            df_grouped,
            title='',
            values='count',
            names='US/Foreign',
        )
        st.plotly_chart(us_airline_figure_2)

    def display_analysis_sc4(self):
        airlines = self.data_dict['airlines']
        countries = self.data_dict['countries']
        flights = self.data_dict['flights'].copy()

        ################################################################
        ####################### 4 AIRLINE TRAFFIC ######################
        ################################################################
        st.title('Scenario 4', anchor='PABSc4')
        st.markdown("##### Airlines traffic is investigated taking into account the number of passengers and the number of flights")
        st.markdown("""Flights and passengers are correlated but characterize traffic in a different way since passengers directly map to profit but flights may not if plains are not full""")
        st.markdown("""Correlation matrix:""")
        st.dataframe(flights[['psg_total_flights', 'dep_total_flights']].rename(columns={
            'psg_total_flights':'passengers',
            'dep_total_flights':'flights',
        }).corr())
        
        st.markdown("""We define traffic as linear combination of passengers and flights.""")
        st.markdown("""Weight $x$ is selected for the passengers factor (0-10) and flights will be assigned $1-x/10$""")
        st.markdown("""
            - Filter for airline selection (us/foreign)
            - Min-max normalize passengers, flights
            - Group by airline
            - Sum linear combination
            - Keep top results
            - (If no airlines are included it is assumed both)
        """)

        airline_selection = st.multiselect(
            'Include Airlines:',
            ('US', 'Foreign'),
            default=('US', 'Foreign'),
            key='ms2',
        )
        airline_selection = airline_selection if airline_selection else ('US', 'Foreign')
        airline_selection = [{'US':1, 'Foreign':0}[s] for s in airline_selection]

        pass_wgt = st.number_input("Enter number as a weight for flight passenger number (0-10):", min_value=0, max_value=10, step=1, value=5, format="%i")
        pass_wgt = pass_wgt / 10.
        dep_wgt = 1 - pass_wgt

        st.markdown(f"#### Weighted: ${pass_wgt:.1f}\cdot\mathrm{{passengers\;N}}\;+\;{dep_wgt:.1f}\cdot\mathrm{{flights\;N}}$")
        nlargest_airlines = st.number_input("Enter number for top busiest airlines (1-20):", min_value=1, max_value=20, step=1, value=5, format="%i", key='lrg2')
        
        df = flights.copy()
        df = df.loc[df['us_foreign_airline'].isin(airline_selection)]
        
        # min-max normalization
        col1 = pass_wgt * (df['psg_total_flights'] - df['psg_total_flights'].min()) / (df['psg_total_flights'].max() - df['psg_total_flights'].min())
        col2 = dep_wgt * (df['dep_total_flights'] - df['dep_total_flights'].min()) / (df['dep_total_flights'].max() - df['dep_total_flights'].min())
        df['weighted'] =  col1 + col2
        keep_columns = [
            'airline_id',
            'weighted',
        ]
        df = df[keep_columns]
        df_grouped = df.groupby('airline_id').sum().reset_index()
        df_grouped = df_grouped.sort_values('weighted', ascending=False).nlargest(nlargest_airlines, 'weighted')
        df_grouped['country'] = df_grouped['airline_id'].map(airlines[['id', 'country_id']].set_index('id').squeeze()).map(countries[['id', 'name']].set_index('id').squeeze())
        df_grouped['name'] = df_grouped['airline_id'].map(airlines[['id', 'name']].set_index('id').squeeze())

        top_airlines = df_grouped.apply(lambda r: f"{r['airline_id']}: {r['name']} | {r['country']}", axis='columns')
        top_airlines = top_airlines.reset_index(drop=True)
        top_airlines.index = top_airlines.index + 1
        top_airlines = top_airlines.index.map(lambda x : f"| {str(x).zfill(2)}").str.cat(top_airlines.values, sep=' | ')
        st.markdown("### Airlines Ranking:")
        st.markdown('\n\n'.join(top_airlines))

    def display_analysis_page(self):
        with st.sidebar:
            main_selected = option_menu(
                menu_title=None,
                options = [f"Scenario {i}"for i in range(1,5)],
                icons = 4 * ['arrow-bar-right'],
                menu_icon=None,
                orientation='vertical',
                default_index=0,
            )
        if main_selected == 'Scenario 1':
            self.display_analysis_sc1()
        elif main_selected == 'Scenario 2':
            self.display_analysis_sc2()
        elif main_selected == 'Scenario 3':
            self.display_analysis_sc3()
        elif main_selected == 'Scenario 4':
            self.display_analysis_sc4()
        
        
        

        

        

        