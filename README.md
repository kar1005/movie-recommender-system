# movie-recommender-system
**Key Technologies and Frameworks:**

* Streamlit: A web framework used to build a user-friendly interface for interacting with the recommender system.<br>
* Google Drive: Used for storing and downloading data files, providing a scalable solution for data storage.<br>
* Pickle: Used for serializing and deserializing data, allowing for efficient data transfer and storage.<br>
* Pandas: Used for data manipulation and analysis, providing a powerful tool for data processing.<br>
* os: Used for interacting with the file system, enabling the code to read and write files.<br>

**Architecture and Design Patterns:**<br>
<br>
* The code follows a simple, modular design, with clear separation of concerns between data loading, data processing, and recommendation generation.<br>
* The use of caching (Streamlit's `@st.cache_resource` decorator) optimizes data loading and reduces the load on the system.<br>
* The recommendation function is straightforward and easy to understand, making it a great starting point for further development.<br>
<br>
**Main Functionality and Features:**<br>

* The recommender system takes a movie title as input and returns a list of recommended movies based on the similarity matrix.<br>
* The system loads data from Google Drive files "movies.pkl" and "similarity.pkl" using the `load_data` function.<br>
* The data is stored in a Pandas DataFrame and a similarity matrix, allowing for efficient data processing and analysis.<br>
<br>
**Areas of Particular Interest for My Role:**<br>

* **Scalability Considerations:** While the current system is simple and efficient, it may not be able to handle a large number of users or a vast amount of data. I would recommend exploring solutions for scaling the system, such as distributed computing or cloud-based services.<br>
* **User Workflow and Customer Journey:** The current system assumes a straightforward user workflow, where users input a movie<br>
