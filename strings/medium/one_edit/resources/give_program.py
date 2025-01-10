import json

# List of dictionaries to split
test_cases = [{
    "input": {
        "stringOne": "a",
        "stringTwo": "a"
    },
    "expected": True
},

    {
        "input": {
            "stringOne": "aaa",
            "stringTwo": "aaa"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "a",
            "stringTwo": "b"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "ab",
            "stringTwo": "b"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "abc",
            "stringTwo": "b"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "ab",
            "stringTwo": "a"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "b",
            "stringTwo": "ab"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "bb",
            "stringTwo": "a"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "a",
            "stringTwo": "ab"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "bb",
            "stringTwo": "ab"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "ab",
            "stringTwo": "bb"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "helo"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "heo"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "heloo"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "heloos"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "helllo"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "helllos"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "ello"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "llo"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "ellos"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "hello",
            "stringTwo": "elllos"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "helo",
            "stringTwo": "helle"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "abcdefghijklmnopqrstuvwxyz",
            "stringTwo": "abcdefghijklmnopqrstuvwxyz"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "bcdefghijklmnopqrstuvwxyz",
            "stringTwo": "abcdefghijklmnopqrstuvwxyz"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "bcdefgijklmnopqrstuvwxyz",
            "stringTwo": "abcdefghijklmnopqrstuvwxyz"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "bcdefghijklmnopqrstuvwxyz",
            "stringTwo": "acdefghijklmnopqrstuvwxyz"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "bcdefghijklmnopqrstuvwxyz",
            "stringTwo": "abdefghijklmnopqrstuvwxyz"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "bcdefghijklmnopqrstuvwxyz",
            "stringTwo": "abcdefghijklmnopqrstuvwxy"
        },
        "expected": False
    },

    {
        "input": {
            "stringOne": "bcdefghijklmnopqrstuvwxyz",
            "stringTwo": "abcdefghijklmnopqrstuvwxyza"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "abcdefghijklmnopqrstuvwxyz",
            "stringTwo": "abcdefghijklnopqrstuvwxyz"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "abcdefghijklmnopqrstuvwxyz",
            "stringTwo": "abcdefghijklmmnopqrstuvwxyz"
        },
        "expected": True
    },

    {
        "input": {
            "stringOne": "abcdefghijklmnopqrstuvwxyz",
            "stringTwo": "abcdefghijklnnopqrstuvwxyz"
        },
        "expected": False
    }]

# Split test_cases into separate files
for i, testcase in enumerate(test_cases, start=1):
    filename = f"testcase{i}.json"
    with open(filename, 'w') as file:
        json.dump(testcase, file, indent=4)

print("Test cases have been saved as individual JSON files.")