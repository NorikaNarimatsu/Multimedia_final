import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from pywebio.output import *
from pywebio.input import *
from pywebio.session import *
from pywebio.platform import *
import random 
from dashboard import discussion_dashboard 

# Rest of the code remains the same

def first_page():
    clear()
    # add logo
    put_image("https://github.com/NorikaNarimatsu/Multimedia_final/blob/main/logo.png?raw=true", width = '250px').style( 'display: block; margin-left: auto;  margin-right: auto;  width: 60%;')
    put_markdown('# Welcome to VoiceVista').style( 'text-align: center; margin: auto;  width: 80%; font-size: 40px') 
    # add team introduction
    put_text('In an era where communication is key, the ability to comprehend and analyze group discussions is more crucial than ever. Enter VoiceVista - Illuminating Dialogues in the Multimedia Realm! VoiceVista is a final project for multimedia system cource at Leiden University designed to revolutionize the way we perceive and manage dialogues. At its core, VoiceVista is a multimedia system driven by real-time speech recognition, offering a comprehensive suite of features for enhanced discussion management and insightful analysis.')

    put_markdown('## Team Members:')
    put_text('- Gu Xiaolin & Norika Narimatsu')
    put_text('- Leiden Institute of Advanced Computer Science (LIACS) / Multimedia System Course 2023 Fall Semester') 
             
    # Purpose
    put_markdown('## Purpose:')
    put_text("The purpose of this project is to develop a multimedia system that enhances the management and analysis "
             "of group discussions by providing real-time speech recognition, visualization of discussion dynamics, "
             "participant scoring, and content filtering.")
    
    put_markdown('## Click Here for Dashboard').style('text-align: center;')
    put_buttons(['Dashboard'], onclick=[discussion_dashboard]).style('text-align: center;')
    put_image("https://github.com/NorikaNarimatsu/Multimedia_final/blob/main/team_test.png?raw=true", width='500px').style( 'display: block; margin-left: auto;  margin-right: auto;  width: 60%;')

