# Merge Sort Project
## Demo
### Testing screenshot
- manual dsecending test
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/4f495527-ef63-49e6-a0ff-20a8b4bea6b0" />
- manual ascending test
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/7824c050-f42c-4c45-8ab8-686dad7bdabb" />
- random generated ascending test
<img width="2940" height="1910" alt="image" src="https://github.com/user-attachments/assets/65bbd722-bcb8-4582-a0a1-80a18c86d3ea" />
- random generated descending test
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/46fd81bc-ffa7-41e1-b324-ba38e6d590c6" />
- exception catch test
<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/4eb22c25-b540-4ce5-b125-c11add282b10" />

## Problem Breakdown & Computational Thinking
### Decomposition
- I first break the problem into two main parts: splitting the list and merging it back.
- The original list is divided into two halves until each sublist has one element.
- Each half is sorted recursively using the same merge sort function.
- Two sorted sublists are then merged into one using two pointers that move through the lists.
-A `direction` parameter is used to decide whether the merged result should be in ascending or descending order.
### Pattern recognition
- I noticed that the same process repeats at every level of the recursion: split the list, sort each half, and merge them.
- During merging, the same pattern appears: compare the current elements of the two sublists and move the pointer forward on the side that was chosen.
- This repeated pattern makes it clear that recursion is a good fit for implementing merge sort.
### Abstraction
- The user dosent need to know how the program (recursion and pointers) works internally.
- The program hides the splitting and merging, only show off the inputs and outputs.
- All low-level details, such as list indices, pointer movement, and recursive calls, are handled inside the functions.
### Algorithm Design
- Input a unsorted list and a direction parameter(boolean)
- Keep splitting the list into tow halfs unil they each sublists has length 1 or 2.
- Every sublist uses the same merge function to sort
- Uses pointers to compare the elements in two halve lists and put the suitable elements into a new list.
- Pointers will decide sort it in ascending or descending according to the direction parameter.
## Steps to run
### No Hugging face version:
- Make sure Python 3 is installed on your computer.
- Download GitHub repository to your local machine.
- Open the prpject folder in your pycharm.
- Make sure gradio is installed already.
- If you didnt installed gradio: open your terminal and input pip install --upgrade gradio
- Run the program
- Open the local URL shown in the terminal
- You can choose manual input a list you like, and choose order, then will shown the list before sorted and after sorted. You also can choose random generated a list.
### Huggingface version:
- Open the hugging face link in the browser
- In "App" you can use the program as I mentioned before
- In "Files" you will see all files that app included.
## Hugging face link
- https://huggingface.co/spaces/Stellaaaaaaaaaaa/Final_project/tree/main
## Author and Acknowledgment
- Author: XU,Anhang
- Course: CISC121
- ChatGPT was used for debugging support.



