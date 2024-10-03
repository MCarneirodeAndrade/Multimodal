'''
created: 02 March 2024
last update: 
@author: davahm
'''


'''
This script starts the button box and streams its events as MyMarkerStream
'''
#!/usr/bin/env python
#-*- coding: utf-8 -*-

### Loading PACKAGES ###
from psychopy import visual, core, event
import pandas as pd
import random
import csv
from pylsl import StreamInfo, StreamOutlet  
from rusocsci import buttonbox
import os
import json


# Define Variables and print them. 
curfolder = os.getcwd()
print(curfolder)

#Define the markernames for the triggers send from the buttonbox
markernames = ['SUD_0_Start', 'SUD_0_End', 'Speech_Start', 'SUD_1_Start', 'SUD_1_End', 'SUD_2_Start', 'SUD_2_End', 'SUD_3_Start', 'SUD_3_End', 'Speech_End']
print('markernames=', markernames)


###  BUTTON BOX
# initiate button box
bb = buttonbox.Buttonbox()

# initiate clocks
globalClock = core.Clock()

for index, marker in enumerate(markernames):
    print(f"Press button 'A' for {marker}")
    while True:
        # Wait for a single button press
        b = bb.waitButtons()


# wait for a single button press
b = bb.waitButtons()
 
# print the button pressed
print("b: {}".format(b)) 

### SYSTEM SETTINGS ###

# initiate clocks
globalClock = core.Clock()


### LSL STREAM ###

info = StreamInfo('MyMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')
outlet = StreamOutlet(info)

print("now sending markers...")


## Looping trhough each button box
trigger = [],

for x in markernames: 
    trigger = markernames[x],
    print(trigger)
    time = globalClock.getTime()  
    






### SYSTEM SETTINGS ###

# initiate clocks
globalClock = core.Clock()


# wait for the key
# event.waitKeys()
key = []
while key == []: 
    key = bb.getButtons(buttonList='A')
    core.wait(0.01)

# Start the experiment
print(markernames [0]) 
# get the time of the start
start_time = globalClock.getTime() 
outlet.push_sample([markernames[0]])


# wait for the key
# event.waitKeys()
key = []
while key == []: 
    key = bb.getButtons(buttonList='A')
    core.wait(0.01)

print(markernames [1]) 
start_time = globalClock.getTime() 
outlet.push_sample([markernames[1]])


# wait for the key
# event.waitKeys()
key = []
while key == []: 
    key = bb.getButtons(buttonList='A')
    core.wait(0.01)

# send marker
print("practice starts")  
outlet.push_sample([markernames[9]])

# 3 blocks
for block_num, block in enumerate (conditions, start=1):

    # Display block instructions
    block_text = visual.TextStim(win1, 
                                 text=f"This is block {block_num}: {block}", 
                                 height=80, 
                                 color="black",
                                 wrapWidth=1000)
    if block == "gebaren":
        image_stimulus = create_visual(win0, "gebaren")
    elif block == "combinatie":
        image_stimulus = create_visual(win0, "combinatie")
    elif block == "geluiden":
        image_stimulus = create_visual(win0, "geluiden")
    else:
        print("error in generating picture")

    # display
    display_on_windows(win0, block_text, win1, block_text, [image_stimulus], [image_stimulus])

    block_text.draw(win2)
    block_text.draw(win3)
    win2.flip()
    win3.flip()


    # send marker
    print("Practice: new block starts")  
    outlet.push_sample([markernames[1]])

    # get the time of the start
    block_time = globalClock.getTime()

    # wait for the key
    # event.waitKeys()
    key = []
    while key == []: 
        key = bb.getButtons(buttonList='A')
        core.wait(0.01)
    

    # 2 cycles for each participant
    cycle  = 0  # 1 cycle for 1 participant
    while cycle < 2:
        # Present each concept as a stimulus, up to 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  stimuli
        index = 0  # Initialize index
        presented_concepts = 1  # Initialize counter for concepts

        #if the cycle has number 1, use gesture_, vocal_ and multimodal_ lists from participant 1, if 2, use lists from participant 2
        if cycle == 0:
            if block == "gebaren":
                practice_list = pr_ges1
                concept_list = ges1
                instructions_g = create_instr(win0, "gebaren", "instructions_g1")
                instructions_p = create_instr(win0, "gebaren", "instructions_p1")
            elif block == "combinatie":
                practice_list = pr_mult1
                concept_list = mult1
                instructions_g = create_instr(win0, "combinatie", "instructions_g1")
                instructions_p = create_instr(win0, "combinatie", "instructions_p1")
            elif block == "geluiden":
                practice_list = pr_voc1
                concept_list = voc1
                instructions_g = create_instr(win0, "geluiden", "instructions_g1")
                instructions_p = create_instr(win0, "geluiden", "instructions_p1")
            else:
                print("error in generating block instructions and stimuli")
        elif cycle == 1:
            if block == "gebaren":
                practice_list = pr_ges2
                concept_list = ges2
                instructions_g = create_instr(win0, "gebaren", "instructions_g2")
                instructions_p = create_instr(win0, "gebaren", "instructions_p2")
            elif block == "combinatie":
                practice_list = pr_mult2
                concept_list = mult2
                instructions_g = create_instr(win0, "combinatie", "instructions_g2")
                instructions_p = create_instr(win0, "combinatie", "instructions_p2")
            elif block == "geluiden":
                practice_list = pr_voc2
                concept_list = voc2
                instructions_g = create_instr(win0, "geluiden", "instructions_g2")
                instructions_p = create_instr(win0, "geluiden", "instructions_p2")
            else:
                print("error in generating block instructions and stimuli")
        else:
            print("error in generating block instructions and stimuli")


        # update picture 
        image_stimulus.size = (300,300)
        image_stimulus.pos = [0, 0]
        image_stimulus.opacity = 0.2

        # display
        display_on_windows(win0, instructions_g, win1, instructions_p, [image_stimulus], [image_stimulus])

        instructions_g.draw(win2)
        instructions_p.draw(win3)
        win2.flip()
        win3.flip()


        # wait for the key
        # event.waitKeys()
        key = []
        while key == []: 
            key = bb.getButtons(buttonList='A')
            core.wait(0.01)

        ### practice ###
        display_on_windows(win0, practice_text, win1, practice_text, [], [])

        practice_text.draw(win2)
        practice_text.draw(win3)
        win2.flip()
        win3.flip()


        # wait for the key
        # event.waitKeys()
        key = []
        while key == []: 
            key = bb.getButtons(buttonList='A')
            core.wait(0.01)
    

        if block_num == 1:
            # how to signal
            display_on_windows(win0, get_ready, win1, tpose_prompt, [], [])

            get_ready.draw(win2)
            tpose_prompt.draw(win3)
            win2.flip()
            win3.flip()

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)

            # send the marker
            print("tpose_start")  
            outlet.push_sample([markernames[12]])

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)

            # send the marker
            print("tpose_end")  
            outlet.push_sample([markernames[13]])

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)
            # how to signal
            display_on_windows(win0, signal_guesser, win1, signal_text, [], [arrow, marker_demo])

            signal_guesser.draw(win2)
            signal_text.draw(win3)
            win2.flip()
            win3.flip()

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)
        else:
            # how to signal
            display_on_windows(win0, signal_guesser, win1, signal_text, [], [arrow, marker_demo])

            signal_guesser.draw(win2)
            signal_text.draw(win3)
            win2.flip()
            win3.flip()

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)

        # send the marker
        print("practice: trials start")  
        outlet.push_sample([markernames[2]])
        
        while index < len(practice_list) and presented_concepts <= 2:
            concept = practice_list[index]
            practice = 'practice'
            # Display the concept
            text_stimuli.text = concept
            # resize picture
            image_stimulus.size = (150,150)
            image_stimulus.pos = [-250,400]
            image_stimulus.opacity = 0.75
            progress_bar.text = f"Progress: {presented_concepts}/2"
            display_on_windows(win0, get_ready, win1, text_stimuli, [progress_bar], [progress_bar, marker_start, image_stimulus])

            get_ready.draw(win2)
            text_stimuli.draw(win3)
            win2.flip()
            win3.flip()

            # save time of word display
            word_display_time = globalClock.getTime() 
            
            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)
            
            # save time of performance start
            performance_start_time = globalClock.getTime()

            # send marker to 'start' recording
            print("practice: trial started")  
            outlet.push_sample([markernames[10]])

            # Display the concept with marker_recording
            display_on_windows(win0, watch_stimuli, win1, text_stimuli, [progress_bar], [progress_bar, marker_end, image_stimulus])

            watch_stimuli.draw(win2)
            text_stimuli.draw(win3)
            win2.flip()
            win3.flip()

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)

            # save time of performance end
            performance_end_time = globalClock.getTime() 
            # send marker
            print("practice: trial ended")  
            outlet.push_sample([markernames[11]])

            # Display the concept without marker_recording and get input from guesser 
            response = visual.TextBox2(win0, size=(0.8, 0.2), pos=(0, -0.2), font = 'Arial', text='', color='black')
            display_on_windows(win0, prompt_answer, win1, text_stimuli, [progress_bar], [progress_bar, image_stimulus])

            prompt_answer.draw(win2)
            text_stimuli.draw(win3)
            win2.flip()
            win3.flip()

            
            game_point = 0
            response = get_input(response, 'Wat denk je dat je teamgenoot probeerde uit te drukken?', prompt_answer, proceed_enter, win0)
            
            # save time of response
            response_time = globalClock.getTime() 

            # save trial results
            trial_result = {'ID': participant_id_input, 'exp_start': start_time, 'block_start': block_time, 'practice': practice, 'cycle': cycle, 'display_start': word_display_time, 'trial_start': performance_start_time, 'trial_end': performance_end_time, 'RT': response_time, 'word': concept, 'modality': block, 'answer': response, 'points': game_point}
            save_trial_results(trial_result)

            # Add index +1
            presented_concepts += 1
            index += 1
            # index += 1
            print("practice: next word")  
            outlet.push_sample([markernames[6]])
           
            # Clear win0 before presenting the next word
            win1.flip(clearBuffer=True)
            win0.flip(clearBuffer=True)    

        index = 0 # reinitialize index
        presented_concepts = 1 # reinitialize presented concepts
        display_on_windows(win0, start_text, win1, start_text, [], []) 
        
        start_text.draw(win2)
        start_text.draw(win3)
        win2.flip()
        win3.flip()
        
        # wait for the key
        # event.waitKeys()
        key = []
        while key == []: 
            key = bb.getButtons(buttonList='A')
            core.wait(0.01)
            
        while index < len(concept_list) and presented_concepts <= 7:  #set to less presented concepts when debugging
            concept = concept_list[index]
            practice = 'none'
            game_point = 0      # Initialize game points
            # Display the concept
            text_stimuli.text = concept
            # resize it
            image_stimulus.size = (100,100)
            image_stimulus.pos = [-200,400]
            progress_bar.text = f"Progress: {presented_concepts}/7"
            display_on_windows(win0, get_ready, win1, text_stimuli, [progress_bar], [progress_bar, marker_start, image_stimulus])

            get_ready.draw(win2)
            text_stimuli.draw(win3)
            win2.flip()
            win3.flip()

            # save time of word display
            word_display_time = globalClock.getTime() 
            
            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)
        
            # save time of performance start
            performance_start_time = globalClock.getTime()

            # send marker to 'start' recording
            print("trial started")  
            outlet.push_sample([markernames[4]])

            # Display the concept with marker_recording
            display_on_windows(win0, watch_stimuli, win1, text_stimuli, [progress_bar], [progress_bar, marker_end, image_stimulus])

            watch_stimuli.draw(win2)
            text_stimuli.draw(win3)
            win2.flip()
            win3.flip()

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)

            # save time of performance end
            performance_end_time = globalClock.getTime() 
            # send marker
            print("trial ended")  
            outlet.push_sample([markernames[5]])

            # Display the concept without marker_recording and get input from guesser 
            response = visual.TextBox2(win0, size=(0.8, 0.2), pos=(0, -0.2), font = 'Arial', text='', color='black')
            display_on_windows(win0, prompt_answer, win1, text_stimuli, [progress_bar], [progress_bar, image_stimulus])

            prompt_answer.draw(win2)
            text_stimuli.draw(win3)
            win2.flip()
            win3.flip()
            
            response = get_input(response, 'Wat denk je dat je teamgenoot probeerde uit te drukken?', prompt_answer, proceed_enter, win0)
            
            # save time of response
            response_time = globalClock.getTime() 

            # Add game points
            if response == concept:
                game_point = 1
            else:
                game_point = 0

            # save trial results
            trial_result = {'ID': participant_id_input, 'exp_start': start_time, 'block_start': block_time, 'practice': practice, 'cycle': cycle, 'display_start': word_display_time, 'trial_start': performance_start_time, 'trial_end': performance_end_time, 'RT': response_time, 'word': concept, 'modality': block, 'answer': response, 'points': game_point}
            save_trial_results(trial_result)

            presented_concepts += 1
            index += 1
            print("next word")  
            outlet.push_sample([markernames[6]])
           
            # Clear win0 before presenting the next word
            win1.flip(clearBuffer=True)
            win0.flip(clearBuffer=True)

        cycle += 1  
        if cycle == 1 and block_num <= 3:
            # send markers
            print("change of participants")  
            outlet.push_sample([markernames[3]])
            # display
            display_on_windows(win0, new_round, win1, new_round, [], [])

            new_round.draw(win2)
            new_round.draw(win3)
            win2.flip()
            win3.flip()
            

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)
            
        elif cycle == 2 and block_num < 3:
            # display end of block
            display_on_windows(win0, block_end, win1, block_end, [], [])

            block_end.draw(win2)
            block_end.draw(win3)
            win2.flip()
            win3.flip()

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)
            continue
        else:
            # window with end
            display_on_windows(win0, end, win1, end, [], [])

            end.draw(win2)
            end.draw(win3)
            win2.flip()
            win3.flip()

            # wait for the key
            # event.waitKeys()
            key = []
            while key == []: 
                key = bb.getButtons(buttonList='A')
                core.wait(0.01)

# send markers
print("end of experiment")  
outlet.push_sample([markernames[8]])

# close the windows
win0.close()
win1.close()

core.quit()
