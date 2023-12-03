import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd

list_director = ['', 'Christopher Nolan', 'Frank Darabont', 'Quentin Tarantino', 'Francis Ford Coppola' ]
list_genre = ['', 'Sci-Fi', 'Drama', 'Action', 'Crime']

# Connection to the PostgreSQL database for cinema schedules
conn = st.connection("postgresql", type="sql", 
                     url="postgresql://intanoliviaitaliyana:BHs3h0cygXUa@ep-morning-waterfall-53636265.us-east-2.aws.neon.tech/web")

# Cinema Schedule Table
with conn.session as session_cinema:
    query = text('CREATE TABLE IF NOT EXISTS SCHEDULE (id SERIAL, movie_title TEXT, genre TEXT, director TEXT, release_date DATE, start_time TIME, end_time TIME, theater_number INT, ticket_price DECIMAL);')
   
    session_cinema.execute(query)

# Streamlit app for cinema schedule
st.header('SIMPLE CINEMA SCHEDULE MANAGEMENT SYS')
page_cinema = st.sidebar.selectbox("Choose Menu", ["View Cinema Schedule", "Edit Cinema Schedule"])

if page_cinema == "View Cinema Schedule":
    # Display cinema schedule data
        data_cinema = conn.query('SELECT * FROM movie_schedule ORDER BY id;')
        st.dataframe(data_cinema)

if page_cinema == "Edit Cinema Schedule":
    # Add Movie Schedule Button
    if st.button('Add Movie Schedule'):
        with conn_cinema.session as session_cinema:
            query_add_cinema = text('''
                INSERT INTO movie_schedule (
                    movie_title, genre, director, release_date, start_time, end_time, theater_number, ticket_price
                ) VALUES (:1, :2, :3, :4, :5, :6, :7, :8);
            ''')
            session_cinema.execute(query_add_cinema, {'1': '', '2': '', '3': '', '4': None, '5': None, '6': None, '7': None, '8': None})
            session_cinema.commit()

    # Display existing cinema schedule data with options to edit or delete
    data = conn.query('SELECT * FROM schedule ORDER By id;', ttl="0")
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
                director_baru = st.text_input("Director", director_lama)
                release_date_baru = st.date_input("Release Date", release_date_lama)
                start_time_baru = st.time_input("Start Time", start_time_lama)
                end_time_baru = st.time_input("End Time", end_time_lama)
                theater_number_baru = st.number_input("Theater Number", theater_number_lama)
                ticket_price_baru = st.number_input("Ticket Price", ticket_price_lama)


                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn_cinema.session as session_cinema:
                            query = text('UPDATE schedule \
                                          SET doctor_name=:1, patient_name=:2, gender=:3, symptom=:4, \
                                          handphone=:5, address=:6, waktu=:7, tanggal=:8 \
                                          WHERE id=:9;')
                            session.execute(query_update_cinema, {'1': movie_title_baru, '2': genre_baru, '3': director_baru,
                                                                         '4': release_date_baru, '5': start_time_baru, '6': end_time_baru,
                                                                         '7': theater_number_baru, '8': ticket_price_baru, '9': id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM schedule WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
