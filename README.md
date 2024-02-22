CS50W Project 1- Django-based Wiki

This project was done following the specifications of the real Wikipedia. The application was built with Django, a Python-based framework used for web development.

The specifications are as follow:
-Any markdown content would be converted to HTML for display using python-markdown2 package.

-Entry Page: Visiting the entry page (/wiki/TITLE) would render a page displaying the contents of the entry TITLE by calling the appropriate util function. 
  Error page would appear if the requested entry does not exist.
  
-Index Page: User is able to click on any of the entries displayed and taken to the requested entry page.

-New Page: User can create a new page by clicking "Create New Page" option in the sidebar. 
  User will be taken to a page dedicated to creating a new entry. 
  If the entry created uses the same title as an entry that already exists, user will be presented with an error message. 
  Otherwise, the new entry will be saved and added to the Index Page. 
  
-Edit Page: Clicking a link to edit entry would take user to a textarea where they can edit the entry's Markdown content.

-Random Page: Clicking random page would take the user to a random encyclopedia entry.

-Search: This function allows the user to type a query into the search box in the sidebar to search for an entry.
  If the query matches with an entry, the user would be redirected to that entry page. 
  Otherwise, if the query matches any of the substring, the user would be presented with a page showing the entry pages containing the said substring in their titles. 
  For example, if the search query were ytho, then Python should appear in the search results. 
  Clicking on any of the entry names on the search results page should take the user to that entry’s page.
