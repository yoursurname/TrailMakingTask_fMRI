#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on November 17, 2022, at 17:05
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
psychopyVersion = '2021.2.3'
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
    originPath='C:\\Users\\emilo\\OneDrive - Lund University\\Jobb\\Experiments\\TMT_PsychoPY_new\\TMT_fmri_git\\TMT_fmri.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[3440, 1440], fullscr=True, screen=0, 
    winType='glfw', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instruktioner_TMTControl"
Instruktioner_TMTControlClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='Instruktioner TMTstopA_first.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.28, 0.72),
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

# Initialize components for Routine "EndLoop"
EndLoopClock = core.Clock()

# Initialize components for Routine "trial_baseline"
trial_baselineClock = core.Clock()
Stim_2 = visual.ImageStim(
    win=win,
    name='Stim_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.777, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "FixCross_Baseline"
FixCross_BaselineClock = core.Clock()
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
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
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.777, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial_baseline"
trial_baselineClock = core.Clock()
Stim_2 = visual.ImageStim(
    win=win,
    name='Stim_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.777, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "FixCross_Baseline"
FixCross_BaselineClock = core.Clock()
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
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
    ori=0.0, pos=(0, 0), size=(1.777, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "TMTA_info"
TMTA_infoClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Numerisk ordning.\n\n(1-2-3-4...)',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_baseline"
trial_baselineClock = core.Clock()
Stim_2 = visual.ImageStim(
    win=win,
    name='Stim_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.777, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "FixCross_Baseline"
FixCross_BaselineClock = core.Clock()
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
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
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
Stim = visual.ImageStim(
    win=win,
    name='Stim', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.777, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "trial_baseline"
trial_baselineClock = core.Clock()
Stim_2 = visual.ImageStim(
    win=win,
    name='Stim_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.777, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "FixCross_Baseline"
FixCross_BaselineClock = core.Clock()
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
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
    ori=0.0, pos=(0, 0), size=(1.777, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()
total_corr=0
total_all=0
msg2=''
rt=0
first_attempt=0



# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Tiden är ute!\n\nBra jobbat, du har slutfört experimentet.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruktioner_TMTControl"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Instruktioner_TMTControlComponents = [image_2, key_resp_6]
for thisComponent in Instruktioner_TMTControlComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instruktioner_TMTControlClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruktioner_TMTControl"-------
while continueRoutine:
    # get current time
    t = Instruktioner_TMTControlClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instruktioner_TMTControlClock)
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
    for thisComponent in Instruktioner_TMTControlComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruktioner_TMTControl"-------
for thisComponent in Instruktioner_TMTControlComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruktioner_TMTControl" was not non-slip safe, so reset the non-slip timer
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
        core.wait(4.5)
        core.wait(4.5)
        core.wait(4.5)
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

# set up handler to look after randomisation of conditions etc
Blocks_TMTControl = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMTstop-Control_1_conditions.xlsx', selection='0:2'),
    seed=None, name='Blocks_TMTControl')
thisExp.addLoop(Blocks_TMTControl)  # add the loop to the experiment
thisBlocks_TMTControl = Blocks_TMTControl.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTControl.rgb)
if thisBlocks_TMTControl != None:
    for paramName in thisBlocks_TMTControl:
        exec('{} = thisBlocks_TMTControl[paramName]'.format(paramName))

for thisBlocks_TMTControl in Blocks_TMTControl:
    currentLoop = Blocks_TMTControl
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTControl.rgb)
    if thisBlocks_TMTControl != None:
        for paramName in thisBlocks_TMTControl:
            exec('{} = thisBlocks_TMTControl[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "EndLoop"-------
    continueRoutine = True
    # update component parameters for each repeat
    if globalClock.getTime() - startTime >= 47.5:
        currentLoop.finished = True
    # keep track of which components have finished
    EndLoopComponents = []
    for thisComponent in EndLoopComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EndLoopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "EndLoop"-------
    while continueRoutine:
        # get current time
        t = EndLoopClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EndLoopClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndLoopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "EndLoop"-------
    for thisComponent in EndLoopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "EndLoop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_baseline1 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMTstop-control_1_merged.xlsx', selection=Condition_rows),
        seed=None, name='trials_baseline1')
    thisExp.addLoop(trials_baseline1)  # add the loop to the experiment
    thisTrials_baseline1 = trials_baseline1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline1.rgb)
    if thisTrials_baseline1 != None:
        for paramName in thisTrials_baseline1:
            exec('{} = thisTrials_baseline1[paramName]'.format(paramName))
    
    for thisTrials_baseline1 in trials_baseline1:
        currentLoop = trials_baseline1
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline1.rgb)
        if thisTrials_baseline1 != None:
            for paramName in thisTrials_baseline1:
                exec('{} = thisTrials_baseline1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_baseline"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim_2.setImage(Correct_StimFile)
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        #if key_resp_2.corr:
          #total_corr=total_corr+1
          #total_all=total_all+1
          #rt=key_resp_2.rt
          #Stim.setImage(Correct_StimFile)
          
        
        #else:
          #msg='buzzerwrong.wav'
          #total_all=total_all+1
          #rt=key_resp_2.rt
        
        
        if Round == 1 or 2: # only on the first trial per round
            startTime = globalClock.getTime()
            
        
        
        # keep track of which components have finished
        trial_baselineComponents = [Stim_2, key_resp_8]
        for thisComponent in trial_baselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_baseline"-------
        while continueRoutine:
            # get current time
            t = trial_baselineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_baselineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim_2* updates
            if Stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim_2.frameNStart = frameN  # exact frame index
                Stim_2.tStart = t  # local t and not account for scr refresh
                Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_2, 'tStartRefresh')  # time at next scr refresh
                Stim_2.setAutoDraw(True)
            
            # *key_resp_8* updates
            waitOnFlip = False
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = [key.name for key in _key_resp_8_allKeys]  # storing all keys
                    key_resp_8.rt = [key.rt for key in _key_resp_8_allKeys]
                    # was this correct?
                    if (key_resp_8.keys == str(corrAns)) or (key_resp_8.keys == corrAns):
                        key_resp_8.corr = 1
                    else:
                        key_resp_8.corr = 0
            if globalClock.getTime() - startTime >= 45:
                currentLoop.finished = True
                continueRoutine = False
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_8.keys) > 0 and [key_resp_8.keys[-1]] == corrAns:
                key_resp_8.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            #elif len(key_resp_2.keys) == 5:   # give up after 5 attempts.
                #continueRoutine = False # don't need to override resp.corr in this case
            
            elif len(key_resp_8.keys) > 0 and [key_resp_8.keys] != corrAns:
                key_resp_8.corr = 0
                #continueRoutine = True
                Stim_2.setImage(False_StimFile)
                
            attempts = len(key_resp_8.keys)    
            thisExp.addData('Attempts', attempts)
            
            if len(key_resp_8.keys) == 1:
                first_attempt = 1
            else:
                first_attempt = 0
                
            thisExp.addData('First_attempt', first_attempt)
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_baselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_baseline"-------
        for thisComponent in trial_baselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_baseline1.addData('Stim_2.started', Stim_2.tStartRefresh)
        trials_baseline1.addData('Stim_2.stopped', Stim_2.tStopRefresh)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_8.corr = 1;  # correct non-response
            else:
               key_resp_8.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_baseline1 (TrialHandler)
        trials_baseline1.addData('key_resp_8.keys',key_resp_8.keys)
        trials_baseline1.addData('key_resp_8.corr', key_resp_8.corr)
        if key_resp_8.keys != None:  # we had a response
            trials_baseline1.addData('key_resp_8.rt', key_resp_8.rt)
        trials_baseline1.addData('key_resp_8.started', key_resp_8.tStartRefresh)
        trials_baseline1.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
        # the Routine "trial_baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_baseline1'
    
    # get names of stimulus parameters
    if trials_baseline1.trialList in ([], [None], None):
        params = []
    else:
        params = trials_baseline1.trialList[0].keys()
    # save data for this loop
    trials_baseline1.saveAsExcel(filename + '.xlsx', sheetName='trials_baseline1',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_baseline1.saveAsText(filename + 'trials_baseline1.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "FixCross_Baseline"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixCross_BaselineComponents = [polygon_3]
    for thisComponent in FixCross_BaselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixCross_BaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixCross_Baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCross_BaselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixCross_BaselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        if globalClock.getTime() - startTime >= 47.5:
            currentLoop.nReps = 0
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCross_BaselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross_Baseline"-------
    for thisComponent in FixCross_BaselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_TMTControl'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
if globalClock.getTime() - startTime >= 92.5:
    currentLoop.finished = True
    continueRoutine = False
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    
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

# set up handler to look after randomisation of conditions etc
Blocks_TMTA = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMTstop-A_1_conditions.xlsx', selection='0:3'),
    seed=None, name='Blocks_TMTA')
thisExp.addLoop(Blocks_TMTA)  # add the loop to the experiment
thisBlocks_TMTA = Blocks_TMTA.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTA.rgb)
if thisBlocks_TMTA != None:
    for paramName in thisBlocks_TMTA:
        exec('{} = thisBlocks_TMTA[paramName]'.format(paramName))

for thisBlocks_TMTA in Blocks_TMTA:
    currentLoop = Blocks_TMTA
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTA.rgb)
    if thisBlocks_TMTA != None:
        for paramName in thisBlocks_TMTA:
            exec('{} = thisBlocks_TMTA[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_TMTA = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMTstop-A_1_merged.xlsx', selection=Condition_rows),
        seed=None, name='trials_TMTA')
    thisExp.addLoop(trials_TMTA)  # add the loop to the experiment
    thisTrials_TMTA = trials_TMTA.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTA.rgb)
    if thisTrials_TMTA != None:
        for paramName in thisTrials_TMTA:
            exec('{} = thisTrials_TMTA[paramName]'.format(paramName))
    
    for thisTrials_TMTA in trials_TMTA:
        currentLoop = trials_TMTA
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTA.rgb)
        if thisTrials_TMTA != None:
            for paramName in thisTrials_TMTA:
                exec('{} = thisTrials_TMTA[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        #if key_resp_2.corr:
          #total_corr=total_corr+1
          #total_all=total_all+1
          #rt=key_resp_2.rt
          #Stim.setImage(Correct_StimFile)
          
        
        #else:
          #msg='buzzerwrong.wav'
          #total_all=total_all+1
          #rt=key_resp_2.rt
        
        
        if Round == 1 or 2: # only on the first trial per round
            startTime = globalClock.getTime()
            
        
        
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
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if globalClock.getTime() - startTime >= 90:
                currentLoop.finished = True
                continueRoutine = False
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            #elif len(key_resp_2.keys) == 5:   # give up after 5 attempts.
                #continueRoutine = False # don't need to override resp.corr in this case
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            attempts = len(key_resp_2.keys)    
            thisExp.addData('Attempts', attempts)
            
            if len(key_resp_2.keys) == 1:
                first_attempt = 1
            else:
                first_attempt = 0
                
            thisExp.addData('First_attempt', first_attempt)
            
            
            
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
        trials_TMTA.addData('Stim.started', Stim.tStartRefresh)
        trials_TMTA.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_TMTA (TrialHandler)
        trials_TMTA.addData('key_resp_2.keys',key_resp_2.keys)
        trials_TMTA.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_TMTA.addData('key_resp_2.rt', key_resp_2.rt)
        trials_TMTA.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_TMTA.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_TMTA'
    
    # get names of stimulus parameters
    if trials_TMTA.trialList in ([], [None], None):
        params = []
    else:
        params = trials_TMTA.trialList[0].keys()
    # save data for this loop
    trials_TMTA.saveAsExcel(filename + '.xlsx', sheetName='trials_TMTA',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_TMTA.saveAsText(filename + 'trials_TMTA.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "FixCross"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if globalClock.getTime() - startTime >= 92.5:
        currentLoop.finished = True
        continueRoutine = False
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
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
# completed 1.0 repeats of 'Blocks_TMTA'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
if globalClock.getTime() - startTime >= 92.5:
    currentLoop.finished = True
    continueRoutine = False
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    
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

# set up handler to look after randomisation of conditions etc
Blocks_baseline2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMTstop-Control_1_conditions.xlsx', selection='2:4'),
    seed=None, name='Blocks_baseline2')
thisExp.addLoop(Blocks_baseline2)  # add the loop to the experiment
thisBlocks_baseline2 = Blocks_baseline2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_baseline2.rgb)
if thisBlocks_baseline2 != None:
    for paramName in thisBlocks_baseline2:
        exec('{} = thisBlocks_baseline2[paramName]'.format(paramName))

for thisBlocks_baseline2 in Blocks_baseline2:
    currentLoop = Blocks_baseline2
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_baseline2.rgb)
    if thisBlocks_baseline2 != None:
        for paramName in thisBlocks_baseline2:
            exec('{} = thisBlocks_baseline2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_baseline2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMTstop-control_1_merged.xlsx', selection=Condition_rows),
        seed=None, name='trials_baseline2')
    thisExp.addLoop(trials_baseline2)  # add the loop to the experiment
    thisTrials_baseline2 = trials_baseline2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline2.rgb)
    if thisTrials_baseline2 != None:
        for paramName in thisTrials_baseline2:
            exec('{} = thisTrials_baseline2[paramName]'.format(paramName))
    
    for thisTrials_baseline2 in trials_baseline2:
        currentLoop = trials_baseline2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline2.rgb)
        if thisTrials_baseline2 != None:
            for paramName in thisTrials_baseline2:
                exec('{} = thisTrials_baseline2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_baseline"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim_2.setImage(Correct_StimFile)
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        #if key_resp_2.corr:
          #total_corr=total_corr+1
          #total_all=total_all+1
          #rt=key_resp_2.rt
          #Stim.setImage(Correct_StimFile)
          
        
        #else:
          #msg='buzzerwrong.wav'
          #total_all=total_all+1
          #rt=key_resp_2.rt
        
        
        if Round == 1 or 2: # only on the first trial per round
            startTime = globalClock.getTime()
            
        
        
        # keep track of which components have finished
        trial_baselineComponents = [Stim_2, key_resp_8]
        for thisComponent in trial_baselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_baseline"-------
        while continueRoutine:
            # get current time
            t = trial_baselineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_baselineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim_2* updates
            if Stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim_2.frameNStart = frameN  # exact frame index
                Stim_2.tStart = t  # local t and not account for scr refresh
                Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_2, 'tStartRefresh')  # time at next scr refresh
                Stim_2.setAutoDraw(True)
            
            # *key_resp_8* updates
            waitOnFlip = False
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = [key.name for key in _key_resp_8_allKeys]  # storing all keys
                    key_resp_8.rt = [key.rt for key in _key_resp_8_allKeys]
                    # was this correct?
                    if (key_resp_8.keys == str(corrAns)) or (key_resp_8.keys == corrAns):
                        key_resp_8.corr = 1
                    else:
                        key_resp_8.corr = 0
            if globalClock.getTime() - startTime >= 45:
                currentLoop.finished = True
                continueRoutine = False
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_8.keys) > 0 and [key_resp_8.keys[-1]] == corrAns:
                key_resp_8.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            #elif len(key_resp_2.keys) == 5:   # give up after 5 attempts.
                #continueRoutine = False # don't need to override resp.corr in this case
            
            elif len(key_resp_8.keys) > 0 and [key_resp_8.keys] != corrAns:
                key_resp_8.corr = 0
                #continueRoutine = True
                Stim_2.setImage(False_StimFile)
                
            attempts = len(key_resp_8.keys)    
            thisExp.addData('Attempts', attempts)
            
            if len(key_resp_8.keys) == 1:
                first_attempt = 1
            else:
                first_attempt = 0
                
            thisExp.addData('First_attempt', first_attempt)
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_baselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_baseline"-------
        for thisComponent in trial_baselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_baseline2.addData('Stim_2.started', Stim_2.tStartRefresh)
        trials_baseline2.addData('Stim_2.stopped', Stim_2.tStopRefresh)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_8.corr = 1;  # correct non-response
            else:
               key_resp_8.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_baseline2 (TrialHandler)
        trials_baseline2.addData('key_resp_8.keys',key_resp_8.keys)
        trials_baseline2.addData('key_resp_8.corr', key_resp_8.corr)
        if key_resp_8.keys != None:  # we had a response
            trials_baseline2.addData('key_resp_8.rt', key_resp_8.rt)
        trials_baseline2.addData('key_resp_8.started', key_resp_8.tStartRefresh)
        trials_baseline2.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
        # the Routine "trial_baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_baseline2'
    
    # get names of stimulus parameters
    if trials_baseline2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_baseline2.trialList[0].keys()
    # save data for this loop
    trials_baseline2.saveAsExcel(filename + '.xlsx', sheetName='trials_baseline2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_baseline2.saveAsText(filename + 'trials_baseline2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "FixCross_Baseline"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixCross_BaselineComponents = [polygon_3]
    for thisComponent in FixCross_BaselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixCross_BaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixCross_Baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCross_BaselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixCross_BaselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        if globalClock.getTime() - startTime >= 47.5:
            currentLoop.nReps = 0
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCross_BaselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross_Baseline"-------
    for thisComponent in FixCross_BaselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_baseline2'


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

# set up handler to look after randomisation of conditions etc
Blocks_TMTB = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMTstop-B_1_conditions.xlsx', selection='0:2'),
    seed=None, name='Blocks_TMTB')
thisExp.addLoop(Blocks_TMTB)  # add the loop to the experiment
thisBlocks_TMTB = Blocks_TMTB.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTB.rgb)
if thisBlocks_TMTB != None:
    for paramName in thisBlocks_TMTB:
        exec('{} = thisBlocks_TMTB[paramName]'.format(paramName))

for thisBlocks_TMTB in Blocks_TMTB:
    currentLoop = Blocks_TMTB
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTB.rgb)
    if thisBlocks_TMTB != None:
        for paramName in thisBlocks_TMTB:
            exec('{} = thisBlocks_TMTB[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_TMTB = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMTstop-B_1_merged.xlsx', selection=Condition_rows),
        seed=None, name='trials_TMTB')
    thisExp.addLoop(trials_TMTB)  # add the loop to the experiment
    thisTrials_TMTB = trials_TMTB.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTB.rgb)
    if thisTrials_TMTB != None:
        for paramName in thisTrials_TMTB:
            exec('{} = thisTrials_TMTB[paramName]'.format(paramName))
    
    for thisTrials_TMTB in trials_TMTB:
        currentLoop = trials_TMTB
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTB.rgb)
        if thisTrials_TMTB != None:
            for paramName in thisTrials_TMTB:
                exec('{} = thisTrials_TMTB[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        #if key_resp_2.corr:
          #total_corr=total_corr+1
          #total_all=total_all+1
          #rt=key_resp_2.rt
          #Stim.setImage(Correct_StimFile)
          
        
        #else:
          #msg='buzzerwrong.wav'
          #total_all=total_all+1
          #rt=key_resp_2.rt
        
        
        if Round == 1 or 2: # only on the first trial per round
            startTime = globalClock.getTime()
            
        
        
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
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if globalClock.getTime() - startTime >= 90:
                currentLoop.finished = True
                continueRoutine = False
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            #elif len(key_resp_2.keys) == 5:   # give up after 5 attempts.
                #continueRoutine = False # don't need to override resp.corr in this case
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            attempts = len(key_resp_2.keys)    
            thisExp.addData('Attempts', attempts)
            
            if len(key_resp_2.keys) == 1:
                first_attempt = 1
            else:
                first_attempt = 0
                
            thisExp.addData('First_attempt', first_attempt)
            
            
            
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
        trials_TMTB.addData('Stim.started', Stim.tStartRefresh)
        trials_TMTB.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_TMTB (TrialHandler)
        trials_TMTB.addData('key_resp_2.keys',key_resp_2.keys)
        trials_TMTB.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_TMTB.addData('key_resp_2.rt', key_resp_2.rt)
        trials_TMTB.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_TMTB.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_TMTB'
    
    # get names of stimulus parameters
    if trials_TMTB.trialList in ([], [None], None):
        params = []
    else:
        params = trials_TMTB.trialList[0].keys()
    # save data for this loop
    trials_TMTB.saveAsExcel(filename + '.xlsx', sheetName='trials_TMTB',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_TMTB.saveAsText(filename + 'trials_TMTB.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "FixCross"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if globalClock.getTime() - startTime >= 92.5:
        currentLoop.finished = True
        continueRoutine = False
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
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
# completed 1.0 repeats of 'Blocks_TMTB'


# ------Prepare to start Routine "TMTA_info"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
TMTA_infoComponents = [text_2]
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
        if tThisFlipGlobal > text_2.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
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

# set up handler to look after randomisation of conditions etc
Blocks_baseline3 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMTstop-Control_1_conditions.xlsx', selection='4:6'),
    seed=None, name='Blocks_baseline3')
thisExp.addLoop(Blocks_baseline3)  # add the loop to the experiment
thisBlocks_baseline3 = Blocks_baseline3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_baseline3.rgb)
if thisBlocks_baseline3 != None:
    for paramName in thisBlocks_baseline3:
        exec('{} = thisBlocks_baseline3[paramName]'.format(paramName))

for thisBlocks_baseline3 in Blocks_baseline3:
    currentLoop = Blocks_baseline3
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_baseline3.rgb)
    if thisBlocks_baseline3 != None:
        for paramName in thisBlocks_baseline3:
            exec('{} = thisBlocks_baseline3[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_baseline3 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMTstop-control_1_merged.xlsx', selection=Condition_rows),
        seed=None, name='trials_baseline3')
    thisExp.addLoop(trials_baseline3)  # add the loop to the experiment
    thisTrials_baseline3 = trials_baseline3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline3.rgb)
    if thisTrials_baseline3 != None:
        for paramName in thisTrials_baseline3:
            exec('{} = thisTrials_baseline3[paramName]'.format(paramName))
    
    for thisTrials_baseline3 in trials_baseline3:
        currentLoop = trials_baseline3
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline3.rgb)
        if thisTrials_baseline3 != None:
            for paramName in thisTrials_baseline3:
                exec('{} = thisTrials_baseline3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_baseline"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim_2.setImage(Correct_StimFile)
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        #if key_resp_2.corr:
          #total_corr=total_corr+1
          #total_all=total_all+1
          #rt=key_resp_2.rt
          #Stim.setImage(Correct_StimFile)
          
        
        #else:
          #msg='buzzerwrong.wav'
          #total_all=total_all+1
          #rt=key_resp_2.rt
        
        
        if Round == 1 or 2: # only on the first trial per round
            startTime = globalClock.getTime()
            
        
        
        # keep track of which components have finished
        trial_baselineComponents = [Stim_2, key_resp_8]
        for thisComponent in trial_baselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_baseline"-------
        while continueRoutine:
            # get current time
            t = trial_baselineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_baselineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim_2* updates
            if Stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim_2.frameNStart = frameN  # exact frame index
                Stim_2.tStart = t  # local t and not account for scr refresh
                Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_2, 'tStartRefresh')  # time at next scr refresh
                Stim_2.setAutoDraw(True)
            
            # *key_resp_8* updates
            waitOnFlip = False
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = [key.name for key in _key_resp_8_allKeys]  # storing all keys
                    key_resp_8.rt = [key.rt for key in _key_resp_8_allKeys]
                    # was this correct?
                    if (key_resp_8.keys == str(corrAns)) or (key_resp_8.keys == corrAns):
                        key_resp_8.corr = 1
                    else:
                        key_resp_8.corr = 0
            if globalClock.getTime() - startTime >= 45:
                currentLoop.finished = True
                continueRoutine = False
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_8.keys) > 0 and [key_resp_8.keys[-1]] == corrAns:
                key_resp_8.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            #elif len(key_resp_2.keys) == 5:   # give up after 5 attempts.
                #continueRoutine = False # don't need to override resp.corr in this case
            
            elif len(key_resp_8.keys) > 0 and [key_resp_8.keys] != corrAns:
                key_resp_8.corr = 0
                #continueRoutine = True
                Stim_2.setImage(False_StimFile)
                
            attempts = len(key_resp_8.keys)    
            thisExp.addData('Attempts', attempts)
            
            if len(key_resp_8.keys) == 1:
                first_attempt = 1
            else:
                first_attempt = 0
                
            thisExp.addData('First_attempt', first_attempt)
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_baselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_baseline"-------
        for thisComponent in trial_baselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_baseline3.addData('Stim_2.started', Stim_2.tStartRefresh)
        trials_baseline3.addData('Stim_2.stopped', Stim_2.tStopRefresh)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_8.corr = 1;  # correct non-response
            else:
               key_resp_8.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_baseline3 (TrialHandler)
        trials_baseline3.addData('key_resp_8.keys',key_resp_8.keys)
        trials_baseline3.addData('key_resp_8.corr', key_resp_8.corr)
        if key_resp_8.keys != None:  # we had a response
            trials_baseline3.addData('key_resp_8.rt', key_resp_8.rt)
        trials_baseline3.addData('key_resp_8.started', key_resp_8.tStartRefresh)
        trials_baseline3.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
        # the Routine "trial_baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_baseline3'
    
    # get names of stimulus parameters
    if trials_baseline3.trialList in ([], [None], None):
        params = []
    else:
        params = trials_baseline3.trialList[0].keys()
    # save data for this loop
    trials_baseline3.saveAsExcel(filename + '.xlsx', sheetName='trials_baseline3',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_baseline3.saveAsText(filename + 'trials_baseline3.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "FixCross_Baseline"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixCross_BaselineComponents = [polygon_3]
    for thisComponent in FixCross_BaselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixCross_BaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixCross_Baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCross_BaselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixCross_BaselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        if globalClock.getTime() - startTime >= 47.5:
            currentLoop.nReps = 0
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCross_BaselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross_Baseline"-------
    for thisComponent in FixCross_BaselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'Blocks_baseline3'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
if globalClock.getTime() - startTime >= 92.5:
    currentLoop.finished = True
    continueRoutine = False
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    
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

# set up handler to look after randomisation of conditions etc
Blocks_TMTA_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMTstop-A_1_conditions.xlsx', selection='3:6'),
    seed=None, name='Blocks_TMTA_2')
thisExp.addLoop(Blocks_TMTA_2)  # add the loop to the experiment
thisBlocks_TMTA_2 = Blocks_TMTA_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTA_2.rgb)
if thisBlocks_TMTA_2 != None:
    for paramName in thisBlocks_TMTA_2:
        exec('{} = thisBlocks_TMTA_2[paramName]'.format(paramName))

for thisBlocks_TMTA_2 in Blocks_TMTA_2:
    currentLoop = Blocks_TMTA_2
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTA_2.rgb)
    if thisBlocks_TMTA_2 != None:
        for paramName in thisBlocks_TMTA_2:
            exec('{} = thisBlocks_TMTA_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_TMTA_2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMTstop-A_1_merged.xlsx', selection=Condition_rows),
        seed=None, name='trials_TMTA_2')
    thisExp.addLoop(trials_TMTA_2)  # add the loop to the experiment
    thisTrials_TMTA_2 = trials_TMTA_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTA_2.rgb)
    if thisTrials_TMTA_2 != None:
        for paramName in thisTrials_TMTA_2:
            exec('{} = thisTrials_TMTA_2[paramName]'.format(paramName))
    
    for thisTrials_TMTA_2 in trials_TMTA_2:
        currentLoop = trials_TMTA_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTA_2.rgb)
        if thisTrials_TMTA_2 != None:
            for paramName in thisTrials_TMTA_2:
                exec('{} = thisTrials_TMTA_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        #if key_resp_2.corr:
          #total_corr=total_corr+1
          #total_all=total_all+1
          #rt=key_resp_2.rt
          #Stim.setImage(Correct_StimFile)
          
        
        #else:
          #msg='buzzerwrong.wav'
          #total_all=total_all+1
          #rt=key_resp_2.rt
        
        
        if Round == 1 or 2: # only on the first trial per round
            startTime = globalClock.getTime()
            
        
        
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
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if globalClock.getTime() - startTime >= 90:
                currentLoop.finished = True
                continueRoutine = False
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            #elif len(key_resp_2.keys) == 5:   # give up after 5 attempts.
                #continueRoutine = False # don't need to override resp.corr in this case
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            attempts = len(key_resp_2.keys)    
            thisExp.addData('Attempts', attempts)
            
            if len(key_resp_2.keys) == 1:
                first_attempt = 1
            else:
                first_attempt = 0
                
            thisExp.addData('First_attempt', first_attempt)
            
            
            
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
        trials_TMTA_2.addData('Stim.started', Stim.tStartRefresh)
        trials_TMTA_2.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_TMTA_2 (TrialHandler)
        trials_TMTA_2.addData('key_resp_2.keys',key_resp_2.keys)
        trials_TMTA_2.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_TMTA_2.addData('key_resp_2.rt', key_resp_2.rt)
        trials_TMTA_2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_TMTA_2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_TMTA_2'
    
    # get names of stimulus parameters
    if trials_TMTA_2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_TMTA_2.trialList[0].keys()
    # save data for this loop
    trials_TMTA_2.saveAsExcel(filename + '.xlsx', sheetName='trials_TMTA_2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_TMTA_2.saveAsText(filename + 'trials_TMTA_2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "FixCross"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if globalClock.getTime() - startTime >= 92.5:
        currentLoop.finished = True
        continueRoutine = False
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
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
# completed 1.0 repeats of 'Blocks_TMTA_2'


# ------Prepare to start Routine "FixCross"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
if globalClock.getTime() - startTime >= 92.5:
    currentLoop.finished = True
    continueRoutine = False
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if polygon.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            polygon.tStop = t  # not accounting for scr refresh
            polygon.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
            polygon.setAutoDraw(False)
    
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

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMTstop-Control_1_conditions.xlsx', selection='6:8'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_baseline4 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMTstop-control_1_merged.xlsx', selection=Condition_rows),
        seed=None, name='trials_baseline4')
    thisExp.addLoop(trials_baseline4)  # add the loop to the experiment
    thisTrials_baseline4 = trials_baseline4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline4.rgb)
    if thisTrials_baseline4 != None:
        for paramName in thisTrials_baseline4:
            exec('{} = thisTrials_baseline4[paramName]'.format(paramName))
    
    for thisTrials_baseline4 in trials_baseline4:
        currentLoop = trials_baseline4
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_baseline4.rgb)
        if thisTrials_baseline4 != None:
            for paramName in thisTrials_baseline4:
                exec('{} = thisTrials_baseline4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_baseline"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim_2.setImage(Correct_StimFile)
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        #if key_resp_2.corr:
          #total_corr=total_corr+1
          #total_all=total_all+1
          #rt=key_resp_2.rt
          #Stim.setImage(Correct_StimFile)
          
        
        #else:
          #msg='buzzerwrong.wav'
          #total_all=total_all+1
          #rt=key_resp_2.rt
        
        
        if Round == 1 or 2: # only on the first trial per round
            startTime = globalClock.getTime()
            
        
        
        # keep track of which components have finished
        trial_baselineComponents = [Stim_2, key_resp_8]
        for thisComponent in trial_baselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_baseline"-------
        while continueRoutine:
            # get current time
            t = trial_baselineClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_baselineClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Stim_2* updates
            if Stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stim_2.frameNStart = frameN  # exact frame index
                Stim_2.tStart = t  # local t and not account for scr refresh
                Stim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stim_2, 'tStartRefresh')  # time at next scr refresh
                Stim_2.setAutoDraw(True)
            
            # *key_resp_8* updates
            waitOnFlip = False
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = [key.name for key in _key_resp_8_allKeys]  # storing all keys
                    key_resp_8.rt = [key.rt for key in _key_resp_8_allKeys]
                    # was this correct?
                    if (key_resp_8.keys == str(corrAns)) or (key_resp_8.keys == corrAns):
                        key_resp_8.corr = 1
                    else:
                        key_resp_8.corr = 0
            if globalClock.getTime() - startTime >= 45:
                currentLoop.finished = True
                continueRoutine = False
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_8.keys) > 0 and [key_resp_8.keys[-1]] == corrAns:
                key_resp_8.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            #elif len(key_resp_2.keys) == 5:   # give up after 5 attempts.
                #continueRoutine = False # don't need to override resp.corr in this case
            
            elif len(key_resp_8.keys) > 0 and [key_resp_8.keys] != corrAns:
                key_resp_8.corr = 0
                #continueRoutine = True
                Stim_2.setImage(False_StimFile)
                
            attempts = len(key_resp_8.keys)    
            thisExp.addData('Attempts', attempts)
            
            if len(key_resp_8.keys) == 1:
                first_attempt = 1
            else:
                first_attempt = 0
                
            thisExp.addData('First_attempt', first_attempt)
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_baselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_baseline"-------
        for thisComponent in trial_baselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_baseline4.addData('Stim_2.started', Stim_2.tStartRefresh)
        trials_baseline4.addData('Stim_2.stopped', Stim_2.tStopRefresh)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_8.corr = 1;  # correct non-response
            else:
               key_resp_8.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_baseline4 (TrialHandler)
        trials_baseline4.addData('key_resp_8.keys',key_resp_8.keys)
        trials_baseline4.addData('key_resp_8.corr', key_resp_8.corr)
        if key_resp_8.keys != None:  # we had a response
            trials_baseline4.addData('key_resp_8.rt', key_resp_8.rt)
        trials_baseline4.addData('key_resp_8.started', key_resp_8.tStartRefresh)
        trials_baseline4.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
        # the Routine "trial_baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_baseline4'
    
    # get names of stimulus parameters
    if trials_baseline4.trialList in ([], [None], None):
        params = []
    else:
        params = trials_baseline4.trialList[0].keys()
    # save data for this loop
    trials_baseline4.saveAsExcel(filename + '.xlsx', sheetName='trials_baseline4',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_baseline4.saveAsText(filename + 'trials_baseline4.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "FixCross_Baseline"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixCross_BaselineComponents = [polygon_3]
    for thisComponent in FixCross_BaselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixCross_BaselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixCross_Baseline"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCross_BaselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixCross_BaselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        if globalClock.getTime() - startTime >= 47.5:
            currentLoop.nReps = 0
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCross_BaselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross_Baseline"-------
    for thisComponent in FixCross_BaselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1.0 repeats of 'trials_2'


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

# set up handler to look after randomisation of conditions etc
Blocks_TMTB_2 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TMTstop-B_1_conditions.xlsx', selection='2:5'),
    seed=None, name='Blocks_TMTB_2')
thisExp.addLoop(Blocks_TMTB_2)  # add the loop to the experiment
thisBlocks_TMTB_2 = Blocks_TMTB_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTB_2.rgb)
if thisBlocks_TMTB_2 != None:
    for paramName in thisBlocks_TMTB_2:
        exec('{} = thisBlocks_TMTB_2[paramName]'.format(paramName))

for thisBlocks_TMTB_2 in Blocks_TMTB_2:
    currentLoop = Blocks_TMTB_2
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_TMTB_2.rgb)
    if thisBlocks_TMTB_2 != None:
        for paramName in thisBlocks_TMTB_2:
            exec('{} = thisBlocks_TMTB_2[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_TMTB_2 = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TMTstop-B_1_merged.xlsx', selection=Condition_rows),
        seed=None, name='trials_TMTB_2')
    thisExp.addLoop(trials_TMTB_2)  # add the loop to the experiment
    thisTrials_TMTB_2 = trials_TMTB_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTB_2.rgb)
    if thisTrials_TMTB_2 != None:
        for paramName in thisTrials_TMTB_2:
            exec('{} = thisTrials_TMTB_2[paramName]'.format(paramName))
    
    for thisTrials_TMTB_2 in trials_TMTB_2:
        currentLoop = trials_TMTB_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_TMTB_2.rgb)
        if thisTrials_TMTB_2 != None:
            for paramName in thisTrials_TMTB_2:
                exec('{} = thisTrials_TMTB_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        Stim.setImage(Correct_StimFile)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        #if key_resp_2.corr:
          #total_corr=total_corr+1
          #total_all=total_all+1
          #rt=key_resp_2.rt
          #Stim.setImage(Correct_StimFile)
          
        
        #else:
          #msg='buzzerwrong.wav'
          #total_all=total_all+1
          #rt=key_resp_2.rt
        
        
        if Round == 1 or 2: # only on the first trial per round
            startTime = globalClock.getTime()
            
        
        
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
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                    key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                    # was this correct?
                    if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
            if globalClock.getTime() - startTime >= 90:
                currentLoop.finished = True
                continueRoutine = False
                
            #Display last trial image to show result for 1 sec then ends
            if currentLoop.thisN == 25 and (t >= 1): 
                continueRoutine = False
            
            #End trial only on correct responses
            if len(key_resp_2.keys) > 0 and [key_resp_2.keys[-1]] == corrAns:
                key_resp_2.corr = 1
                thisExp.addData('ResponseClock', Time_Since_Run.getTime())
                continueRoutine = False
                   
            #elif len(key_resp_2.keys) == 5:   # give up after 5 attempts.
                #continueRoutine = False # don't need to override resp.corr in this case
            
            elif len(key_resp_2.keys) > 0 and [key_resp_2.keys] != corrAns:
                key_resp_2.corr = 0
                #continueRoutine = True
                Stim.setImage(False_StimFile)
                
            attempts = len(key_resp_2.keys)    
            thisExp.addData('Attempts', attempts)
            
            if len(key_resp_2.keys) == 1:
                first_attempt = 1
            else:
                first_attempt = 0
                
            thisExp.addData('First_attempt', first_attempt)
            
            
            
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
        trials_TMTB_2.addData('Stim.started', Stim.tStartRefresh)
        trials_TMTB_2.addData('Stim.stopped', Stim.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_TMTB_2 (TrialHandler)
        trials_TMTB_2.addData('key_resp_2.keys',key_resp_2.keys)
        trials_TMTB_2.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            trials_TMTB_2.addData('key_resp_2.rt', key_resp_2.rt)
        trials_TMTB_2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        trials_TMTB_2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_TMTB_2'
    
    # get names of stimulus parameters
    if trials_TMTB_2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_TMTB_2.trialList[0].keys()
    # save data for this loop
    trials_TMTB_2.saveAsExcel(filename + '.xlsx', sheetName='trials_TMTB_2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_TMTB_2.saveAsText(filename + 'trials_TMTB_2.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "FixCross"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    if globalClock.getTime() - startTime >= 92.5:
        currentLoop.finished = True
        continueRoutine = False
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
    while continueRoutine and routineTimer.getTime() > 0:
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
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
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
# completed 1.0 repeats of 'Blocks_TMTB_2'


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
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
