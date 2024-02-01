

 # Resume Screening Tool

Welcome to the Resume Screening Tool - a powerful utility to assist with the process of shortlisting resumes based on job descriptions and criteria. This tool leverages state-of-the-art NLP models and Pinecone vector storage to help HR professionals streamline their candidate selection process.
![image](https://github.com/aryan4codes/Resume-Shortlisting-Tool/assets/122562400/944c8325-416a-4ad0-9fa9-91962eb0c21f)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Resume Screening Tool is designed to automate and simplify the resume shortlisting process. It uses natural language processing (NLP) to analyze resumes, match them with job descriptions, and provide relevant candidates. Pinecone is used as the vector storage to efficiently store and retrieve the document embeddings for quick and accurate similarity searches.

## Features

- Upload multiple resumes in PDF format.
- Paste the job description for which you want to screen resumes.
- Retrieve a specified number of top matching resumes based on the job description.
- Utilize SentenceTransformer for generating document embeddings.
- Seamlessly integrate with Pinecone for vector storage and similarity search.
- Get summaries of the top matching resumes for quick review.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/resume-screening-tool.git
