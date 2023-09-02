import random
import os

# Step 1: Prepare the data
states = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}


# Make sure the directory to store the quiz files exists
if not os.path.exists('quizzes'):
    os.makedirs('quizzes')

for quizNum in range(35):  # Step 2: For each student

    quizFile = open(f'quizzes/capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'quizzes/capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states
    shuffled_states = list(states.keys())
    random.shuffle(shuffled_states)

    # Step 2.1: For each state
    for questionNum, state in enumerate(shuffled_states, 1):

        # Get the right and wrong answers
        correctAnswer = states[state]
        wrongAnswers = list(states.values())
        wrongAnswers.remove(correctAnswer)
        wrongAnswers = random.sample(wrongAnswers, 3)  # Pick 3 random wrong answers
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Step 2.1.1: Write the question and answer options to the quiz file
        quizFile.write(f'{questionNum}. What is the capital of {state}?\n')
        for i, option in enumerate('ABCD'):
            quizFile.write(f'    {option}. {answerOptions[i]}\n')
        quizFile.write('\n')

        # Step 2.1.2: Write the answer to the answer key file
        answerKeyFile.write(f'{questionNum}. {answerOptions.index(correctAnswer) + 1}\n')

    quizFile.close()
    answerKeyFile.close()
