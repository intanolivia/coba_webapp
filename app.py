import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd

list_director = ['', 'Christopher Nolan', 'Frank Darabont', 'Quentin Tarantino', 'Francis Ford Coppola' ]
list_genre = ['', 'Sci-Fi', 'Drama', 'Action', 'Crime']

#gpt coba

# ...

# Cinema Schedule Table
with conn.session as session_cinema:
    query = text('CREATE TABLE IF NOT EXISTS movie_schedule (id SERIAL, movie_title TEXT, genre TEXT, director TEXT, release_date DATE, start_time TIME, end_time TIME, theater_number INT, ticket_price DECIMAL);')
   
    session_cinema.execute(query)

# ...

if page_cinema == "Edit Cinema Schedule":
    # ...

    for _, result in data.iterrows():
        id = result['id']
        movie_title_lama = result["movie_title"]
        genre_lama = result["genre"]
        director_name_lama = result["director"]
        release_date_lama = result["release_date"]
        start_time_lama = result["start_time"]
        end_time_lama = result["end_time"]
        theater_number_lama = result["theater_number"]
        ticket_price_lama = result["ticket_price"]

        with st.expander(f'{movie_title_lama}'):
            with st.form(f'movie-data-{id}'):
                movie_title_baru = st.text_input("Movie Title", movie_title_lama)
                genre_baru = st.text_input("Genre", genre_lama)
                director_baru = st.text_input("Director", director_name_lama)
                release_date_baru = st.date_input("Release Date", release_date_lama)
                start_time_baru = st.time_input("Start Time", start_time_lama)
                end_time_baru = st.time_input("End Time", end_time_lama)
                theater_number_baru = st.number_input("Theater Number", theater_number_lama)
                ticket_price_baru = st.number_input("Ticket Price", ticket_price_lama)

                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn_cinema.session as session_cinema:
                            query_update_cinema = text('UPDATE movie_schedule \
                                          SET movie_title=:1, genre=:2, director=:3, release_date=:4, \
                                          start_time=:5, end_time=:6, theater_number=:7, ticket_price=:8 \
                                          WHERE id=:9;')
                            session_cinema.execute(query_update_cinema, {'1': movie_title_baru, '2': genre_baru, '3': director_baru,
                                                                         '4': release_date_baru, '5': start_time_baru, '6': end_time_baru,
                                                                         '7': theater_number_baru, '8': ticket_price_baru, '9': id})
                            session_cinema.commit()
                            st.experimental_rerun()
                
                # ...
