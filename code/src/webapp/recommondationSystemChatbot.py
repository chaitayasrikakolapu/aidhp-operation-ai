import random

responses = {
    "hello": ["Hi, Please provide your CustomerId"],
    "hi": ["Hi, Please provide your CustomerId"],
    "how are you": ["I'm doing great!", "I'm here to assist you."],
    "bye": ["Goodbye!", "Take care!"],
    "CustomerId": ["Do you have investment plans? (yes/no)"],
    
}

userContext = {}
customerID = ''
investmentAmt = 0
tenure = 0
returnsPer = 0

def get_response(user_input):
   
    
    user_input = user_input.lower()
    
    for key in responses.keys():
        if key in user_input:
            userContext['question'] =  responses[key]
            return random.choice(responses[key])
    
    #print('userinput:'+user_input)
    previousQuestion = str(userContext['question'])
    #print('previousQuestion:'+ previousQuestion)

    nextQuestion = "Hi" 
    if 'CustomerId' in previousQuestion:
        customerID=user_input
        nextQuestion = "Do you have investment plans? (yes/no)"
        
    elif previousQuestion == "Do you have investment plans? (yes/no)":
        nextQuestion = "How much you want to invest?"
        
    elif previousQuestion == "How much you want to invest?":
        nextQuestion = "Tenure?"
        investmentAmt=user_input
        
    elif previousQuestion == "Tenure?":
        nextQuestion = "Expected Returns (in percentage)?"
        tenure = user_input
        
    elif previousQuestion == "Expected Returns (in percentage)?":
        returnsPer=user_input
        return "SBI Small CAP"

    print("nextquestion:"+ nextQuestion)
    if nextQuestion == "Hi":
        return "I'm sorry, I didn't understand that."

    else:
        userContext['question']  = nextQuestion
        return nextQuestion
    
    