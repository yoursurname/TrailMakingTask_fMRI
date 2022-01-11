/************** 
 * Tmtab Test *
 **************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'TMTAB';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(FinishRound1RoutineBegin());
flowScheduler.add(FinishRound1RoutineEachFrame());
flowScheduler.add(FinishRound1RoutineEnd());
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'TMTBD1.bmp', 'path': 'TMTBD1.bmp'},
    {'name': 'TMTAD113.bmp', 'path': 'TMTAD113.bmp'},
    {'name': 'TMTB-1.xlsx', 'path': 'TMTB-1.xlsx'},
    {'name': 'TMTBD17.bmp', 'path': 'TMTBD17.bmp'},
    {'name': 'TMTBD1I.bmp', 'path': 'TMTBD1I.bmp'},
    {'name': 'TMTBD112.bmp', 'path': 'TMTBD112.bmp'},
    {'name': 'TMTAD16.bmp', 'path': 'TMTAD16.bmp'},
    {'name': 'TMTAD121.bmp', 'path': 'TMTAD121.bmp'},
    {'name': 'TMTBD1F.bmp', 'path': 'TMTBD1F.bmp'},
    {'name': 'TMTBD14.bmp', 'path': 'TMTBD14.bmp'},
    {'name': 'TMTAD110.bmp', 'path': 'TMTAD110.bmp'},
    {'name': 'TMTAD115.bmp', 'path': 'TMTAD115.bmp'},
    {'name': 'TMTBD15.bmp', 'path': 'TMTBD15.bmp'},
    {'name': 'TMTAD123.bmp', 'path': 'TMTAD123.bmp'},
    {'name': 'TMTAD112.bmp', 'path': 'TMTAD112.bmp'},
    {'name': 'TMTAD13.bmp', 'path': 'TMTAD13.bmp'},
    {'name': 'TMTBD12.bmp', 'path': 'TMTBD12.bmp'},
    {'name': 'TMTBD11.bmp', 'path': 'TMTBD11.bmp'},
    {'name': 'TMTAD119.bmp', 'path': 'TMTAD119.bmp'},
    {'name': 'TMTAD111.bmp', 'path': 'TMTAD111.bmp'},
    {'name': 'TMTBD1C.bmp', 'path': 'TMTBD1C.bmp'},
    {'name': 'TMTBD16.bmp', 'path': 'TMTBD16.bmp'},
    {'name': 'TMTBD111.bmp', 'path': 'TMTBD111.bmp'},
    {'name': 'TMTAD120.bmp', 'path': 'TMTAD120.bmp'},
    {'name': 'TMTAD18.bmp', 'path': 'TMTAD18.bmp'},
    {'name': 'TMTBD19.bmp', 'path': 'TMTBD19.bmp'},
    {'name': 'TMTAD11.bmp', 'path': 'TMTAD11.bmp'},
    {'name': 'TMTAD1.bmp', 'path': 'TMTAD1.bmp'},
    {'name': 'TMTAD12.bmp', 'path': 'TMTAD12.bmp'},
    {'name': 'TMTAD17.bmp', 'path': 'TMTAD17.bmp'},
    {'name': 'TMTAD122.bmp', 'path': 'TMTAD122.bmp'},
    {'name': 'TMTA-1.xlsx', 'path': 'TMTA-1.xlsx'},
    {'name': 'TMTBD1B.bmp', 'path': 'TMTBD1B.bmp'},
    {'name': 'TMTBD1G.bmp', 'path': 'TMTBD1G.bmp'},
    {'name': 'TMTAD15.bmp', 'path': 'TMTAD15.bmp'},
    {'name': 'TMTAD19.bmp', 'path': 'TMTAD19.bmp'},
    {'name': 'TMTBD1D.bmp', 'path': 'TMTBD1D.bmp'},
    {'name': 'TMTBD1H.bmp', 'path': 'TMTBD1H.bmp'},
    {'name': 'TMTAD114.bmp', 'path': 'TMTAD114.bmp'},
    {'name': 'TMTAD14.bmp', 'path': 'TMTAD14.bmp'},
    {'name': 'TMTAD116.bmp', 'path': 'TMTAD116.bmp'},
    {'name': 'TMTBD18.bmp', 'path': 'TMTBD18.bmp'},
    {'name': 'TMTBD110.bmp', 'path': 'TMTBD110.bmp'},
    {'name': 'TMTBD1K.bmp', 'path': 'TMTBD1K.bmp'},
    {'name': 'TMTAD118.bmp', 'path': 'TMTAD118.bmp'},
    {'name': 'TMTBD13.bmp', 'path': 'TMTBD13.bmp'},
    {'name': 'TMTBD1J.bmp', 'path': 'TMTBD1J.bmp'},
    {'name': 'InkedInstructBfinal_LI.jpg', 'path': 'InkedInstructBfinal_LI.jpg'},
    {'name': 'TMTBD1A.bmp', 'path': 'TMTBD1A.bmp'},
    {'name': 'TMTAD117.bmp', 'path': 'TMTAD117.bmp'},
    {'name': 'TMTBD1E.bmp', 'path': 'TMTBD1E.bmp'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var InstructionsClock;
var Instruct;
var key_resp;
var text_2;
var trialClock;
var Stim;
var key_resp_2;
var msg;
var total_corr;
var total_all;
var msg2;
var rt;
var FinishRound1Clock;
var text_3;
var key_resp_3;
var EndClock;
var text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  Instruct = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Instruct', units : undefined, 
    image : 'InkedInstructBfinal_LI.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.8, 0.8],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Position your fingers over 1, 2 and 3 then press any button to start the experiment.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.04,  wrapWidth: 2.0, ori: 0.5,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  Stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Stim', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  msg = "";
  total_corr = 0;
  total_all = 0;
  msg2 = "";
  rt = 0;
  
  // Initialize components for Routine "FinishRound1"
  FinishRound1Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Good job!\n\nRound 1 of 4 finished.\n\nPress any button to continue.\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  Instruct = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Instruct', units : undefined, 
    image : 'InkedInstructBfinal_LI.jpg', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.8, 0.8],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Position your fingers over 1, 2 and 3 then press any button to start the experiment.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.04,  wrapWidth: 2.0, ori: 0.5,
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  Stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Stim', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  msg = "";
  total_corr = 0;
  total_all = 0;
  msg2 = "";
  rt = 0;
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Thank you!\n\nYou have finished the task!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Instructions'-------
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(Instruct);
    InstructionsComponents.push(key_resp);
    InstructionsComponents.push(text_2);
    
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Instructions'-------
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instruct* updates
    if (t >= 0.0 && Instruct.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instruct.tStart = t;  // (not accounting for frame time here)
      Instruct.frameNStart = frameN;  // exact frame index
      
      Instruct.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: [], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Instructions'-------
    InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'TMTA-1.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'TMTB-1.xlsx',
    seed: undefined, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_2.forEach(function() {
    const snapshot = trials_2.getSnapshot();

    trials_2LoopScheduler.add(importConditions(snapshot));
    trials_2LoopScheduler.add(trialRoutineBegin(snapshot));
    trials_2LoopScheduler.add(trialRoutineEachFrame(snapshot));
    trials_2LoopScheduler.add(trialRoutineEnd(snapshot));
    trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var _key_resp_2_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Stim.setImage(StimFile);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    if (key_resp.corr) {
        msg = "ring.wav";
        total_corr = (total_corr + 1);
        total_all = (total_all + 1);
        rt = key_resp.rt;
    } else {
        msg = "buzzerwrong.wav";
        total_all = (total_all + 1);
        rt = key_resp.rt;
    }
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(Stim);
    trialComponents.push(key_resp_2);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Stim* updates
    if (t >= 0.0 && Stim.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Stim.tStart = t;  // (not accounting for frame time here)
      Stim.frameNStart = frameN;  // exact frame index
      
      Stim.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[0].name;  // just the first key pressed
        key_resp_2.rt = _key_resp_2_allKeys[0].rt;
        // was this correct?
        if (key_resp_2.keys == corrAns) {
            key_resp_2.corr = 1;
        } else {
            key_resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (key_resp_2.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         key_resp_2.corr = 1;  // correct non-response
      } else {
         key_resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    psychoJS.experiment.addData('key_resp_2.corr', key_resp_2.corr);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var FinishRound1Components;
function FinishRound1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'FinishRound1'-------
    t = 0;
    FinishRound1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    FinishRound1Components = [];
    FinishRound1Components.push(text_3);
    FinishRound1Components.push(key_resp_3);
    
    FinishRound1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function FinishRound1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'FinishRound1'-------
    // get current time
    t = FinishRound1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: [], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    FinishRound1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FinishRound1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'FinishRound1'-------
    FinishRound1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "FinishRound1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndComponents;
function EndRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(text);
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function EndRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'End'-------
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 6.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'End'-------
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
