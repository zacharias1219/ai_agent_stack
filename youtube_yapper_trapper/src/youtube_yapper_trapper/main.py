#!/usr/bin/env python
from youtube_yapper_trapper.crew import YoutubeYapperTrapperCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    YoutubeYapperTrapperCrew().crew().kickoff(inputs=inputs)