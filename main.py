import streamlit as st
from db import SessionLocal, init_db
from models import Conversation
from groq_client import ask_groq

# Iniciar la base de datos
init_db()

st.title(" Agente IA con Groq")

question = st.text_input("Haz tu pregunta:")
if st.button("Enviar") and question:
    with st.spinner("Procesando con Groq..."):
        answer = ask_groq(question)

        # Mostrar respuesta
        st.text_area("Respuesta:", value=answer, height=200)

        # Guardar en la base de datos
        db = SessionLocal()
        new_entry = Conversation(question=question, answer=answer)
        db.add(new_entry)
        db.commit()
        db.close()


# # Mostrar historial guardado
# st.subheader("Historial de conversaciones")
# db = SessionLocal()
# results = db.query(Conversation).order_by(Conversation.created_at.desc()).limit(10).all()
# for entry in results:
#     st.markdown(f"**🗨️ Pregunta:** {entry.question}")
#     st.markdown(f"**💬 Respuesta:** {entry.answer}")
#     st.markdown("---")
# db.close()
