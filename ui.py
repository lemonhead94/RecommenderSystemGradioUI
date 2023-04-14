from typing import List

import gradio as gr


def recommend_exams() -> List[str]:
    return ["Maths", "Physics", "Chemistry"]


with gr.Blocks(title="Recommender System") as demo:
    gr.Interface(
        title="Recommender System",
        fn=recommend_exams,
        inputs=gr.Textbox(
            placeholder="Describe what you are searching for..."
        ),
        outputs="label",
        interpretation="default",
        examples=[
            ["This is an example search query"],
            ["This is another example"],
        ],
    )
demo.launch()
