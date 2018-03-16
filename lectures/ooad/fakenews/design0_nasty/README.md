## Object Oriented Analysis

What I don't like about this code

1. It is hard to test the scoring logic outside of flask
2. It is hard to test individual scoring logic (whitelist, content, domain) independent of each other
3. We do not associate data (whitelist and content keywords) with the function (the former is at the top, the latter is at the bottom)
4. There is a growing 'blob' of code within the handler. Right now it is almost readable but wont become readable if I add more scorers or make any one of them more complex
5. Not super easy to add a new scorer
6. Not super easy to change the weighting of different scorers
7. The webservice just knows too much. All it needs to know is there is something which scores a domain. We do not need to expose the messiness

Hmmmm!!!!
