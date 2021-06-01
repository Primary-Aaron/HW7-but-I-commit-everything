Question 3: test-driving in social media platform context

I'd probably want to test errors for uploading files that are too big or writing posts too long, so I'd write tests for each error making sure that the right error is caught. That might look like this:

1: create a test that asserts a certain flag is called
2: implement a an error handling method to limit file size or total characters in a posts
3: test for some kind of message that I want to print on the screen when the error happens
4: assert that the error message is properly displayed


DISCLAIMER:

each commit happens within second of eachother which I feel looks suspicious, so I'll
clarify that each commit was so close together because I did the assignment twice, but I
didn't do as many commits and was scared of losing points, so I copy/pasted the code 
step by step to make sure I didn't miss any commits that might have gotten me points

for proof that I did all my own work, here's a link to my other repository where I was worried I didn't do enough commits:

https://github.com/Primary-Aaron/HW7