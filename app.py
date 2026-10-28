from sqlalchemy import create_engine, text
import streamlit as st

try:

    url = st.secrets["DATABASE_URL"]

    st.write("URL encontrada ✅")

    # Oculta la contraseña
    st.write(
        url.replace(
            url.split(":")[2].split("@")[0],
            "*****"
        )
    )

    engine = create_engine(url)

    with engine.connect() as conn:

        resultado = conn.execute(
            text("SELECT NOW()")
        )

        st.success("✅ Conexión exitosa")

        st.write(resultado.fetchone())

except Exception as e:

    st.error(f"❌ Error: {e}")

    import traceback

    st.code(traceback.format_exc())
