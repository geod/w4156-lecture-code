# w4156 Labs
The following individual lab exercise apply the concepts from lectures

## Lab 1 - Testing Theory

The structure of the project is the code under test is in [lectures](lectures/testing/theory) and the associated [tests](tests/testing/theory) are in a parallel 'tests' directory

1. Execute test_wraparound_exhaustive.py
2. Run statement coverage on test_wraparound_exhaustive.py
4. Consider the test cases for the mood calculator using EP and BVA.
 * Code these test cases in test_mood_calculator.py
 * Write the implementation of mood_calculator.py
3. Open test_legaldrinking.py. There is a progression in the tests which accompany lectures.
 * Start by executing Test100StatementCoverageTwoBugs.
 * Understand that with 100% statement coverage there were two bugs.
 * We add branch coverage but there is still a bug
 * We then add condition coverage

4. Consider a more complex example of plane_navigation_computer.py. The state space can not be exhausively explored
  * Consider the equivalence partitions and write test cases
  * Write the test cases into test_plane_navigation_computer.py, write an implementation of plane_navigation_computer.py
  * Run the test cases and generate a coverage report

## Lab 2 - TDD
[lecture / code under tests](lectures/testing/tdd) and [tests](tests/testing/tdd)

1. Follow the lecture code for urlvalidator
    * The code accompanies the lectures showing the iterative stages of the TDD process

2. You now have the opportunity to try out TDD in practice. See test_efficient_frontier.py which explains the problem.
There is an empty file in the lecture directory (efficient_frontier.py) for you to complete
* Understand the problem
* Follow the TDD process to write the tests and an implementation of efficient_frontier

## Lab 3 - Mocking
[lecture / code under tests](lectures/testing/mocking) and [tests](tests/testing/mocking)

1. Follow through the auction_bot code
* Run the unit tests test_auction_bot.py until you understand what has been mocked and how the unit tests work

2. Devise your own simple example of a class with an external dependency that you need to mock to be able to test your code.

## Lab 4 - Levels
[lecture / code under tests](lectures/testing/levels) and [tests](tests/testing/levels)

We are now going to stitch together a few of the skills into a small example that also covers testing. In this lab
you will write a very simple store. The store has inventory/stock and a till to keep track of money. I suggest you model your code as

1. Items that are sold. Each item has a SKU, name and price
2. An inventory class whose sole responsibility is keeping track of all the items
3. A till which keeps track of cash. When items are sold cash increases, when refunded the opposite. The till may start the day with cash
4. The store is an object which encapsulates the inventory and till. The API of the store allows people to list inventory and buy. The store needs to manage both changes to the inventory and till
5. Things to consider: it is not possible to buy items if they are not in the inventory

Your task should you choose to accept it

0. Think about the design and requirements. Think about the responsibilities of the inventory vs the till vs the store
1. TDD the development of the inventory
2. TDD the development of the till
3. TDD the development of the store

There should be three tests. Three empty files exist test_inventory.py, test_till.py and test_store.py. Remember, there
are different levels of testing. We will write tests for the inventory and till individualls. Then we assemble this with the store and write
tests for all three objects wired together. Consider which test cases are appropriate for each class/level.

## Lab 5 - Debugging

[lecture / code under tests](lectures/testing/debugging) and [tests](tests/testing/debugging)

In this example we have some code with a bug. We want to be systematic in rectifying. We did cover this example in class 
but I think there is value in running through the workflow yourself and getting familiar with the debugging tools

Remember the systematic process is:
0. Tracking (in our project we will capture bugs in Trello)
1. Reproducing - by forming a hypothesis
2. Automating the test case
3. Finding the infection origin
4. Focus on most likely origin
5. Isolate the infection chain
6. Correct the defect

The bug report from a users is

![Bug](assets/debugging_call_to_action.png?raw=true "Bug!")

1. Run the user service (user_service.py)
2. Install [postman](https://www.getpostman.com/). You will find this tool useful if you produce any REST APIs
3. Explore creating, listing and counting until you replicate the bug. The service allows you to create, list and count 
users using HTTP GET and POST commands 
* Create
![Create](assets/postman_users_create.png?raw=true "Title")
* List
![List](assets/postman_users_list.png?raw=true "Title")
* Count
![Count](assets/postman_users_count.png?raw=true "Title")

4. Form the hypothesis as to the nature of the bug
5. Write a test case which replicates the issue [lecture / code under tests](lectures/testing/debugging/test_user_service.py). 
There is a placeholder test for you
```python
    def test_lab_for_student(self):
        # Exercise to the student
        # Write a test which replicates the bug
        pass
```
Remember you can use the IDE facilities to debug into the code.
6. Find the infection origin
7. Fix
8. Rerun the unit test you write as part of #5
9. Commit into your local fork



