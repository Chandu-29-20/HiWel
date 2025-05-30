import pandas as pd
from langchain_core.documents import Document


def dataconverter():
    product_data=pd.read_csv("C:\\Users\\Chandana\\Desktop\\E-Commerce-Chatbot1\\data\\mightymerge.io__th52bne0.csv")

    data=product_data[["product_title","review"]]

    product_list = []

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        # Construct an object with 'product_name' and 'review' attributes
        obj = {
                'product_name': row['product_title'],
                'review': row['review']
            }
        # Append the object to the list
        product_list.append(obj)

        
            
    docs = []
    for entry in product_list:
        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content=entry['review'], metadata=metadata)
        docs.append(doc)
    return docs