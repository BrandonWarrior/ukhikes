# Hiking Blog

## Overview

The **Hiking Blog** is a platform for outdoor enthusiasts to share, discover, and engage with hiking experiences. Users can create posts about their adventures, upvote or comment on other posts, and filter hikes by location and difficulty. The application is designed to be fully responsive and accessible across all devices.

For project planning, see: [Project Planning](planning.md)

---

## Features

### Core Features (MVP)

1. **User Registration and Authentication**:
   - Secure user registration and login.
   - Profile updates for showcasing user information and authored posts.

2. **Post Management**:
   - Create, edit, and delete posts with details like title, content, location, and difficulty.
   - Filter and search posts by location and difficulty.

3. **Community Interaction**:
   - Comment on posts to engage with the community.
   - Upvote/downvote posts to highlight the best content.

4. **Responsive Design**:
   - Fully responsive UI for desktop, tablet, and mobile devices.

5. **Admin Moderation**:
   - Admins can manage posts, comments, and users to maintain a positive community environment.

For a full list of planned features refer to the [Project Planning](planning.md) document.

---

## Installation and Setup

### Prerequisites

- Python 
- pip
- Virtual environment 

### Installation Steps

## Bugs and Fixes 

Bug 1: "ERR_SSL_PROTOCOL_ERROR" when running the server

- Cause: Tried accessing Django’s development server over HTTPS, but it only supports HTTP.

- Fix: Used http://127.0.0.1:8000/blog/ instead of https://.

Bug 5: "git push rejected" due to upstream issues

- Cause: The local Git branch was behind the remote repository.

- Fix: Pulled remote changes first using:
git pull origin main --rebase
## Credits 