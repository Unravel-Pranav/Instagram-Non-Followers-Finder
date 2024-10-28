import json
import streamlit as st
from io import StringIO

# Function to process JSON data and return users who don't follow back
def find_non_followers(followers_data, following_data):
    try:
        # Extract followers usernames
        followers_usernames = {
            user["string_list_data"][0]["value"]
            for user in followers_data
            if isinstance(user, dict) and "string_list_data" in user and user["string_list_data"]
        }

        # Extract following usernames
        following_usernames = {
            user["string_list_data"][0]["value"]
            for user in following_data.get("relationships_following", [])
            if isinstance(user, dict) and "string_list_data" in user and user["string_list_data"]
        }

        # Find users who are followed but do not follow back
        not_following_back = following_usernames - followers_usernames
        return followers_usernames, following_usernames, not_following_back

    except (IndexError, KeyError, TypeError):
        st.error("Error in JSON structure. Please check your files.")
        return None, None, None

# Streamlit interface
st.title("Instagram Non-Followers Finder")

# Upload JSON files
followers_file = st.file_uploader("Upload your followers JSON file", type="json")
following_file = st.file_uploader("Upload your following JSON file", type="json")

# Process files if both are uploaded
if followers_file and following_file:
    # Load JSON data
    followers_data = json.load(followers_file)
    following_data = json.load(following_file)

    # Find users who don't follow back
    followers_usernames, following_usernames, not_following_back = find_non_followers(followers_data, following_data)

    # Display result and provide download link if list is generated
    if not_following_back is not None:
        # Count followers and non-followers
        count_followers = len(followers_usernames)
        count_following = len(following_usernames)
        count_non_followers = len(not_following_back)

        # Display counts
        st.write(f"Total Followers: {count_followers}")
        st.write(f"Total Following: {count_following}")
        st.write(f"Non-Followers (You follow but they don't follow back): {count_non_followers}")

        # Add interactive options
        show_non_followers = st.checkbox("Show non-followers list")
        download_non_followers = st.button("Download non-followers list")

        if show_non_followers:
            if not_following_back:
                st.write("**Users you follow but who don't follow you back:**")
                # Display each non-follower with spacing
                for user in not_following_back:
                    st.write(f"- {user}")  # Use bullet points for better readability
            else:
                st.success("All users you follow also follow you back!")

        if download_non_followers:
            if not_following_back:
                # Prepare the text output
                output_text = "Users you follow but who don't follow you back:\n" + "\n".join(not_following_back)
                
                # Create a downloadable text file
                output_file = StringIO(output_text)
                output_file.seek(0)

                st.download_button(
                    label="Download list of non-followers",
                    data=output_file.getvalue(),
                    file_name="not_following_back.txt",
                    mime="text/plain"
                )
            else:
                st.warning("No non-followers to download.")
