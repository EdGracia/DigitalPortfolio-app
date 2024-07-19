import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Blog Posts", page_icon="✍️", layout= "wide")


#---Sidebar-----
st.sidebar.title("Blog ✍️")
st.sidebar.subheader("Posts about my projects")


#----Header-----
st.title("Blog ✍️")


#---------------------------------BLOG STUFF--------------------------------------------------------------


#---Setting up blog database---

with open("pages/blog.txt") as f:
    blogsRaw = f.readlines()

blogs = []



# Define some functions for interacting with the database
def add_post(author, title, content, date, time):
    with open("pages/blog.txt", "a") as f:
        f.write(author + "\n")
        f.write(title + "\n")
        f.write(content + "\n")
        f.write(str(date) + "\n")
        f.write(time + "\n")

def get_all_posts():
    blogs = []
    #parses raw into individual posts
    for i in range(1, len(blogsRaw) - 1, 5):
        blogs.append(blogsRaw[i - 1: i + 4])

    return blogs



def delete_post(title):
    target = 0
    for i in range(len(blogs) -1):
        temp = []
        temp = blogs[i]
        if temp[1] == title:
            target = (i * 5)

    with open("pages/blog.txt") as f:
        lines = f.readlines()

    for i in range(5):
        lines.pop(target)

    open("pages/blog.txt").close()

    with open("pages/blog.txt", "w") as f:
        for line in lines:
            f.write(line)


# Define some HTML templates for displaying the posts
title_temp = """
<div style="background-color:#858585;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Author: {}</h6>
<br/>
<br/>
<p style="text-align:justify"> {}</p>
</div>
"""

post_temp = """
<div style="background-color:#586e75;padding:10px;border-radius:5px;margin:10px;">
<h4 style="text-align:center;">{}</h4> 
<h6>Author: {}</h6> 
<img src="https://mail.google.com/mail/u/0?ui=2&ik=41fed2199a&attid=0.2&permmsgid=msg-a:r4276339577935421273&th=1902702e71a7485c&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ8dqyLILxESsWNa91TS2kyQESirRHXgwPGy80LCVp39dirtdbKkLLIFdRo8JxfkOsIsz0Gzq7SNKHM9KHEcCFJj-joOzku55uLdLEBKjHahDFK73llmkpPGQps&disp=emb&realattid=ii_lxj6q0w51" alt="Avatar" style="vertical-align: middle;width: 60px;height: 60px;border-radius: 50%;">
<br/>
<br/>
<h6 style="color:#002B36;">Date: {}</h6> 
<p "text-align:justify"> {}</p>
<hr>
<h6 style="color:#002B36;">Time: {}</h6>
</div>
"""

# Create a sidebar menu with different options
menu = ["View Posts", "Add Post", "Search", "Manage"]
choice = st.sidebar.selectbox("Menu", menu)


if choice == "View Posts":
    st.subheader("Blog posts consist of my thoughts, challenges, successes, and overall workflow of my projects.")
    st.write("Hope you enjoy!")
    #st.header("View Posts")
    #st.write("Here you can see all the posts in the blog.")
    # Get all the posts from the database
    posts = get_all_posts()
    # Display each post as a card
    for post in posts[::-1]:
        #st.markdown(title_temp.format(post[1], post[0], post[2][:50] + "..."), unsafe_allow_html=True)
        # Add a button to view the full post
        #if st.button("Read More", key=post[1]):
        st.markdown(post_temp.format(post[1], post[0], post[3], post[2], post[4]), unsafe_allow_html=True)

elif choice == "Add Post":
    st.header("Add Post")
    st.write("Here you can add a new post to the blog.")
    passcode = st.text_input("Enter the Passcode to submit blog posts: ")
    if passcode == "Airplane8!":
        # Create a form to get the post details
        with st.form(key="add_form"):
            author = st.text_input("Author")
            title = st.text_input("Title")
            content = st.text_area("Content")
            date = st.date_input("Date")
            time = st.text_input("Time")
            submit = st.form_submit_button("Submit")
        # If the form is submitted, add the post to the database
        if submit:
            add_post(author, title, content, date, str(time))
            st.success("Post added successfully")
    else:
        st.write("Incorrect password... if you are not Ed Gracia you cannot write a blog post")
elif choice == "Search":
    st.header("Search")
    st.write("Here you can search for a post by title or author.")
    # Create a text input to get the search query
    query = st.text_input("Enter your query")
    # If the query is not empty, search for the matching posts
    if query:
        # Get all the posts from the database
        posts = get_all_posts()
        # Filter the posts by the query
        results = [post for post in posts if query.lower() in post[0].lower() or query.lower() in post[1].lower()]
        # Display the results
        if results:
            st.write(f"Found {len(results)} matching posts:")
            for result in results:
                #st.markdown(title_temp.format(result[1], result[0], result[2][:50] + "..."), unsafe_allow_html=True)
                # Add a button to view the full post
                #if st.button("Read More", key=result[1]):
                st.markdown(post_temp.format(result[1], result[0], result[3], result[2], result[4]), unsafe_allow_html=True)
        else:
            st.write("No matching posts found")

elif choice == "Manage":
    st.header("Manage")
    st.write("Here you can delete posts or view some statistics.")
    # Create a selectbox to choose a post to delete
    titles = [post[1] for post in get_all_posts()]
    title = st.selectbox("Select a post to inspect", titles)
    # Add a button to confirm the deletion
    delete_pass = st.text_input("Enter the password to delete this post: ")
    if delete_pass == "Airplane8!":
        if st.button("Delete") and delete_pass == "Airplane8!":
            delete_post(title)
            st.success("Post deleted successfully")
    # Create a checkbox to show some statistics
    if st.checkbox("Show statistics"):
        # Get all the posts from the database
        posts = get_all_posts()
        # Convert the posts to a dataframe
        df = pd.DataFrame(posts, columns=["author", "title", "content", "date", "time"])
        # Display some basic statistics
        st.write("Number of posts:", len(posts))
        st.write("Number of authors:", len(df["author"].unique()))
        st.write("Most recent post:", df["date"].max())
        st.write("Oldest post:", df["date"].min())
        # Display a bar chart of posts by author
        st.write("Posts by author:")
        author_count = df["author"].value_counts()
        st.bar_chart(author_count)

