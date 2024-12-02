# Test Prep

Consider interview or SAT preps. What we want to know is the optimal time to spend on practicing.

- The test have `X` questions
- The test bank have `Y` questions
    - For initial simplicity, assume each question have an equal chance to be included in the actual test
    - Each question also have an equal score
- The test taker's performance on a given question is relatived to `how much they have practiced` the question, with a diminishing return
    - For example, for a given question, the chance to get the answer correct based on times practiced could be:
        - 0: 25%
        - 1: 75%
        - 2: 90%
        - 3: 95%
        - 4: 98%
        - 5+: 100%
    - In more complicated model, each question can have a fractional score
- People have a limited memory, so if the number of questions prepared exceeded `Z`, there is a chance (increases with `Z`) that previously prepared question is forgot
    - This could also be modeled as a decrease in (effective) times practices

Some other interesting things to consider:
- Opportunity cost
- Transferrable learning
    - That practicing certain questions will lead to not only success in other problems, but also higher speed in solving the familiar problems

## Example

There are 25 high frequency interview questions, each with a 2% chance of being tested on an onsite interview of 5 rounds. There are 250 other questions, each with a 0.2% chance of being tested.

To pass the interview, one need to get 4 out of the 5 questions correct.

The probability of passing an interview based on the times practiced is:
    - 0: 35%
    - 1: 60%
    - 2: 80%
    - 3: 90%
    - 4: 95%
    - 5+: 100%

The constrain is to pass the interview with 90% confidence. What should be the minimal number of practices?

### Strategies

#### 0. No prep

Practices required: 0

Chances of passing: 5.5%

#### 1. Prepare all questions

##### Once

Practices required: 275

Chances of passing: 33.34%

##### Twice

Practices required: 550

Chances of passing: 73~74%

#### 2. Prepare all high frequency questions

See `test_prep/basic.py`.

##### Once

Practices required: 25

Chances of passing: ~15%

##### Twice

Practices required: 50

Chances of passing: 28-29%

##### Four Times

Practices required: 100

Chances of passing: 41~42%

#### TODO - ?