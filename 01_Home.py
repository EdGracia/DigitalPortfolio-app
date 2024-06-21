import streamlit as st



st.set_page_config(page_title="Ed Gracia", page_icon="👨‍💻", layout= "wide")

#Use local CSS style
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---Sidebar-----
st.sidebar.title("Home 👨‍💻")
st.sidebar.subheader("About Me information")
st.sidebar.subheader("Contact Me")
#-----Header------
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Hi, I am Ed :wave:")
        st.write("Eduardo Gracia Panini")
        st.subheader("Software Engineering student at the University of Miami")

        st.write("I am passionate about expanding my knowledge on all things programming, data science, and artificial intelligence.")


    with right_column:
        headshot = st.image('images/headshot.png', width=200,
                            output_format="PNG")

#----About me------------
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("---")
        st.header("About Me:")
        st.subheader("⚪️️     The Loomis Chaffee School Graduate")
        st.write("Graduated from the prestigious New England boarding school in 2024")
        st.write(" ")
        st.subheader("⚪️     University of Miami Software Engineering Student")
        st.write("'Canes Achievement Scholarship recipient")

    with right_column:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        loomis = st.image('images/loomislogo.jpeg', width=200,
                            output_format="PNG")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        miami = st.image('images/umiamilogo.png', width=200,
                            output_format="PNG")


#--------Contact Form-------------------------------
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write('##')

contact_form = """
<form action=""https://formsubmit.co/talogracia@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()


