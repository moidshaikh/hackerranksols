'''

The first step in creating the micro-blogging website is to create the interface mock-up. There are a number of critical pages that will need to be created and linked together to illustrate the interface features. For those pages that will ultimately contain user-contributed data, they can be loaded with sample data to illustrate the design. You should start by sketching each page, and then build it using HTML5 and CSS.
The following pages are to be created:
1. Login Page
The purpose of this page is to provide branding for your micro-blogging site, and to allow the user to enter their username and password to login.
2. Sign-up Form
This form should collect the information required for creating a new account on your micro-blogging site. At the least, it should collect an email address, username, date of birth, image/graphic, and a password. The form should ask the user to enter their password twice, to ensure that it is entered properly.
3. Posting List Page
This is the default page for the micro-blogging site, showing the postings of all users ordered by date/time of entry (most recent first). Eventually, it will be loaded with content extracted from the database; for now, it can be loaded with sample information. Each posting should include the content of the microblogging post, the date/time of the posting, the username of the poster, and the image/graphic for the user. There should be a link for re-posting another user’s post, six icons with names similar to the ones used in Facebook’s Reaction buttons that allow the user to like or give a different reaction to the post, and a count on the number of likes and other reactions. At least one of the sample postings should include a URL; at least one should include a link to another user (using @username syntax); and at least one should be a re-post. (LIKE , LOVE, HAHA, WOW, SAD, ANGRY) Facebook Reactions Example Note that this will be the home page for the application. In the final version, this can be viewed by anyone, but only those who are logged in will be able to post, re-post, or indicate that they have a “Reaction” to the post. These details will be implemented in subsequent assignments.
4. Posting Form
This is the form that will be used to make a posting. It should allow the user to enter the text of their posting. Eventually, you will write software to ensure that only logged-in users can make postings, and control the length of the posting.
5. Re-post Form
This is the form that will be used to make a re-posting. It will be shown after the user clicks on the re-post link (see above). The details of the original post will be shown, and the user should be allowed to enter the text of their own as comments on the post. Eventually, you will write software to ensure that only logged-in users can re-post.
6. User Detail Page
This is the page that will be shown when a user clicks the username of a poster (or a username within the body of a posting). It should show the details for the selected user, along with an ordered list of all of their postings and re-postings (in the same format as the posting list page).
You must ensure that each of these pages makes appropriate use of HTML5 (following the syntax rules of XHTML) and CSS, and construct them such that there is a proper separation of the specification of the content from the specification of the presentation rules. Your submission should include six sketches (one per page), six HTML5 pages, and a single CSS file.


'''