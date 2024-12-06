import instaloader

# Initialize Instaloader
L = instaloader.Instaloader()

# Prompt user to enter the Instagram username
username = input("Enter the Instagram username: ")  # User inputs the Instagram username

# Fetch profile data
profile = instaloader.Profile.from_username(L.context, username)

# Open a text file to save the data
with open(f"{username}_profile_data.txt", "w", encoding="utf-8") as file:
    # Write profile information to the file in a table-like format
    file.write(f"{'Profile Information'.center(50, '-')}\n")
    file.write(f"{'Username:':<20} {profile.username}\n")
    file.write(f"{'Full Name:':<20} {profile.full_name}\n")
    file.write(f"{'Bio:':<20} {profile.biography}\n")
    file.write(f"{'Followers:':<20} {profile.followers}\n")
    file.write(f"{'Following:':<20} {profile.followees}\n")
    file.write(f"{'Posts:':<20} {profile.mediacount}\n")
    file.write(f"{'Is Verified:':<20} {profile.is_verified}\n")
    
    file.write("\n" + "-"*50 + "\n")
    
    # Write recent posts information in a table format
    file.write(f"{'Recent Posts:'.center(50, '-')}\n")
    file.write(f"{'Post URL':<50} {'Likes':<10} {'Comments':<10} {'Caption'}\n")
    file.write("-" * 80 + "\n")
    
    for post in profile.get_posts():
        file.write(f"{post.url:<50} {post.likes:<10} {post.comments:<10} {post.caption[:50]}...\n")
    
    file.write("-" * 80 + "\n")

print(f"Profile data has been saved to {username}_profile_data.txt")
