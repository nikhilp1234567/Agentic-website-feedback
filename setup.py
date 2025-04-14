from setuptools import setup, find_packages

setup(
    name='Agentic-website-feedback',  # Replace with your project's name
    version='0.1',  # Replace with your project's version
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        'langchain-google-genai',
        'pydantic',
        'python-dotenv',
        'asyncio',
        'overrides',
        # Add any other dependencies used in agent.py
    ],
    description='An agent for automating website usability feedback',  # Replace with a short description
    long_description=open('README.md').read(),  # Read the long description from a README file
    long_description_content_type='text/markdown',  # Specify the content type of the long description
    url='https://github.com/nikhilp1234567/Agentic-website-feedback',  # Replace with the URL of your GitHub repository
    author='Nikhil, Engombe',  # Replace with your name
    license='MIT',  # Replace with your project's license
    classifiers=[
        # Classifiers help users find your project by categorizing it
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',  # Specify the Python version requirements
)
