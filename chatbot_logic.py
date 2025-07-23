from nltk.chat.util import Chat, reflections

pairs = [
    # Greetings
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm fine. How can I assist you?"]],
    ["bye|goodbye", ["Goodbye!", "See you later!"]],
    
    # Name / Identity
    ["what is your name?", ["I am your college assistant chatbot."]],
    
    # Department Info
    ["what departments are there?", [
        "Our college offers BSc Computer Science, BCA, BCom, BBA, BA English, and more."
    ]],
    ["do you have bca department?", ["Yes, we have a BCA department."]],
    
    # Timings
    ["what are college timings?", [
        "College runs from 9:00 AM to 1:30 PM for regular classes."
    ]],
    ["is saturday working?", ["No, college is usually closed on Saturdays."]],

    # Fees
    ["what is the fees for bsc cs?", [
        "The approximate annual fee for BSc Computer Science is ₹20,000."
    ]],
    ["when should we pay exam fees?", [
        "Exam fees are usually paid one month before the exams."
    ]],

    # Faculty
    ["who is the hod of cs department?", ["Dr. Ramesh Kumar is the current HOD of CS."]],
    ["how many faculty in bca?", ["There are 5 faculty members in the BCA department."]],

    # Events
    ["when is cultural day?", ["Cultural Day is held in February every year."]],
    ["do we celebrate women's day?", ["Yes, we celebrate Women's Day in March."]],

    # Others
    ["how to contact principal?", ["You can contact the principal through the college office or official email."]],
    ["is hostel facility available?", ["Yes, hostel facility is available for both boys and girls."]],
    ["where is the library?", ["The library is located on the first floor of the main building."]],
]

chatbot = Chat(pairs, reflections)

def get_bot_response(user_input):
    response = chatbot.respond(user_input)
    return response or "Sorry, I didn't understand that."
