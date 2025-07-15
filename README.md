# 🎬 Movie Recommendation System

---

## 📌 Project Name
**Movie Recommendation System using Content-Based Filtering**

---

## 🧩 Problem Statement

In today's digital world, users are overwhelmed with vast amounts of movie content on various platforms. It's difficult for users to discover movies they would enjoy without spending time browsing or relying on arbitrary suggestions.

> **Objective:** Build a recommendation system that helps users discover movies similar to a selected title based on content like genres, cast, director, and more.

---

## 💡 Solution Approach

We built a **Content-Based Movie Recommender** that uses **Natural Language Processing (NLP)** and **vector similarity techniques** to recommend movies.

### 🔧 Key Steps:

1. **Dataset Preparation**:
   - Used TMDb (The Movie Database) dataset: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
   - Merged, cleaned, and preprocessed data.

2. **Text Preprocessing**:
   - Extracted relevant features: genres, keywords, cast, crew.
   - Combined them into a unified `tags` column.
   - Applied **Stemming** using NLTK for normalization.

3. **Feature Extraction**:
   - Converted text data into numerical form using **CountVectorizer** with top 5000 features.

4. **Similarity Computation**:
   - Calculated pairwise **cosine similarity** between movie vectors.

5. **Recommendation Engine**:
   - Returned top 5 similar movies to the selected title using the precomputed similarity matrix.

6. **Deployment**:
   - Built an interactive **web app using Streamlit**.
   - Allows users to select a movie and see recommendations with posters and descriptions.

---

## 🔍 Observations

- Data required heavy preprocessing: especially nested JSON columns for cast and crew.
- Some movies had missing values or no similarity due to limited metadata.
- Using more descriptive metadata like overview/keywords improves recommendation quality.

---

## 📊 Findings

- Movies from the same **genre** and **director** were often rated highly in similarity.
- The addition of **cast** and **keywords** increased diversity in recommendations.
- Using **stemming** reduced vector noise and improved grouping of similar content.

---

## 📈 Insights

- **Content-based filtering** works well even with no user history — good for cold-start users.
- Lightweight ML with vectorization and cosine similarity is fast and deployable.
- Adding external APIs (like OMDb/TMDB) enhances the user interface with images and ratings.
- Can be extended to **hybrid recommendation** by combining user ratings (collaborative filtering).

---

## 🚀 Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **NLTK (Stemming)**
- **Scikit-learn (CountVectorizer, cosine_similarity)**
- **Streamlit (Web App)**
- **Pickle (Model saving/loading)**

---

## 🖼️ Sample UI

Users select a movie from the dropdown and get:
- 🖼 Movie Posters
- 📖 Short Descriptions
- ⭐ Ratings (Optional)
- 🎬 Similar Movie Titles

---

