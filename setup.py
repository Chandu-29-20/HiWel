from setuptools import setup, find_packages

setup(
    name='ecommbot',
    version='1.0.0',
    description='An E-Commerce chatbot using LangChain and Gemini for product recommendations.',
    author='Chandana',
    author_email='chandanayadav82153@gmail.com',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'langchain-core',
        'langchain-community',
        'langchain-google-genai',
        'langchain-huggingface',
        'sentence-transformers',
        'faiss-cpu',
        'python-dotenv',
        'flask',
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
