# Reddit Mental Health Discussions EDA

This project contains an exploratory data analysis (EDA) notebook that analyzes Reddit posts related to mental health. The analysis was originally developed in Google Colab and covers various aspects such as data cleaning, text processing, visualization, and n-gram analysis.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Notebook Structure](#notebook-structure)
- [Results and Visualizations](#results-and-visualizations)
- [Team Members](#team-members)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

This notebook performs an in-depth exploratory data analysis on a dataset of Reddit posts related to mental health. The analysis includes:

- **Data Loading and Cleaning:** Importing data, handling missing values, and dropping unnecessary columns.
- **Text Processing:** Tokenization, stopword removal, lemmatization, and stemming.
- **Word Cloud Visualization:** Generating word clouds from the processed text, both overall and for specific subreddits.
- **Medication Mentions Analysis:** Identifying and visualizing mentions of various medications related to anxiety, depression, and ADHD.
- **Time Series Analysis:** Analyzing daily post frequency over time.
- **User Engagement Analysis:** Evaluating active subreddits, top posts, and user activity.
- **N-gram Analysis:** Extracting and visualizing bigrams and trigrams for each subreddit.
- **Additional EDA:** Detailed analysis on disease category post frequency and top author activity.

## Features

- **Comprehensive Data Cleaning & Preprocessing:** Handles missing values, standardizes text, and drops irrelevant columns.
- **Advanced Text Processing:** Uses NLTK for tokenization and spaCy for lemmatization.
- **Visual Insights:** Creates word clouds, line plots, bar charts, and heatmaps.
- **Medication Analysis:** Separates and visualizes mentions for different medication categories.
- **N-gram Analysis:** Extracts and plots the most frequent bigrams and trigrams by subreddit.

## Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **Jupyter Notebook** or **Google Colab**

Python libraries required:

- `pandas`
- `numpy`
- `nltk`
- `spacy` (with the `en_core_web_sm` model)
- `matplotlib`
- `wordcloud`
- `seaborn`

## Usage

### Open the Notebook

Open `DSCI_591_EDA_22nd_March.ipynb` in Jupyter Notebook or upload it to Google Colab.

### Run the Notebook

Execute each cell sequentially to perform the following tasks:

- **Data Loading:** Load the CSV dataset (`reddit_posts_combined_26Jan_16Mar.csv`) and inspect its structure.
- **Data Cleaning:** Handle missing values by dropping rows with missing text and filling missing authors.
- **Text Processing:** Tokenize, remove stopwords, and lemmatize text.
- **Word Cloud Generation:** Create general and subreddit-specific word clouds.
- **Medication Analysis:** Identify and visualize medication mentions for anxiety, depression, and ADHD.
- **Time Series Analysis:** Plot daily post frequencies.
- **User Engagement Analysis:** Analyze active subreddits, top posts, and users.
- **N-gram Analysis:** Extract and visualize bigrams and trigrams.
- **Additional EDA:** Further analyze disease category posting frequency and top author posting trends.

## Notebook Structure

The notebook is organized into the following sections:

- **Dataset Loading:** Import libraries, download resources, and load the CSV dataset.
- **Data Cleaning & Preprocessing:** Check and handle missing values, drop unnecessary columns, and save the cleaned dataset.
- **Text Processing:** Tokenization, lemmatization, and creation of new text columns.
- **Word Cloud Visualization:** Generate word clouds for overall processed text and subreddit-specific data.
- **Medication Mentions Analysis:** Analyze and visualize mentions of medications.
- **Time Series Analysis:** Convert date columns and plot the frequency of posts over time.
- **User Engagement & Subreddit Activity Analysis:** Visualize the activity of subreddits, posts, and users.
- **N-gram Analysis:** Extract and visualize top bigrams and trigrams for each subreddit.
- **Additional EDA:** Additional plots including disease category trends and top author activity analysis.

## Results and Visualizations

The notebook produces several visual outputs:

- **Word Clouds:** For tokenized, lemmatized, and merged text.
- **Time Series Plots:** Showing daily post frequency.
- **Bar Charts:** For top subreddits and active users.
- **Heatmaps:** For top authors across different subreddits.
- **N-gram Bar Plots:** For bigram and trigram frequencies by subreddit.

## Team Members

**Group 11 - NeuroNexus**

- Aman Ostwal
- Darshit Rai
- Sai Pokuri
- Sanjoli Sogani# Predicting-Mental-Health-Trends
