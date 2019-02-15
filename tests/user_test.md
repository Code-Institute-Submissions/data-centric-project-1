### User Testing

As I deployed a new feature, I did manual tests to check the UI and UX worked as expected.
Below is a list of features and the tests I carried out:

- Add Book Form
    - Navbar Link goes to "Add Book" page
    - Try to submit empty form and required input error stops submit
    - Try submit more than the main author or one genre and validation highlights relevant help text
    - Enter all inputs and submit redirects user to the "Book Record" they just added successfully
    - "Clear" button clears form

- Edit Book Form
    - "Edit" button in "Book Record" goes to "Edit Book" page
    - Form is prepopulated with Book details from DB
    - Try submit form with an empty input and required input error stops submit
    - Try submit more than the main author or one genre and validation highlights relevant help text
    - Enter edit any inputs and submit redirects user to the "Book Record" they just edited successfully

- Delete Book
    - "Delete?" button in "Book Record" opens a confirmation modal
    - "Close" button closes modal
    - "Delete" button deletes relevant book from DB and redirects user to Homepage

- Full Text Search
    - Try to submit with empty input and required input error stops submit
    - Search word or pharse redirects to results page with results of the search term
    - Quick Search buttons redirects to results page with results of the search term
    - Results can be sorted and filtered, by genre and author, or clear filters to return to search term
    - Sorting and Filtering can be done in any order and if not results are found will display "No results Found"

- View Book
    - "View Book" button redirects to "Book Record" page with relevant book id
    - "Book Record" page displays relevant details for book selected
    - Ratings Chart displays relevant ratings data for book

- Review Form
    - "Write a review" button displays Review Form on "Book Record" page
    - Try to submit empty form and required input error stops submit
    - Enter all inputs and submit adds a review to "Book Record" page for user to see
    - Successful reviews also add to rating data which updates the rating chart

- Recommend Form
    - Try to submit empty form and required input error stops submit
    - Enter a username that does not exist in users DB will display "This username does not exist. Please try again."
    - Enter a username that is in users DB will display "This has been Successfully Recommended"

- My Books Login
    - Try to submit empty Register form and required input error stops submit
    - Try to submit empty Login form and required input error stops submit
    - Enter input for Register form and submit redirects to "My Books" for username
    - Enter input for Register form that already exists and submit displays "This username is not available. Please try again."
    - Enter input for Login form and submit redirects to "My Books" for username
    - Enter input for Login form that doesn't exist and submit displays "This username does not exist. Please try again or Register."

