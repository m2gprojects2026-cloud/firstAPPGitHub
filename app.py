from sqlalchemy import create_engine
import streamlit as st

engine = create_engine(
    st.secrets["DATABASE_URL"]
)

with engine.connect() as conn:

    result = conn.execute(
        text("SELECT NOW()")
    )

    print(result.fetchone())
