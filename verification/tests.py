"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3,4]],
            "answer": [2,3,4,1],
        },
        {
            "input": [[1]],
            "answer": [1],
        },
        {
            "input": [[]],
            "answer": [],
        },
    ],
    "Extra": [
        {
            "input": [[10, 10]],
            "answer": [10, 10],
        },
        {
            "input": [[1,2,2,2]],
            "answer": [2,2,2,1],
        },
        {
            "input": [[100]],
            "answer": [100],
        },
    ]
}
