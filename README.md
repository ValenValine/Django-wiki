## Django Wikipedia Clone

## Project Background

This project was developed as part of CS50W at Harvard University. This project is a clone of Wikipedia, built following the specifications of the real Wikipedia. It was developed using Django, a Python-based framework for web development.


## Specifications

    Markdown Conversion: Any Markdown content is converted to HTML for display using the python-markdown2 package.

    Entry Page: Visiting the entry page (/wiki/TITLE) renders a page displaying the contents of the entry TITLE. If the requested entry does not exist, an error page is displayed.

    Index Page: Users can click on any of the entries displayed on the index page and are taken to the requested entry page.

    New Page: Users can create a new page by clicking the "Create New Page" option in the sidebar. They are then taken to a page dedicated to creating a new entry. If the entry created uses the same title as an existing entry, an error message is displayed. Otherwise, the new entry is saved and added to the index page.

    Edit Page: Clicking a link to edit an entry takes the user to a textarea where they can edit the entry's Markdown content.

    Random Page: Clicking on the "Random Page" option takes the user to a random encyclopedia entry.

    Search: Users can type a query into the search box in the sidebar to search for an entry. If the query matches an entry, the user is redirected to that entry page. If the query matches any substring of an entry title, the user is presented with a page showing the entry pages containing the said substring in their titles. Clicking on any of the entry names on the search results page takes the user to that entry’s page.


## Installation

To run the project locally, follow these steps:

    Clone this repository to your local machine.
    Install the required dependencies by running pip install -r requirements.txt.
    Run the Django development server using python manage.py runserver.
    Access the application in your web browser at http://localhost:8000.


## Usage

Once the application is running, you can interact with it through your web browser. Navigate to different pages using the provided links and features such as entry pages, creating new pages, editing pages, searching, and accessing random pages.


## License

This project is for educational purposes only. It is not intended for commercial use or redistribution. All rights reserved. 
