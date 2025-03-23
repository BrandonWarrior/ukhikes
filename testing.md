# **UK Hikes - Testing Documentation**

## **Overview**

This document outlines the testing process for the **UK Hikes Django Blog** project. The testing phase ensures that the web application functions correctly, meets its requirements, and provides a smooth user experience.

---

## **1. Types of Tests**

### **Flake8 and PEP8**

- The code was tested using **Flake8** to ensure it adheres to **PEP8** standards. The code passes without errors, ensuring consistent formatting.

---

### **Manual Testing**

#### **Tested Areas**:

1. **User Registration**:
   - Tested user registration and login, ensuring that only valid credentials were accepted.
   
2. **Post Management**:
   - Verified that users could create, edit, and delete hiking posts.
   
3. **Testimonials**:
   - Verified that users could leave testimonials on hiking posts.
   
4. **Search**:
   - Ensured that users could search for posts by title or content.
   
5. **Commenting**:
   - Ensured that users could leave and delete comments on hiking posts.


**Lighthouse Performance Scores**
As part of the overall testing process, Google Lighthouse was used to assess key aspects of the **UK Hikes Django Blog** in terms of performance, accessibility, SEO, and best practices. Lighthouse provides valuable insights into the web application's strengths and areas for improvement.



---

## **2. Deployment**

To deploy this app on **Heroku**, follow these steps:

1. Fork or clone the repository.
2. Create a new Heroku app.
3. Set up the necessary environment variables (e.g., `DEBUG=False`, `SECRET_KEY=<your_secret_key>`).
4. Link the repository to Heroku and deploy it using Git.
5. Run `python manage.py migrate` to apply migrations on Heroku.

---

## **3. Bugs and Fixes**

### **1. Database Migration Issue**:
- **Bug**: Encountered an issue with database migrations not applying correctly.
- **Fix**: Ran `python manage.py makemigrations` followed by `python manage.py migrate` to ensure the database schema was up to date.

### **2. Static Files Not Loading on Deployment**:
- **Bug**: Static files were not served correctly after deployment to Heroku.
- **Fix**: Configured `STATIC_ROOT` and ran `collectstatic` on Heroku.

---

## **4. Future Testing**

In future development, additional tests will be added for the following features:
- **Filter Functionality**: Automated tests to verify the correct behaviour of the filter feature (location and difficulty).
- **Upvote/Downvote System**: Automated tests for voting functionality.
- **Hike Rating**: Tests to verify the correct rating system and calculations.

---

## **5. Conclusion**

This testing phase ensured that key features of the **UK Hikes Django Blog** work correctly and that the code adheres to best practices in terms of functionality and quality. Manual testing was used to verify user interactions, while automated tests helped ensure the integrity of the models, views, and forms.

---

## **Credits**

- **Django Framework** for the built-in testing tools.
- **Flake8** for ensuring adherence to PEP8 guidelines.
- **GitHub Issues** for tracking bugs and feature requests during testing.
- **Stack Overflow** for resolving any technical questions that arose during testing.
