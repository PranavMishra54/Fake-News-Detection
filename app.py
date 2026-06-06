import pickle

import streamlit as st


st.set_page_config(page_title="Fake News Detection")


@st.cache_resource
def load_assets():
    with open("model.pkl", "rb") as model_file:
        loaded_model = pickle.load(model_file)

    with open("vectorizer.pkl", "rb") as vectorizer_file:
        loaded_vectorizer = pickle.load(vectorizer_file)

    return loaded_model, loaded_vectorizer


try:
    model, vectorizer = load_assets()
except Exception as exc:
    st.error(f"Unable to load the saved model files: {exc}")
    st.stop()


st.title("Fake News Detection App")
st.write("Enter any news text below and the model will predict whether it is Real or Fake.")

user_input = st.text_area("Enter News Text Here")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        transformed_text = vectorizer.transform([user_input])
        prediction = model.predict(transformed_text)[0]

        if prediction == 1:
            st.success("This news appears to be **Real**.")
        else:
            st.error("This news appears to be **Fake**.")
