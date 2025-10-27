import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import toml

# Load CodeLlama Model
@st.cache_resource
def load_model():
    try:
        tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Instruct-hf")
        model = AutoModelForCausalLM.from_pretrained("codellama/CodeLlama-7b-Instruct-hf", torch_dtype=torch.float16, device_map="auto")
        return pipeline("text-generation", model=model, tokenizer=tokenizer)
    except Exception as e:
        st.error(f"Error loading CodeLlama model: {e}")
        return None

code_generator = load_model()

def generate_code(prompt, language, max_length=200, temperature=0.5):
    formatted_prompt = f"[INST] Write a {language} program that does the following:\n{prompt}\n[/INST]"
    result = code_generator(
        formatted_prompt,
        max_length=max_length,
        do_sample=True,
        temperature=temperature,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1
    )
    return result[0]['generated_text']

# Streamlit UI

# Page config
st.set_page_config(page_title="CodeCraft", layout="wide")

def main():

    # Global CSS for background and text colors
    st.markdown(
        """
        <style>
            body {
                background-color: #0F1117;
            }
            .main {
                background-color: #0F1117;
                color: white;
            }
            .block-container {
                padding-top: 2rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header / Branding
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1 style='font-size: 59px; font-weight: bold; margin-bottom: 0;'>
                <span style='color: #6EC1E4;'>Code</span>
                <span style='background-color: #B388EB; color: white; padding: 5px 10px; border-radius: 8px;'>Craft</span>
            </h1>
            <p style='color: #AAAAAA; font-size: 18px;'>Create code like a pro with AI assistance</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # Main inputs
    col1, col2 = st.columns([2, 1])

    with col1:
        user_prompt = st.text_area(
            "📝 **What do you want to build or ask about?**",
            height=200
        )

    with col2:
        option = st.selectbox('💬 **Choose a Language**', ('Python', 'Java', 'C', 'C++'))

        # Sidebar settings
        st.sidebar.header("⚙️ Generation Settings")
        max_length = st.sidebar.slider(
            "🔢 Max Code Length",
            min_value=50, max_value=500, value=200, step=50
        )
        temperature = st.sidebar.slider(
            "🎨 Creativity (Temperature)",
            min_value=0.1, max_value=1.0, value=0.5, step=0.1
        )

    st.markdown("")

    # Generate button & output
    if st.button("🚀 Generate Code"):
        if user_prompt.strip():
            if 'code_generator' in globals():
                with st.spinner("Generating your code..."):
                    code = generate_code(user_prompt, option, max_length, temperature)
                st.success("✅ Code generated successfully!")
                st.subheader("📄 Generated Code:")
                st.code(code, language=option.lower())

                # 🌟 Download Button Added Here
                extension_map = {
                    "Python": "py",
                    "Java": "java",
                    "C": "c",
                    "C++": "cpp"
                }
                file_extension = extension_map.get(option, "txt")

                st.download_button(
                    label="💾 Download Code",
                    data=code,
                    file_name=f"generated_code.{file_extension}",
                    mime="text/plain"
                )

            else:
                st.error("❌ Code generation model not loaded.")
        else:
            st.warning("⚠️ Please enter a valid input.")

if __name__ == '__main__':
    main()
