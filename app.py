import streamlit as st
import uuid
from utils import *
import os
from dotenv import load_dotenv



# Access the environment variables


def main():

    load_dotenv()

    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    PINECONE_ENV = os.getenv('PINECONE_ENV')

    st.set_page_config(page_title="Resume Screening Tool")
    st.title("Project Horizon")
    st.subheader("Shortlisting resumes:")

    shortlist_desc= st.text_area("Paste Shortlisting requirements here :", key="1")
    doc_count= st.text_input("No. of Resumes to return",key="2")

    pdf= st.file_uploader("Upload resumes here (PDF Format only)", type=["pdf"],accept_multiple_files=True)

    submit = st.button("Shortlist Resumes")

    if submit:
        with st.spinner('Getting you the best participants :'):

            st.write("Process")
            st.session_state['unique_id']=uuid.uuid4().hex
            #st.write(st.session_state['unique_id'])

            #Create docs

            final_docs_list=create_docs(pdf,st.session_state['unique_id'])
            
            #Displaying the count of resumes that have been uploaded
            st.write("*Resumes uploaded* :"+str(len(final_docs_list)))


            #create embeddings instance
            embeddings=create_embeddings_load_data()


            #Push data to PINECONE
            push_to_pinecone(PINECONE_API_KEY,PINECONE_ENV,"resume",embeddings,final_docs_list)


            #Fetch relevant docs from PINECONE

            relevant_docs= similar_docs(shortlist_desc,doc_count,PINECONE_API_KEY,PINECONE_ENV,"resume",embeddings,st.session_state['unique_id'])

            #st.write(relevant_docs)


            #Introducing line seperator:

            st.write(":heavy_minus_sign:" *30)

            for item in range(len(relevant_docs)):

                st.subheader(+str(item+1))

                st.write("**File** :"+relevant_docs[item][0].metadata['name'])

                #Introducing expander feature

                with st.expander("Show Results"):
                    st.info("**Match Score** : "+str(relevant_docs[item][1]*100+" % "))

                    summary = get_summary(relevant_docs[item[0]])
                    st.write("*Summary* :"+summary)

        st.success("Enjoy Hacking!")


if __name__ == "__main__":
    main()