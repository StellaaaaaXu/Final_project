import gradio as gr
import random
def mergesort_main(unsorted_list,direction):
   if len(unsorted_list)<=1:
       return unsorted_list
   mid=len(unsorted_list)//2
   right_half = unsorted_list[mid:]
   left_half= unsorted_list[0:mid]
   sorted_right= mergesort_main(right_half,direction)
   sorted_left= mergesort_main(left_half,direction)
   result=pointer(sorted_right,sorted_left,direction)
   return result

def pointer(sorted_right,sorted_left,direction):
    merged=[]
    pointerA=0
    pointerB=0
    while pointerA<len(sorted_right) and pointerB<len(sorted_left):
      if direction==True:
         if sorted_right[pointerA]<sorted_left[pointerB]:
            merged.append(sorted_right[pointerA])
            pointerA=pointerA+1
         else:
            merged.append(sorted_left[pointerB])
            pointerB=pointerB+1
      else:
         if sorted_right[pointerA]>sorted_left[pointerB]:
            merged.append(sorted_right[pointerA])
            pointerA=pointerA+1
         else:
             merged.append(sorted_left[pointerB])
             pointerB = pointerB + 1
    if pointerA<len(sorted_right):
        merged.extend(sorted_right[pointerA:])
    if pointerB<len(sorted_left):
        merged.extend(sorted_left[pointerB:])
    return merged

def random_list(order):
    arr=random.sample(range(1,100),10)
    if order== "Ascending":
        direction=True
    else:
        direction=False
    result= mergesort_main(arr,direction)
    return str(arr),str(result)

def run_sort(input_text, order):
    try:
        nums = [int(x.strip()) for x in input_text.split(",") if x.strip() != ""]
    except:
        return "Invalid input. Please enter numbers separated by commas.",""
    if order== "Ascending":
        direction=True
    else:
        direction=False
    result= mergesort_main(nums,direction)
    return str(nums),str(result)

ui = gr.Interface(fn=run_sort,
    inputs=[gr.Textbox(label="Enter numbers (comma separated)"),gr.Dropdown(["Ascending", "Descending"], label="Sorting Order")],
    outputs=[gr.Textbox(label="Before Sorting"),gr.Textbox(label="After Sorting")],
    title="Merge Sort (Manual)",
    description="Manual input mode. Scroll down for random mode.")

ui_random = gr.Interface(fn=random_list,
    inputs=[gr.Dropdown(["Ascending", "Descending"], label="Sorting Order")],
    outputs=[gr.Textbox(label="Before Sorting (Random)"),gr.Textbox(label="After Sorting (Random)")],
    title="Merge Sort (Random Generator)")
app = gr.TabbedInterface([ui, ui_random],["Manual Input", "Random Generator"])
if __name__ == "__main__":
    app.launch()


