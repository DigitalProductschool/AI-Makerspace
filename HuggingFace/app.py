import gradio as gr
title = "Classify text according to emotion"
description = "Emotion text classification via bert-base finetuned by bhadresh-savani"
examples = [
    ["Remember before Twitter when you took a photo of food, got the film developed, then drove around showing everyone the pic? No? Me neither."],
    ['''"We are all here because we're committed to the biggest question of all: What's out there?" Take your first steps toward answering that question by watching our Gameplay Reveal from the #XboxBethesda Showcase. '''],
    ["A STUNNER IN KNOXVILLE! 😱 Notre Dame takes down No. 1 Tennessee for its first trip to Omaha in 20 years‼️"],
    ["you and I best moment is yet to come 💜 #BTS9thAnniversary"]
]

interface = gr.Interface.load("huggingface/bhadresh-savani/bert-base-go-emotion",
            title=title,
            description=descrition,
            examples = examples
)

interface.launch(enable_queue=True)
