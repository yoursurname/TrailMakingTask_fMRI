#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on mars 01, 2023, at 15:40
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'pyo'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'TMT_fmri'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\HP\\Documents\\My Experiments\\7T\\7T060\\TrailMakingTask_fMRI\\TMT_fmri\\TMT_fmri_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruktioner_TMT"
Instruktioner_TMTClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='Instructions_TMT_shorter.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "Wait_fMRI"
Wait_fMRIClock = core.Clock()
key_resp_7 = keyboard.Keyboard()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "TMTA_info"
TMTA_infoClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Numerisk ordning.\n\n(1-2-3-4...)',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cirkel = visual.TextStim(win=win, name='cirkel',
    text='Cirkelform',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.60, 0.78),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "End_TMT"
End_TMTClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "utspritt"
utsprittClock = core.Clock()
utspritt_txt = visual.TextStim(win=win, name='utspritt_txt',
    text='Utspridda ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.60, 0.78),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "End_TMT"
End_TMTClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "cirkel_text"
cirkel_textClock = core.Clock()
cirkel_2 = visual.TextStim(win=win, name='cirkel_2',
    text='Cirkelform\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.60, 0.78),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "End_TMT"
End_TMTClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "TMTB_info"
TMTB_infoClock = core.Clock()
Info2 = visual.TextStim(win=win, name='Info2',
    text='Växla mellan numerisk och alfabetisk ordning.\n\n(1-A-2-B-3...)',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.60, 0.78),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "End_TMT"
End_TMTClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "TMTA_info"
TMTA_infoClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Numerisk ordning.\n\n(1-2-3-4...)',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cirkel = visual.TextStim(win=win, name='cirkel',
    text='Cirkelform',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.60, 0.78),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "End_TMT"
End_TMTClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "utspritt"
utsprittClock = core.Clock()
utspritt_txt = visual.TextStim(win=win, name='utspritt_txt',
    text='Utspridda ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.60, 0.78),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "End_TMT"
End_TMTClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "cirkel_text"
cirkel_textClock = core.Clock()
cirkel_2 = visual.TextStim(win=win, name='cirkel_2',
    text='Cirkelform\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.60, 0.78),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "End_TMT"
End_TMTClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "TMTB_info"
TMTB_infoClock = core.Clock()
Info2 = visual.TextStim(win=win, name='Info2',
    text='Växla mellan numerisk och alfabetisk ordning.\n\n(1-A-2-B-3...)',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.60, 0.78),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "End_TMT"
End_TMTClock = core.Clock()
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Klar!\n\nBra jobbat, du har slutfört experimentet. \n\nLigg still och invänta instruktioner.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruktioner_TMT"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Instruktioner_TMTComponents = [image_2, key_resp_6]
for thisComponent in Instruktioner_TMTComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruktioner_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruktioner_TMT"-------
while continueRoutine:
    # get current time
    t = Instruktioner_TMTClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruktioner_TMTClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=None, waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruktioner_TMTComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruktioner_TMT"-------
for thisComponent in Instruktioner_TMTComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruktioner_TMT" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Wait_fMRI"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
Wait_fMRIComponents = [key_resp_7, polygon_2]
for thisComponent in Wait_fMRIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Wait_fMRIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Wait_fMRI"-------
while continueRoutine:
    # get current time
    t = Wait_fMRIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Wait_fMRIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    if (key_resp_7.keys) == 's':
        core.wait(8)
        continueRoutine = False
            
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Wait_fMRIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wait_fMRI"-------
for thisComponent in Wait_fMRIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
Time_Since_Run = core.MonotonicClock()
globalClock = core.Clock()
# the Routine "Wait_fMRI" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TMTA_info"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
TMTA_infoComponents = [text_2, cirkel]
for thisComponent in TMTA_infoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TMTA_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TMTA_info"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = TMTA_infoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TMTA_infoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 5.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *cirkel* updates
    if cirkel.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        # keep track of start time/frame for later
        cirkel.frameNStart = frameN  # exact frame index
        cirkel.tStart = t  # local t and not account for scr refresh
        cirkel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cirkel, 'tStartRefresh')  # time at next scr refresh
        cirkel.setAutoDraw(True)
    if cirkel.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cirkel.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            cirkel.tStop = t  # not accounting for scr refresh
            cirkel.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cirkel, 'tStopRefresh')  # time at next scr refresh
            cirkel.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TMTA_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TMTA_info"-------
for thisComponent in TMTA_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
startTime = globalClock.getTime()

cross_duration_mean = 4
thisExp.addData('cirkel.started', cirkel.tStartRefresh)
thisExp.addData('cirkel.stopped', cirkel.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Blocks_Control1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMT_conditions.xlsx', selection='0:4'),
    seed=None, name='Blocks_Control1')
thisExp.addLoop(Blocks_Control1)  # add the loop to the experiment
thisBlocks_Control1 = Blocks_Control1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_Control1.rgb)
if thisBlocks_Control1 != None:
    for paramName in thisBlocks_Control1:
        exec('{} = thisBlocks_Control1[paramName]'.format(paramName))

for thisBlocks_Control1 in Blocks_Control1:
    currentLoop = Blocks_Control1
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_Control1.rgb)
    if thisBlocks_Control1 != None:
        for paramName in thisBlocks_Control1:
            exec('{} = thisBlocks_Control1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_Control1 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMT_trials.xlsx', selection=Condition_rows),
        seed=None, name='trials_Control1')
    thisExp.addLoop(trials_Control1)  # add the loop to the experiment
    thisTrials_Control1 = trials_Control1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Control1.rgb)
    if thisTrials_Control1 != None:
        for paramName in thisTrials_Control1:
            exec('{} = thisTrials_Control1[paramName]'.format(paramName))
    
    for thisTrials_Control1 in trials_Control1:
        currentLoop = trials_Control1
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Control1.rgb)
        if thisTrials_Control1 != None:
            for paramName in thisTrials_Control1:
                exec('{} = thisTrials_Control1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        
        #Clear keyes from last trial to affect this trial
        key_resp_2.clearEvents()
        
        # keep track of which components have finished
        trialComponents = [Stim, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            if Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                Stim.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(Correct)) or (key_resp_2.keys == Correct):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 45:
                if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                    Blocks_Control1.finished = True
                    continueRoutine = False
                elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                    Blocks_Control2.finished = True
                    continueRoutine = False
                elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                    Blocks_Control3.finished = True
                    continueRoutine = False
                elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                    Blocks_Control4.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_A' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                    Blocks_TMTA1.finished = True
                    continueRoutine = False
                elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                    Blocks_TMTA2.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_B' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'B1' or 'B2' or 'B3':
                    Blocks_TMTB1.finished = True
                    continueRoutine = False
                elif Block_paper == 'B4' or 'B5' or 'B6':
                    Blocks_TMTB2.finished = True
                    continueRoutine = False
                    
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_Control1.addData('Stim.started', Stim.tStartRefresh)
        trials_Control1.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_Control1 (TrialHandler)
        trials_Control1.addData('key_resp_2.keys',key_resp_2.keys)
        trials_Control1.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_Control1.addData('key_resp_2.rt', key_resp_2.rt)
        trials_Control1.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_Control1.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        if key_resp_2.keys is not None:
            attempts = len(key_resp_2.keys)    
            currentLoop.addData('Attempts', attempts)
        
        print(f"pressed: {key_resp_2.keys}")
        print(f"corrcet: {Correct}")
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_Control1'
    
    # get names of stimulus parameters
    if trials_Control1.trialList in ([], [None], None):
        params = []
    else:
        params = trials_Control1.trialList[0].keys()
    # save data for this loop
    trials_Control1.saveAsExcel(filename + '.xlsx', sheetName='trials_Control1',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "End_TMT"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    End_TMTComponents = [polygon_4]
    for thisComponent in End_TMTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_TMT"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_TMTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_TMTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 47.5:
            if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                Blocks_Control1.finished = True
                continueRoutine = False
            elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                Blocks_Control2.finished = True
                continueRoutine = False
            elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                Blocks_Control3.finished = True
                continueRoutine = False
            elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                Blocks_Control4.finished = True
                continueRoutine = False
        
        if Version == 'TMT_A' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                Blocks_TMTA1.finished = True
                continueRoutine = False
            elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                Blocks_TMTA2.finished = True
                continueRoutine = False
        
        if Version == 'TMT_B' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'B1' or 'B2' or 'B3':
                Blocks_TMTB1.finished = True
                continueRoutine = False
            elif Block_paper == 'B4' or 'B5' or 'B6':
                Blocks_TMTB2.finished = True
                continueRoutine = False
        
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_TMTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_TMT"-------
    for thisComponent in End_TMTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_Control1'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
# update component parameters for each repeat
cross_duration = normal(cross_duration_mean,2.2)

if cross_duration > 8:
    cross_duration = 8
if cross_duration < 2:
    cross_duration = 2
  
print(f"cross duration: {cross_duration}")
# keep track of which components have finished
FixCrossComponents = [polygon]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 50:
        continueRoutine = False
    elif Version == 'TMT_A' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
    elif Version == 'TMT_B' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startTime = globalClock.getTime()
# the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "utspritt"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
utsprittComponents = [utspritt_txt]
for thisComponent in utsprittComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
utsprittClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "utspritt"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = utsprittClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=utsprittClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *utspritt_txt* updates
    if utspritt_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        utspritt_txt.frameNStart = frameN  # exact frame index
        utspritt_txt.tStart = t  # local t and not account for scr refresh
        utspritt_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(utspritt_txt, 'tStartRefresh')  # time at next scr refresh
        utspritt_txt.setAutoDraw(True)
    if utspritt_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > utspritt_txt.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            utspritt_txt.tStop = t  # not accounting for scr refresh
            utspritt_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(utspritt_txt, 'tStopRefresh')  # time at next scr refresh
            utspritt_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in utsprittComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "utspritt"-------
for thisComponent in utsprittComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('utspritt_txt.started', utspritt_txt.tStartRefresh)
thisExp.addData('utspritt_txt.stopped', utspritt_txt.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Blocks_TMTA1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMT_conditions.xlsx', selection='4:8'),
    seed=None, name='Blocks_TMTA1')
thisExp.addLoop(Blocks_TMTA1)  # add the loop to the experiment
thisBlocks_TMTA1 = Blocks_TMTA1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTA1.rgb)
if thisBlocks_TMTA1 != None:
    for paramName in thisBlocks_TMTA1:
        exec('{} = thisBlocks_TMTA1[paramName]'.format(paramName))

for thisBlocks_TMTA1 in Blocks_TMTA1:
    currentLoop = Blocks_TMTA1
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTA1.rgb)
    if thisBlocks_TMTA1 != None:
        for paramName in thisBlocks_TMTA1:
            exec('{} = thisBlocks_TMTA1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_TMTA1 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMT_trials.xlsx', selection=Condition_rows),
        seed=None, name='trials_TMTA1')
    thisExp.addLoop(trials_TMTA1)  # add the loop to the experiment
    thisTrials_TMTA1 = trials_TMTA1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTA1.rgb)
    if thisTrials_TMTA1 != None:
        for paramName in thisTrials_TMTA1:
            exec('{} = thisTrials_TMTA1[paramName]'.format(paramName))
    
    for thisTrials_TMTA1 in trials_TMTA1:
        currentLoop = trials_TMTA1
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTA1.rgb)
        if thisTrials_TMTA1 != None:
            for paramName in thisTrials_TMTA1:
                exec('{} = thisTrials_TMTA1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        
        #Clear keyes from last trial to affect this trial
        key_resp_2.clearEvents()
        
        # keep track of which components have finished
        trialComponents = [Stim, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            if Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                Stim.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(Correct)) or (key_resp_2.keys == Correct):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 45:
                if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                    Blocks_Control1.finished = True
                    continueRoutine = False
                elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                    Blocks_Control2.finished = True
                    continueRoutine = False
                elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                    Blocks_Control3.finished = True
                    continueRoutine = False
                elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                    Blocks_Control4.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_A' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                    Blocks_TMTA1.finished = True
                    continueRoutine = False
                elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                    Blocks_TMTA2.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_B' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'B1' or 'B2' or 'B3':
                    Blocks_TMTB1.finished = True
                    continueRoutine = False
                elif Block_paper == 'B4' or 'B5' or 'B6':
                    Blocks_TMTB2.finished = True
                    continueRoutine = False
                    
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_TMTA1.addData('Stim.started', Stim.tStartRefresh)
        trials_TMTA1.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_TMTA1 (TrialHandler)
        trials_TMTA1.addData('key_resp_2.keys',key_resp_2.keys)
        trials_TMTA1.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_TMTA1.addData('key_resp_2.rt', key_resp_2.rt)
        trials_TMTA1.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_TMTA1.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        if key_resp_2.keys is not None:
            attempts = len(key_resp_2.keys)    
            currentLoop.addData('Attempts', attempts)
        
        print(f"pressed: {key_resp_2.keys}")
        print(f"corrcet: {Correct}")
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_TMTA1'
    
    # get names of stimulus parameters
    if trials_TMTA1.trialList in ([], [None], None):
        params = []
    else:
        params = trials_TMTA1.trialList[0].keys()
    # save data for this loop
    trials_TMTA1.saveAsExcel(filename + '.xlsx', sheetName='trials_TMTA1',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "End_TMT"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    End_TMTComponents = [polygon_4]
    for thisComponent in End_TMTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_TMT"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_TMTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_TMTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 47.5:
            if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                Blocks_Control1.finished = True
                continueRoutine = False
            elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                Blocks_Control2.finished = True
                continueRoutine = False
            elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                Blocks_Control3.finished = True
                continueRoutine = False
            elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                Blocks_Control4.finished = True
                continueRoutine = False
        
        if Version == 'TMT_A' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                Blocks_TMTA1.finished = True
                continueRoutine = False
            elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                Blocks_TMTA2.finished = True
                continueRoutine = False
        
        if Version == 'TMT_B' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'B1' or 'B2' or 'B3':
                Blocks_TMTB1.finished = True
                continueRoutine = False
            elif Block_paper == 'B4' or 'B5' or 'B6':
                Blocks_TMTB2.finished = True
                continueRoutine = False
        
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_TMTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_TMT"-------
    for thisComponent in End_TMTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_TMTA1'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
# update component parameters for each repeat
cross_duration = normal(cross_duration_mean,2.2)

if cross_duration > 8:
    cross_duration = 8
if cross_duration < 2:
    cross_duration = 2
  
print(f"cross duration: {cross_duration}")
# keep track of which components have finished
FixCrossComponents = [polygon]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 50:
        continueRoutine = False
    elif Version == 'TMT_A' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
    elif Version == 'TMT_B' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startTime = globalClock.getTime()
# the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "cirkel_text"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
cirkel_textComponents = [cirkel_2]
for thisComponent in cirkel_textComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
cirkel_textClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "cirkel_text"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cirkel_textClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=cirkel_textClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cirkel_2* updates
    if cirkel_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cirkel_2.frameNStart = frameN  # exact frame index
        cirkel_2.tStart = t  # local t and not account for scr refresh
        cirkel_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cirkel_2, 'tStartRefresh')  # time at next scr refresh
        cirkel_2.setAutoDraw(True)
    if cirkel_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cirkel_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            cirkel_2.tStop = t  # not accounting for scr refresh
            cirkel_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cirkel_2, 'tStopRefresh')  # time at next scr refresh
            cirkel_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cirkel_textComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "cirkel_text"-------
for thisComponent in cirkel_textComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cirkel_2.started', cirkel_2.tStartRefresh)
thisExp.addData('cirkel_2.stopped', cirkel_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Blocks_Control2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMT_conditions.xlsx', selection='8:12'),
    seed=None, name='Blocks_Control2')
thisExp.addLoop(Blocks_Control2)  # add the loop to the experiment
thisBlocks_Control2 = Blocks_Control2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_Control2.rgb)
if thisBlocks_Control2 != None:
    for paramName in thisBlocks_Control2:
        exec('{} = thisBlocks_Control2[paramName]'.format(paramName))

for thisBlocks_Control2 in Blocks_Control2:
    currentLoop = Blocks_Control2
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_Control2.rgb)
    if thisBlocks_Control2 != None:
        for paramName in thisBlocks_Control2:
            exec('{} = thisBlocks_Control2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_Control2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMT_trials.xlsx', selection=Condition_rows),
        seed=None, name='trials_Control2')
    thisExp.addLoop(trials_Control2)  # add the loop to the experiment
    thisTrials_Control2 = trials_Control2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Control2.rgb)
    if thisTrials_Control2 != None:
        for paramName in thisTrials_Control2:
            exec('{} = thisTrials_Control2[paramName]'.format(paramName))
    
    for thisTrials_Control2 in trials_Control2:
        currentLoop = trials_Control2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Control2.rgb)
        if thisTrials_Control2 != None:
            for paramName in thisTrials_Control2:
                exec('{} = thisTrials_Control2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        
        #Clear keyes from last trial to affect this trial
        key_resp_2.clearEvents()
        
        # keep track of which components have finished
        trialComponents = [Stim, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            if Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                Stim.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(Correct)) or (key_resp_2.keys == Correct):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 45:
                if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                    Blocks_Control1.finished = True
                    continueRoutine = False
                elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                    Blocks_Control2.finished = True
                    continueRoutine = False
                elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                    Blocks_Control3.finished = True
                    continueRoutine = False
                elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                    Blocks_Control4.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_A' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                    Blocks_TMTA1.finished = True
                    continueRoutine = False
                elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                    Blocks_TMTA2.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_B' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'B1' or 'B2' or 'B3':
                    Blocks_TMTB1.finished = True
                    continueRoutine = False
                elif Block_paper == 'B4' or 'B5' or 'B6':
                    Blocks_TMTB2.finished = True
                    continueRoutine = False
                    
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_Control2.addData('Stim.started', Stim.tStartRefresh)
        trials_Control2.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_Control2 (TrialHandler)
        trials_Control2.addData('key_resp_2.keys',key_resp_2.keys)
        trials_Control2.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_Control2.addData('key_resp_2.rt', key_resp_2.rt)
        trials_Control2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_Control2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        if key_resp_2.keys is not None:
            attempts = len(key_resp_2.keys)    
            currentLoop.addData('Attempts', attempts)
        
        print(f"pressed: {key_resp_2.keys}")
        print(f"corrcet: {Correct}")
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_Control2'
    
    # get names of stimulus parameters
    if trials_Control2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_Control2.trialList[0].keys()
    # save data for this loop
    trials_Control2.saveAsExcel(filename + '.xlsx', sheetName='trials_Control2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "End_TMT"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    End_TMTComponents = [polygon_4]
    for thisComponent in End_TMTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_TMT"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_TMTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_TMTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 47.5:
            if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                Blocks_Control1.finished = True
                continueRoutine = False
            elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                Blocks_Control2.finished = True
                continueRoutine = False
            elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                Blocks_Control3.finished = True
                continueRoutine = False
            elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                Blocks_Control4.finished = True
                continueRoutine = False
        
        if Version == 'TMT_A' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                Blocks_TMTA1.finished = True
                continueRoutine = False
            elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                Blocks_TMTA2.finished = True
                continueRoutine = False
        
        if Version == 'TMT_B' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'B1' or 'B2' or 'B3':
                Blocks_TMTB1.finished = True
                continueRoutine = False
            elif Block_paper == 'B4' or 'B5' or 'B6':
                Blocks_TMTB2.finished = True
                continueRoutine = False
        
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_TMTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_TMT"-------
    for thisComponent in End_TMTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_Control2'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
# update component parameters for each repeat
cross_duration = normal(cross_duration_mean,2.2)

if cross_duration > 8:
    cross_duration = 8
if cross_duration < 2:
    cross_duration = 2
  
print(f"cross duration: {cross_duration}")
# keep track of which components have finished
FixCrossComponents = [polygon]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 50:
        continueRoutine = False
    elif Version == 'TMT_A' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
    elif Version == 'TMT_B' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startTime = globalClock.getTime()
# the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TMTB_info"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
TMTB_infoComponents = [Info2]
for thisComponent in TMTB_infoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TMTB_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TMTB_info"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = TMTB_infoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TMTB_infoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Info2* updates
    if Info2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Info2.frameNStart = frameN  # exact frame index
        Info2.tStart = t  # local t and not account for scr refresh
        Info2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Info2, 'tStartRefresh')  # time at next scr refresh
        Info2.setAutoDraw(True)
    if Info2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Info2.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            Info2.tStop = t  # not accounting for scr refresh
            Info2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Info2, 'tStopRefresh')  # time at next scr refresh
            Info2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TMTB_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TMTB_info"-------
for thisComponent in TMTB_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Info2.started', Info2.tStartRefresh)
thisExp.addData('Info2.stopped', Info2.tStopRefresh)
startTime = globalClock.getTime()

# set up handler to look after randomisation of conditions etc
Blocks_TMTB1 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMT_conditions.xlsx', selection='12:15'),
    seed=None, name='Blocks_TMTB1')
thisExp.addLoop(Blocks_TMTB1)  # add the loop to the experiment
thisBlocks_TMTB1 = Blocks_TMTB1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTB1.rgb)
if thisBlocks_TMTB1 != None:
    for paramName in thisBlocks_TMTB1:
        exec('{} = thisBlocks_TMTB1[paramName]'.format(paramName))

for thisBlocks_TMTB1 in Blocks_TMTB1:
    currentLoop = Blocks_TMTB1
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTB1.rgb)
    if thisBlocks_TMTB1 != None:
        for paramName in thisBlocks_TMTB1:
            exec('{} = thisBlocks_TMTB1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_TMTB1 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMT_trials.xlsx', selection=Condition_rows),
        seed=None, name='trials_TMTB1')
    thisExp.addLoop(trials_TMTB1)  # add the loop to the experiment
    thisTrials_TMTB1 = trials_TMTB1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTB1.rgb)
    if thisTrials_TMTB1 != None:
        for paramName in thisTrials_TMTB1:
            exec('{} = thisTrials_TMTB1[paramName]'.format(paramName))
    
    for thisTrials_TMTB1 in trials_TMTB1:
        currentLoop = trials_TMTB1
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTB1.rgb)
        if thisTrials_TMTB1 != None:
            for paramName in thisTrials_TMTB1:
                exec('{} = thisTrials_TMTB1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        
        #Clear keyes from last trial to affect this trial
        key_resp_2.clearEvents()
        
        # keep track of which components have finished
        trialComponents = [Stim, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            if Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                Stim.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(Correct)) or (key_resp_2.keys == Correct):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 45:
                if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                    Blocks_Control1.finished = True
                    continueRoutine = False
                elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                    Blocks_Control2.finished = True
                    continueRoutine = False
                elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                    Blocks_Control3.finished = True
                    continueRoutine = False
                elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                    Blocks_Control4.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_A' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                    Blocks_TMTA1.finished = True
                    continueRoutine = False
                elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                    Blocks_TMTA2.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_B' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'B1' or 'B2' or 'B3':
                    Blocks_TMTB1.finished = True
                    continueRoutine = False
                elif Block_paper == 'B4' or 'B5' or 'B6':
                    Blocks_TMTB2.finished = True
                    continueRoutine = False
                    
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_TMTB1.addData('Stim.started', Stim.tStartRefresh)
        trials_TMTB1.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_TMTB1 (TrialHandler)
        trials_TMTB1.addData('key_resp_2.keys',key_resp_2.keys)
        trials_TMTB1.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_TMTB1.addData('key_resp_2.rt', key_resp_2.rt)
        trials_TMTB1.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_TMTB1.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        if key_resp_2.keys is not None:
            attempts = len(key_resp_2.keys)    
            currentLoop.addData('Attempts', attempts)
        
        print(f"pressed: {key_resp_2.keys}")
        print(f"corrcet: {Correct}")
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_TMTB1'
    
    # get names of stimulus parameters
    if trials_TMTB1.trialList in ([], [None], None):
        params = []
    else:
        params = trials_TMTB1.trialList[0].keys()
    # save data for this loop
    trials_TMTB1.saveAsExcel(filename + '.xlsx', sheetName='trials_TMTB1',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "End_TMT"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    End_TMTComponents = [polygon_4]
    for thisComponent in End_TMTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_TMT"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_TMTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_TMTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 47.5:
            if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                Blocks_Control1.finished = True
                continueRoutine = False
            elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                Blocks_Control2.finished = True
                continueRoutine = False
            elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                Blocks_Control3.finished = True
                continueRoutine = False
            elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                Blocks_Control4.finished = True
                continueRoutine = False
        
        if Version == 'TMT_A' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                Blocks_TMTA1.finished = True
                continueRoutine = False
            elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                Blocks_TMTA2.finished = True
                continueRoutine = False
        
        if Version == 'TMT_B' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'B1' or 'B2' or 'B3':
                Blocks_TMTB1.finished = True
                continueRoutine = False
            elif Block_paper == 'B4' or 'B5' or 'B6':
                Blocks_TMTB2.finished = True
                continueRoutine = False
        
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_TMTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_TMT"-------
    for thisComponent in End_TMTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_TMTB1'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
# update component parameters for each repeat
cross_duration = normal(cross_duration_mean,2.2)

if cross_duration > 8:
    cross_duration = 8
if cross_duration < 2:
    cross_duration = 2
  
print(f"cross duration: {cross_duration}")
# keep track of which components have finished
FixCrossComponents = [polygon]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 50:
        continueRoutine = False
    elif Version == 'TMT_A' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
    elif Version == 'TMT_B' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startTime = globalClock.getTime()
# the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TMTA_info"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
TMTA_infoComponents = [text_2, cirkel]
for thisComponent in TMTA_infoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TMTA_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TMTA_info"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = TMTA_infoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TMTA_infoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 5.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *cirkel* updates
    if cirkel.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        # keep track of start time/frame for later
        cirkel.frameNStart = frameN  # exact frame index
        cirkel.tStart = t  # local t and not account for scr refresh
        cirkel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cirkel, 'tStartRefresh')  # time at next scr refresh
        cirkel.setAutoDraw(True)
    if cirkel.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cirkel.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            cirkel.tStop = t  # not accounting for scr refresh
            cirkel.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cirkel, 'tStopRefresh')  # time at next scr refresh
            cirkel.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TMTA_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TMTA_info"-------
for thisComponent in TMTA_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
startTime = globalClock.getTime()

cross_duration_mean = 4
thisExp.addData('cirkel.started', cirkel.tStartRefresh)
thisExp.addData('cirkel.stopped', cirkel.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Blocks_Control3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMT_conditions.xlsx', selection='15:19'),
    seed=None, name='Blocks_Control3')
thisExp.addLoop(Blocks_Control3)  # add the loop to the experiment
thisBlocks_Control3 = Blocks_Control3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_Control3.rgb)
if thisBlocks_Control3 != None:
    for paramName in thisBlocks_Control3:
        exec('{} = thisBlocks_Control3[paramName]'.format(paramName))

for thisBlocks_Control3 in Blocks_Control3:
    currentLoop = Blocks_Control3
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_Control3.rgb)
    if thisBlocks_Control3 != None:
        for paramName in thisBlocks_Control3:
            exec('{} = thisBlocks_Control3[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_Control3 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMT_trials.xlsx', selection=Condition_rows),
        seed=None, name='trials_Control3')
    thisExp.addLoop(trials_Control3)  # add the loop to the experiment
    thisTrials_Control3 = trials_Control3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Control3.rgb)
    if thisTrials_Control3 != None:
        for paramName in thisTrials_Control3:
            exec('{} = thisTrials_Control3[paramName]'.format(paramName))
    
    for thisTrials_Control3 in trials_Control3:
        currentLoop = trials_Control3
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Control3.rgb)
        if thisTrials_Control3 != None:
            for paramName in thisTrials_Control3:
                exec('{} = thisTrials_Control3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        
        #Clear keyes from last trial to affect this trial
        key_resp_2.clearEvents()
        
        # keep track of which components have finished
        trialComponents = [Stim, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            if Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                Stim.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(Correct)) or (key_resp_2.keys == Correct):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 45:
                if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                    Blocks_Control1.finished = True
                    continueRoutine = False
                elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                    Blocks_Control2.finished = True
                    continueRoutine = False
                elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                    Blocks_Control3.finished = True
                    continueRoutine = False
                elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                    Blocks_Control4.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_A' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                    Blocks_TMTA1.finished = True
                    continueRoutine = False
                elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                    Blocks_TMTA2.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_B' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'B1' or 'B2' or 'B3':
                    Blocks_TMTB1.finished = True
                    continueRoutine = False
                elif Block_paper == 'B4' or 'B5' or 'B6':
                    Blocks_TMTB2.finished = True
                    continueRoutine = False
                    
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_Control3.addData('Stim.started', Stim.tStartRefresh)
        trials_Control3.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_Control3 (TrialHandler)
        trials_Control3.addData('key_resp_2.keys',key_resp_2.keys)
        trials_Control3.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_Control3.addData('key_resp_2.rt', key_resp_2.rt)
        trials_Control3.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_Control3.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        if key_resp_2.keys is not None:
            attempts = len(key_resp_2.keys)    
            currentLoop.addData('Attempts', attempts)
        
        print(f"pressed: {key_resp_2.keys}")
        print(f"corrcet: {Correct}")
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_Control3'
    
    # get names of stimulus parameters
    if trials_Control3.trialList in ([], [None], None):
        params = []
    else:
        params = trials_Control3.trialList[0].keys()
    # save data for this loop
    trials_Control3.saveAsExcel(filename + '.xlsx', sheetName='trials_Control3',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "End_TMT"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    End_TMTComponents = [polygon_4]
    for thisComponent in End_TMTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_TMT"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_TMTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_TMTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 47.5:
            if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                Blocks_Control1.finished = True
                continueRoutine = False
            elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                Blocks_Control2.finished = True
                continueRoutine = False
            elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                Blocks_Control3.finished = True
                continueRoutine = False
            elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                Blocks_Control4.finished = True
                continueRoutine = False
        
        if Version == 'TMT_A' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                Blocks_TMTA1.finished = True
                continueRoutine = False
            elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                Blocks_TMTA2.finished = True
                continueRoutine = False
        
        if Version == 'TMT_B' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'B1' or 'B2' or 'B3':
                Blocks_TMTB1.finished = True
                continueRoutine = False
            elif Block_paper == 'B4' or 'B5' or 'B6':
                Blocks_TMTB2.finished = True
                continueRoutine = False
        
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_TMTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_TMT"-------
    for thisComponent in End_TMTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_Control3'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
# update component parameters for each repeat
cross_duration = normal(cross_duration_mean,2.2)

if cross_duration > 8:
    cross_duration = 8
if cross_duration < 2:
    cross_duration = 2
  
print(f"cross duration: {cross_duration}")
# keep track of which components have finished
FixCrossComponents = [polygon]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 50:
        continueRoutine = False
    elif Version == 'TMT_A' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
    elif Version == 'TMT_B' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startTime = globalClock.getTime()
# the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "utspritt"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
# keep track of which components have finished
utsprittComponents = [utspritt_txt]
for thisComponent in utsprittComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
utsprittClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "utspritt"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = utsprittClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=utsprittClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *utspritt_txt* updates
    if utspritt_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        utspritt_txt.frameNStart = frameN  # exact frame index
        utspritt_txt.tStart = t  # local t and not account for scr refresh
        utspritt_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(utspritt_txt, 'tStartRefresh')  # time at next scr refresh
        utspritt_txt.setAutoDraw(True)
    if utspritt_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > utspritt_txt.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            utspritt_txt.tStop = t  # not accounting for scr refresh
            utspritt_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(utspritt_txt, 'tStopRefresh')  # time at next scr refresh
            utspritt_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in utsprittComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "utspritt"-------
for thisComponent in utsprittComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('utspritt_txt.started', utspritt_txt.tStartRefresh)
thisExp.addData('utspritt_txt.stopped', utspritt_txt.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Blocks_TMTA2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMT_conditions.xlsx', selection='19:23'),
    seed=None, name='Blocks_TMTA2')
thisExp.addLoop(Blocks_TMTA2)  # add the loop to the experiment
thisBlocks_TMTA2 = Blocks_TMTA2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTA2.rgb)
if thisBlocks_TMTA2 != None:
    for paramName in thisBlocks_TMTA2:
        exec('{} = thisBlocks_TMTA2[paramName]'.format(paramName))

for thisBlocks_TMTA2 in Blocks_TMTA2:
    currentLoop = Blocks_TMTA2
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTA2.rgb)
    if thisBlocks_TMTA2 != None:
        for paramName in thisBlocks_TMTA2:
            exec('{} = thisBlocks_TMTA2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_TMTA2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMT_trials.xlsx', selection=Condition_rows),
        seed=None, name='trials_TMTA2')
    thisExp.addLoop(trials_TMTA2)  # add the loop to the experiment
    thisTrials_TMTA2 = trials_TMTA2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTA2.rgb)
    if thisTrials_TMTA2 != None:
        for paramName in thisTrials_TMTA2:
            exec('{} = thisTrials_TMTA2[paramName]'.format(paramName))
    
    for thisTrials_TMTA2 in trials_TMTA2:
        currentLoop = trials_TMTA2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTA2.rgb)
        if thisTrials_TMTA2 != None:
            for paramName in thisTrials_TMTA2:
                exec('{} = thisTrials_TMTA2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        
        #Clear keyes from last trial to affect this trial
        key_resp_2.clearEvents()
        
        # keep track of which components have finished
        trialComponents = [Stim, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            if Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                Stim.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(Correct)) or (key_resp_2.keys == Correct):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 45:
                if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                    Blocks_Control1.finished = True
                    continueRoutine = False
                elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                    Blocks_Control2.finished = True
                    continueRoutine = False
                elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                    Blocks_Control3.finished = True
                    continueRoutine = False
                elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                    Blocks_Control4.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_A' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                    Blocks_TMTA1.finished = True
                    continueRoutine = False
                elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                    Blocks_TMTA2.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_B' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'B1' or 'B2' or 'B3':
                    Blocks_TMTB1.finished = True
                    continueRoutine = False
                elif Block_paper == 'B4' or 'B5' or 'B6':
                    Blocks_TMTB2.finished = True
                    continueRoutine = False
                    
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_TMTA2.addData('Stim.started', Stim.tStartRefresh)
        trials_TMTA2.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_TMTA2 (TrialHandler)
        trials_TMTA2.addData('key_resp_2.keys',key_resp_2.keys)
        trials_TMTA2.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_TMTA2.addData('key_resp_2.rt', key_resp_2.rt)
        trials_TMTA2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_TMTA2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        if key_resp_2.keys is not None:
            attempts = len(key_resp_2.keys)    
            currentLoop.addData('Attempts', attempts)
        
        print(f"pressed: {key_resp_2.keys}")
        print(f"corrcet: {Correct}")
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_TMTA2'
    
    # get names of stimulus parameters
    if trials_TMTA2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_TMTA2.trialList[0].keys()
    # save data for this loop
    trials_TMTA2.saveAsExcel(filename + '.xlsx', sheetName='trials_TMTA2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "End_TMT"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    End_TMTComponents = [polygon_4]
    for thisComponent in End_TMTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_TMT"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_TMTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_TMTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 47.5:
            if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                Blocks_Control1.finished = True
                continueRoutine = False
            elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                Blocks_Control2.finished = True
                continueRoutine = False
            elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                Blocks_Control3.finished = True
                continueRoutine = False
            elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                Blocks_Control4.finished = True
                continueRoutine = False
        
        if Version == 'TMT_A' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                Blocks_TMTA1.finished = True
                continueRoutine = False
            elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                Blocks_TMTA2.finished = True
                continueRoutine = False
        
        if Version == 'TMT_B' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'B1' or 'B2' or 'B3':
                Blocks_TMTB1.finished = True
                continueRoutine = False
            elif Block_paper == 'B4' or 'B5' or 'B6':
                Blocks_TMTB2.finished = True
                continueRoutine = False
        
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_TMTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_TMT"-------
    for thisComponent in End_TMTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_TMTA2'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
# update component parameters for each repeat
cross_duration = normal(cross_duration_mean,2.2)

if cross_duration > 8:
    cross_duration = 8
if cross_duration < 2:
    cross_duration = 2
  
print(f"cross duration: {cross_duration}")
# keep track of which components have finished
FixCrossComponents = [polygon]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 50:
        continueRoutine = False
    elif Version == 'TMT_A' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
    elif Version == 'TMT_B' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startTime = globalClock.getTime()
# the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "cirkel_text"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
cirkel_textComponents = [cirkel_2]
for thisComponent in cirkel_textComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
cirkel_textClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "cirkel_text"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = cirkel_textClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=cirkel_textClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cirkel_2* updates
    if cirkel_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        cirkel_2.frameNStart = frameN  # exact frame index
        cirkel_2.tStart = t  # local t and not account for scr refresh
        cirkel_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cirkel_2, 'tStartRefresh')  # time at next scr refresh
        cirkel_2.setAutoDraw(True)
    if cirkel_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > cirkel_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            cirkel_2.tStop = t  # not accounting for scr refresh
            cirkel_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(cirkel_2, 'tStopRefresh')  # time at next scr refresh
            cirkel_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in cirkel_textComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "cirkel_text"-------
for thisComponent in cirkel_textComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cirkel_2.started', cirkel_2.tStartRefresh)
thisExp.addData('cirkel_2.stopped', cirkel_2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Blocks_Control4 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMT_conditions.xlsx', selection='23:27'),
    seed=None, name='Blocks_Control4')
thisExp.addLoop(Blocks_Control4)  # add the loop to the experiment
thisBlocks_Control4 = Blocks_Control4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_Control4.rgb)
if thisBlocks_Control4 != None:
    for paramName in thisBlocks_Control4:
        exec('{} = thisBlocks_Control4[paramName]'.format(paramName))

for thisBlocks_Control4 in Blocks_Control4:
    currentLoop = Blocks_Control4
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_Control4.rgb)
    if thisBlocks_Control4 != None:
        for paramName in thisBlocks_Control4:
            exec('{} = thisBlocks_Control4[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_Control4 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMT_trials.xlsx', selection=Condition_rows),
        seed=None, name='trials_Control4')
    thisExp.addLoop(trials_Control4)  # add the loop to the experiment
    thisTrials_Control4 = trials_Control4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_Control4.rgb)
    if thisTrials_Control4 != None:
        for paramName in thisTrials_Control4:
            exec('{} = thisTrials_Control4[paramName]'.format(paramName))
    
    for thisTrials_Control4 in trials_Control4:
        currentLoop = trials_Control4
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_Control4.rgb)
        if thisTrials_Control4 != None:
            for paramName in thisTrials_Control4:
                exec('{} = thisTrials_Control4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        
        #Clear keyes from last trial to affect this trial
        key_resp_2.clearEvents()
        
        # keep track of which components have finished
        trialComponents = [Stim, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            if Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                Stim.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(Correct)) or (key_resp_2.keys == Correct):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 45:
                if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                    Blocks_Control1.finished = True
                    continueRoutine = False
                elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                    Blocks_Control2.finished = True
                    continueRoutine = False
                elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                    Blocks_Control3.finished = True
                    continueRoutine = False
                elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                    Blocks_Control4.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_A' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                    Blocks_TMTA1.finished = True
                    continueRoutine = False
                elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                    Blocks_TMTA2.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_B' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'B1' or 'B2' or 'B3':
                    Blocks_TMTB1.finished = True
                    continueRoutine = False
                elif Block_paper == 'B4' or 'B5' or 'B6':
                    Blocks_TMTB2.finished = True
                    continueRoutine = False
                    
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_Control4.addData('Stim.started', Stim.tStartRefresh)
        trials_Control4.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_Control4 (TrialHandler)
        trials_Control4.addData('key_resp_2.keys',key_resp_2.keys)
        trials_Control4.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_Control4.addData('key_resp_2.rt', key_resp_2.rt)
        trials_Control4.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_Control4.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        if key_resp_2.keys is not None:
            attempts = len(key_resp_2.keys)    
            currentLoop.addData('Attempts', attempts)
        
        print(f"pressed: {key_resp_2.keys}")
        print(f"corrcet: {Correct}")
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_Control4'
    
    # get names of stimulus parameters
    if trials_Control4.trialList in ([], [None], None):
        params = []
    else:
        params = trials_Control4.trialList[0].keys()
    # save data for this loop
    trials_Control4.saveAsExcel(filename + '.xlsx', sheetName='trials_Control4',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "End_TMT"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    End_TMTComponents = [polygon_4]
    for thisComponent in End_TMTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_TMT"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_TMTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_TMTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 47.5:
            if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                Blocks_Control1.finished = True
                continueRoutine = False
            elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                Blocks_Control2.finished = True
                continueRoutine = False
            elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                Blocks_Control3.finished = True
                continueRoutine = False
            elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                Blocks_Control4.finished = True
                continueRoutine = False
        
        if Version == 'TMT_A' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                Blocks_TMTA1.finished = True
                continueRoutine = False
            elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                Blocks_TMTA2.finished = True
                continueRoutine = False
        
        if Version == 'TMT_B' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'B1' or 'B2' or 'B3':
                Blocks_TMTB1.finished = True
                continueRoutine = False
            elif Block_paper == 'B4' or 'B5' or 'B6':
                Blocks_TMTB2.finished = True
                continueRoutine = False
        
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_TMTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_TMT"-------
    for thisComponent in End_TMTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_Control4'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
# update component parameters for each repeat
cross_duration = normal(cross_duration_mean,2.2)

if cross_duration > 8:
    cross_duration = 8
if cross_duration < 2:
    cross_duration = 2
  
print(f"cross duration: {cross_duration}")
# keep track of which components have finished
FixCrossComponents = [polygon]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 50:
        continueRoutine = False
    elif Version == 'TMT_A' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
    elif Version == 'TMT_B' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startTime = globalClock.getTime()
# the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "TMTB_info"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
TMTB_infoComponents = [Info2]
for thisComponent in TMTB_infoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TMTB_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "TMTB_info"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = TMTB_infoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TMTB_infoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Info2* updates
    if Info2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Info2.frameNStart = frameN  # exact frame index
        Info2.tStart = t  # local t and not account for scr refresh
        Info2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Info2, 'tStartRefresh')  # time at next scr refresh
        Info2.setAutoDraw(True)
    if Info2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Info2.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            Info2.tStop = t  # not accounting for scr refresh
            Info2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Info2, 'tStopRefresh')  # time at next scr refresh
            Info2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TMTB_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "TMTB_info"-------
for thisComponent in TMTB_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Info2.started', Info2.tStartRefresh)
thisExp.addData('Info2.stopped', Info2.tStopRefresh)
startTime = globalClock.getTime()

# set up handler to look after randomisation of conditions etc
Blocks_TMTB2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMT_conditions.xlsx', selection='27:30'),
    seed=None, name='Blocks_TMTB2')
thisExp.addLoop(Blocks_TMTB2)  # add the loop to the experiment
thisBlocks_TMTB2 = Blocks_TMTB2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTB2.rgb)
if thisBlocks_TMTB2 != None:
    for paramName in thisBlocks_TMTB2:
        exec('{} = thisBlocks_TMTB2[paramName]'.format(paramName))

for thisBlocks_TMTB2 in Blocks_TMTB2:
    currentLoop = Blocks_TMTB2
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTB2.rgb)
    if thisBlocks_TMTB2 != None:
        for paramName in thisBlocks_TMTB2:
            exec('{} = thisBlocks_TMTB2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_TMTB2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMT_trials.xlsx', selection=Condition_rows),
        seed=None, name='trials_TMTB2')
    thisExp.addLoop(trials_TMTB2)  # add the loop to the experiment
    thisTrials_TMTB2 = trials_TMTB2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTB2.rgb)
    if thisTrials_TMTB2 != None:
        for paramName in thisTrials_TMTB2:
            exec('{} = thisTrials_TMTB2[paramName]'.format(paramName))
    
    for thisTrials_TMTB2 in trials_TMTB2:
        currentLoop = trials_TMTB2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTB2.rgb)
        if thisTrials_TMTB2 != None:
            for paramName in thisTrials_TMTB2:
                exec('{} = thisTrials_TMTB2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        
        #Clear keyes from last trial to affect this trial
        key_resp_2.clearEvents()
        
        # keep track of which components have finished
        trialComponents = [Stim, key_resp_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim* updates
            if Stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim.frameNStart = frameN  # exact frame index
                Stim.tStart = t  # local t and not account for scr refresh
                Stim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim, 'tStartRefresh')  # time at next scr refresh
                Stim.setAutoDraw(True)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(Correct)) or (key_resp_2.keys == Correct):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 45:
                if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                    Blocks_Control1.finished = True
                    continueRoutine = False
                elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                    Blocks_Control2.finished = True
                    continueRoutine = False
                elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                    Blocks_Control3.finished = True
                    continueRoutine = False
                elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                    Blocks_Control4.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_A' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                    Blocks_TMTA1.finished = True
                    continueRoutine = False
                elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                    Blocks_TMTA2.finished = True
                    continueRoutine = False
            
            if Version == 'TMT_B' and globalClock.getTime() - startTime >= 90:
                if Block_paper == 'B1' or 'B2' or 'B3':
                    Blocks_TMTB1.finished = True
                    continueRoutine = False
                elif Block_paper == 'B4' or 'B5' or 'B6':
                    Blocks_TMTB2.finished = True
                    continueRoutine = False
                    
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_TMTB2.addData('Stim.started', Stim.tStartRefresh)
        trials_TMTB2.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_TMTB2 (TrialHandler)
        trials_TMTB2.addData('key_resp_2.keys',key_resp_2.keys)
        trials_TMTB2.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_TMTB2.addData('key_resp_2.rt', key_resp_2.rt)
        trials_TMTB2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_TMTB2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        if key_resp_2.keys is not None:
            attempts = len(key_resp_2.keys)    
            currentLoop.addData('Attempts', attempts)
        
        print(f"pressed: {key_resp_2.keys}")
        print(f"corrcet: {Correct}")
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_TMTB2'
    
    # get names of stimulus parameters
    if trials_TMTB2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_TMTB2.trialList[0].keys()
    # save data for this loop
    trials_TMTB2.saveAsExcel(filename + '.xlsx', sheetName='trials_TMTB2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "End_TMT"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    End_TMTComponents = [polygon_4]
    for thisComponent in End_TMTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_TMTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_TMT"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_TMTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_TMTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 47.5:
            if Block_paper == 'C1' or 'C2' or 'C3' or 'C4':
                Blocks_Control1.finished = True
                continueRoutine = False
            elif Block_paper == 'C5' or 'C6' or 'C7' or 'C8':
                Blocks_Control2.finished = True
                continueRoutine = False
            elif Block_paper == 'C9' or 'C10' or 'C11' or 'C12':
                Blocks_Control3.finished = True
                continueRoutine = False
            elif Block_paper == 'C13' or 'C14' or 'C15' or 'C16':
                Blocks_Control4.finished = True
                continueRoutine = False
        
        if Version == 'TMT_A' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'A1' or 'A2' or 'A3' or 'A4':
                Blocks_TMTA1.finished = True
                continueRoutine = False
            elif Block_paper == 'A5' or 'A6' or 'A7' or 'A8':
                Blocks_TMTA2.finished = True
                continueRoutine = False
        
        if Version == 'TMT_B' and globalClock.getTime() - startTime >= 92.5:
            if Block_paper == 'B1' or 'B2' or 'B3':
                Blocks_TMTB1.finished = True
                continueRoutine = False
            elif Block_paper == 'B4' or 'B5' or 'B6':
                Blocks_TMTB2.finished = True
                continueRoutine = False
        
        
            
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_TMTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_TMT"-------
    for thisComponent in End_TMTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_TMTB2'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
# update component parameters for each repeat
cross_duration = normal(cross_duration_mean,2.2)

if cross_duration > 8:
    cross_duration = 8
if cross_duration < 2:
    cross_duration = 2
  
print(f"cross duration: {cross_duration}")
# keep track of which components have finished
FixCrossComponents = [polygon]
for thisComponent in FixCrossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FixCross"-------
while continueRoutine:
    # get current time
    t = FixCrossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if polygon.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        polygon.frameNStart = frameN  # exact frame index
        polygon.tStart = t  # local t and not account for scr refresh
        polygon.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    if Version == 'TMT_Control' and globalClock.getTime() - startTime >= 50:
        continueRoutine = False
    elif Version == 'TMT_A' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
    elif Version == 'TMT_B' and globalClock.getTime() - startTime >= 95:   
        continueRoutine = False
        
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FixCross"-------
for thisComponent in FixCrossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
startTime = globalClock.getTime()
# the Routine "FixCross" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
