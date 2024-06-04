import streamlit as st
import time
from st_audiorec import st_audiorec

# funkcija za inicijalizaciju session_state za pohranu snimljenog zvuka i prenesenih datoteka
def init_session_state():
    if 'recorded_audio' not in st.session_state:
        st.session_state['recorded_audio'] = None
    if 'uploaded_files' not in st.session_state:
        st.session_state['uploaded_files'] = []

# funkcija za pohranu prenesene datoteke u session_state
def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        # citanje datoteke kao bajtova i pohrana u session_state
        file_bytes = uploaded_file.read()
        st.session_state['uploaded_files'].append((uploaded_file.name, file_bytes))
        st.write(f"Datoteka '{uploaded_file.name}' je prenesena i spremljena.")

def audiorec_ver1():
    # inicijalizacija session_state
    init_session_state()

    # naslov
    st.title('Klasifikacija glazbe')
    st.write('## _Projekt iz PSU_')
    st.write('Jednostavna aplikacija za detekciju žanra glazbe')
    st.divider()
    st.write('### Snimi glazbu preko mikrofona:')

    # snimanje zvuka preko mikrofona
    wav_audio_data = st_audiorec()

    # ak je zvuk snimljen stavlja ga u session_state
    if wav_audio_data is not None:
        st.session_state['recorded_audio'] = wav_audio_data

    # kad se klikne gumb pronalazi se zanr
    if st.button('Pronadi zanr'):
        if st.session_state['recorded_audio'] is not None:
            st.write('Sada ću odgonetnuti žanr snimljene glazbe')
            time.sleep(2)
            # ovdje zovem model i ispijem ga u st.write
            st.write('Tvoj žanr je: ovdje ce bit rezultat modela')
        else:
            st.write('Glazba bi bila poželjna, ne mogu reći žanr tvog šta god to bilo.')

    st.divider()

    
    #sucelje za file uploader
    with st.form("forma"):
        st.write('### Prenesi datoteku:')
        uploaded_file = st.file_uploader("Odaberi datoteku", type=['wav'], accept_multiple_files=False)
        submitted = st.form_submit_button("Žanriraj")
        if submitted and uploaded_file is not None:
            save_uploaded_file(uploaded_file)

    # gleda jel file uploadan u session
    if 'uploaded_files' in st.session_state and st.session_state['uploaded_files']:
        st.write('### Odaberi datoteku za klasifikaciju:')
        selected_files = st.multiselect('Odaberi datoteku:', [f[0] for f in st.session_state['uploaded_files']], max_selections=(1))

        if st.button('Pokreni klasifikaciju'):
            if selected_files:
                # kada se klikne gumb koji je na submitted varijabli ovdje zovem model i on odradi svoje
                st.write('Sada ću odgonetnuti žanr odabrane datoteke')
                time.sleep(2)
                for file_name in selected_files:
                    # ovdje zovem model
                    st.write(f"Datoteka: {file_name}, Tvoj žanr je: ovdje ce bit rezultat modela")

if __name__ == '__main__':
    audiorec_ver1()
