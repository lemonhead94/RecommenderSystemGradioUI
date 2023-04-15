from typing import Dict, List

import gradio as gr


def recommend_by_text(input: str) -> Dict[str, float]:
    return {
        "Recommendation Match 2": 0.7,
        "Recommendation Match 1": 0.2,
        "Recommendation Match 3": 0.1,
    }


def upload_file(files) -> List[str]:
    file_paths = [file.name for file in files]
    return file_paths


def recommend_by_file(input) -> Dict[str, float]:
    return {
        "Recommendation Match 2": 0.7,
        "Recommendation Match 1": 0.2,
        "Recommendation Match 3": 0.1,
    }


with gr.Blocks(
    title="Dev Demo of Recommender System",
) as recommender_ui:
    gr.Markdown(
        """
    # Recommender System
    """
    )
    with gr.Tabs():
        with gr.TabItem("Text-Based Recommender"):
            with gr.Row():
                with gr.Column():
                    input = gr.Textbox(
                        label="Input Box",
                        placeholder="Describe what you are searching for...",
                    )
                    gr.Examples(
                        [
                            ["This an example sentence"],
                            ["This an example sentence 2"],
                        ],
                        inputs=input,
                    )

                with gr.Column():
                    output = gr.Label()

            recommend_btn = gr.Button("Recommend Me Something!")
            recommend_btn.click(
                fn=recommend_by_text,
                inputs=input,
                outputs=output,
                api_name="recommend_by_text",
            )
        with gr.TabItem("File-Based Recommender"):
            with gr.Row():
                with gr.Column():
                    file_output = gr.File()
                    upload_button = gr.UploadButton(
                        "Click to Upload a File",
                        file_types=["image", "video"],
                        file_count="multiple",
                    )
                    upload_button.upload(
                        upload_file, upload_button, file_output
                    )

                with gr.Column():
                    output = gr.Label()

            recommend_btn = gr.Button("Recommend Me Something!")
            recommend_btn.click(
                fn=recommend_by_file,
                inputs=file_output,
                outputs=output,
                api_name="recommend_by_file",
            )

recommender_ui.launch(
    favicon_path="./recommender_ui/favicon.ico",
    server_name="0.0.0.0",
)
