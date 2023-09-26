# Project Name - Task_2_Quiz_Application
# Developed By - Ajay Thakur (2016kuec2026@iiitkota.ac.in)
# Branch Name - Electronics and Communication Engineering
# Institute Name - Indian Institute of Information Technology Kota (An Institute of National Importance under an Act of Parliament)
# Submitted To -  Code Alpha
# Project Link (GitHub) - https://github.com/ajaythakur3369/CodeAlpha-Password-Generator/blob/main/Task_2_Quiz_Application.py

# Project Summery - There are many things to learn in the world, and quizzes help in testing the understanding of those concepts. The Quiz Application will present 
# questions to users and expect the users to respond accordingly. Think of it as a questionnaire. Using the Quiz Application, it will be possible for special users, 
# called administrators, to create tests, and then regular users can answer the questions and test their understanding.

# Importing necessary modules for performing the Program
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.ttk import Style

# Sample quiz data (questions, choices, and answers)
quiz_data = [ 
    {
        "question": "1. Which of the following is the correct extension of the Python file?",
        "choices": [".python", ".pl", ".py", ".p"],
        "answer": ".py"
    },
    {
        "question": "2. Which keyword is used for function in Python language?",
        "choices": ["Function", "def", "Fun", "Define"],
        "answer": "def"
    },  
    {
        "question": "3. What will be the output of the following Python function? min(max(False, -3, -4), 2, 7)",
        "choices": ["-4", "-3", "2", "False"],
        "answer": "False"
    },
    {
        "question": "4. What keyword would you use to add an alternative condition to an if statement?",
        "choices": ["else if", "elseif", "elif", "None of the above"],
        "answer": "elif"
    }, 
    {
        "question": "5. Which data type is used to store a sequence of characters in Python?",
        "choices": ["int", "float", "string", "boolean"],
        "answer": "string"
    }
]

# Dictionary to store admin credentials
admindict = {
        "admin1" : "12345",
        "admin2" : "67890",
        "admin3" : "45678"
}

# Dictionary to store student credentials
studentdict = {
        "student1" : "12345",
        "student2" : "67890",
        "student2" : "56781"
}

# Create the main root window for the application
root = Tk()
root.geometry('500x400')
root.resizable(False, False)
root.title("Quiz Application")

# Create a label for the Quiz title
Label(root, text = "Quiz", foreground = 'blue', font = ('Georgia', 30, 'bold')).pack(pady = 30)

# Function to create a sign in window
def sign_in_window():
    global username_entry, password_entry, user_type_var
    
    window = Toplevel(root)
    window.geometry('925x500')
    window.title('SignIn')
    window.resizable(False, False)
    frame = Frame(window, width = 350, height = 350)  
    frame.pack(pady = 20) 
    style_ = Style()

    # Configure the font size for the question and choice buttons
    style_.configure("TLabel", font = ("Georgia", 20))
    style_.configure("TButton", font = ("Georgia", 16))
    
    heading = Label(frame, text = 'Sign In', foreground = 'blue', font = ('Georgia', 20, 'bold')) # 57a1f8
    heading.pack(pady = 30)

    username_label = Label(frame, text = "Username:", font = ('Georgia', 10))
    username_label.pack()

    username_entry = Entry(frame, width = 25)
    username_entry.pack()
    Frame(frame, width = 295, height = 2).pack()

    password_label = Label(frame, text = "Password:", font = ('Georgia', 10))
    password_label.pack()

    password_entry = Entry(frame, width = 25, show = "*")
    password_entry.pack()

    Frame(frame, width = 295, height = 2).pack()

    # Check buttons for selection of user type (admin or student)
    user_type_var = StringVar()
    admin_checkbox = Checkbutton(frame, text = "Admin", variable = user_type_var, onvalue = "admin")
    admin_checkbox.pack()
    student_checkbox = Checkbutton(frame, text = "Student", variable = user_type_var, onvalue = "student")
    student_checkbox.pack()

    Button(frame, width = 15, text = 'Sign in', command = validate_credentials).pack(pady = 9)

# Clear the entry fields
def clear_entry():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
   
# Function to validate the credentials of the user and admin
def validate_credentials():
    username = username_entry.get()
    password = password_entry.get()
    
    user_type = user_type_var.get()
    
    if user_type == "admin" and username in admindict and admindict[username] == password:
        open_admin_window()
    elif user_type == "student" and username in studentdict and studentdict[username] == password:
        open_student_window()
    else:
        messagebox.showerror("Error", "Invalid credentials. Please try again.")
    clear_entry()
        
# Admin window
def open_admin_window():
    admin_window = Toplevel(root)
    admin_window.geometry('950x500')
    admin_window.title("Admin Window")
    
    # Function to add a new question
    def add_question():
        new_question = question_entry.get()
        option1 = option1_entry.get()
        option2 = option2_entry.get()
        option3 = option3_entry.get()
        option4 = option4_entry.get()
        correct_answer = correct_answer_entry.get()

        new_question_data = {
            "question": new_question,
            "choices": [option1, option2, option3, option4],
            "answer": correct_answer,
        }

        quiz_data.append(new_question_data)
        listbox.insert(END, new_question)
        clear_fields()

    # Function to delete a question
    def delete_question():
        selected_index = listbox.curselection()
        if selected_index:

            # Converting the tuple result given by cursor selection into an integer
            selected_index = int(selected_index[0])
            
            del quiz_data[selected_index]
            listbox.delete(selected_index)
            clear_fields()
            
    # Function to clear the entry fields
    def clear_fields():
        question_entry.delete(0, END)
        option1_entry.delete(0, END)
        option2_entry.delete(0, END)
        option3_entry.delete(0, END)
        option4_entry.delete(0, END)
        correct_answer_entry.delete(0, END)

    Label(admin_window, text = 'Add a Question:', foreground = 'blue', font = ('Georgia', 20, 'bold')).pack(pady = 10)
    Label(admin_window, text = "Question:", font = ('Georgia', 10)).pack()
    
    # Entry fields for questions, options and answer
    question_entry = Entry(admin_window, width = 50)
    question_entry.pack()

    Label(admin_window, text = "Options:", font = ('Georgia', 10)).pack()
    option1_entry = Entry(admin_window, width = 25)
    option1_entry.pack()
    option2_entry = Entry(admin_window, width = 25)
    option2_entry.pack()
    option3_entry = Entry(admin_window, width = 25)
    option3_entry.pack()
    option4_entry = Entry(admin_window, width = 25)
    option4_entry.pack()

    Label(admin_window, text = "Correct Answer:", font = ('Georgia', 10)).pack()
    correct_answer_entry = Entry(admin_window, width = 25)
    correct_answer_entry.pack()

    # Buttons for adding and deleting the questions
    Button(admin_window, text = "Add Question", command = add_question).pack(pady = 10)
    Label(admin_window, text = 'Delete a Question:', foreground = 'blue', font = ('Georgia', 20, 'bold')).pack(pady = 10)
    Button(admin_window, text = "Delete Selected Question", command = delete_question).pack(pady = 30)

    listbox = Listbox(admin_window, selectmode = SINGLE, width = 50, height = 10)
    listbox.pack()

    for question in quiz_data:
        listbox.insert(END, question["question"])
        
# Student Window
def open_student_window():
    student_window = Toplevel(root)
    student_window.geometry('925x500')
    student_window.resizable(False, False)
    student_window.title("Student Window")
 
    Label(student_window,text = 'Start the Quiz', foreground = 'blue', font = ('Georgia', 20, 'bold')).pack(pady = 30)
    Button(student_window, width = 15, text = 'Start', command = Quiz).pack(pady = 9)
    
# Quiz Logic
def Quiz():
    global score, current_question, quiz_data
    
    # Function to display the current question and choices
    def show_question():

    # Get the current question from the quiz_data list
        question = quiz_data[current_question]
        qs_label.config(text = question["question"])

        # Display the choices on the buttons
        choices = question["choices"]
        for i in range(4):

            # Reset button state
            choice_btns[i].config(text = choices[i], state = "normal") 

        # Clear the feedback label and disable the next button
        feedback_label.config(text = "")
        next_btn.config(state = "disabled")
        
    # Function to check the selected answer and provide feedback
    def check_answer(choice):
        global score, current_question

        # Get the current question from the quiz_data list
        question = quiz_data[current_question]
        selected_choice = choice_btns[choice].cget("text")

        # Check if the selected choice matches the correct answer
        if selected_choice == question["answer"]:
            
            # Update the score and display it   
            score += 1
            score_label.config(text = "Score: {}/{}".format(score, len(quiz_data)))
            feedback_label.config(text = "Correct!", foreground = "green")
        else:
            feedback_label.config(text = "Incorrect!", foreground = "red")

        # Disable all choice buttons and enable the next button
        for button in choice_btns:
            button.config(state = "disabled")
        next_btn.config(state = "normal")

    # Function to move to the next question
    def next_question():
        global current_question
        current_question += 1

        if current_question < len(quiz_data):

            # If there are more questions, show the next question
            show_question()
        else:

            # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
            mainroot.destroy()

    # Create the window
    mainroot = Tk()
    mainroot.title("Quiz App")
    mainroot.geometry("600x500")
    style = Style()

    # Configure the font size for the questions and choice buttons
    style.configure("TLabel", font = ("Georgia", 20))
    style.configure("TButton", font = ("Georgia", 16))

    # Create the question label
    qs_label = Label(mainroot, anchor = "center", wraplength = 500, padding = 10)
    qs_label.pack(pady = 10)

    # Create the choice buttons
    choice_btns = []
    for i in range(4):
        button = Button(mainroot, command = lambda i = i: check_answer(i))
        button.pack(pady = 5)
        choice_btns.append(button)

    # Create the feedback label
    feedback_label = Label(mainroot, anchor = "center", padding = 10)
    feedback_label.pack(pady = 10)

    # Initialize the score
    score = 0

    # Create the score label
    score_label = Label(mainroot, text = "Score: 0/{}".format(len(quiz_data)), anchor = "center", padding = 10)
    score_label.pack(pady = 10)

    # Create the next button
    next_btn = Button(mainroot, text = "Next", command = next_question, state = "disabled")
    next_btn.pack(pady = 10)

    # Initialize the current question index
    current_question = 0

    # Show the first question
    show_question()

    # Start the main event loop
    mainroot.mainloop()
    
# Function to open the Sign In Window
def open_sign_in_window():
    sign_in_window()
  
# Main Sign In Window
sign_in_window_button = Button(root, text = "Proceed to Login", command = open_sign_in_window)
sign_in_window_button.pack(pady = 10)

root.mainloop()