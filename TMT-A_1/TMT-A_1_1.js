/****************** 
 * Tmt-A_1_1 Test *
 ******************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'TMT-A_1_1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});
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
flowScheduler.add(InstruktionerRoutineBegin());
flowScheduler.add(InstruktionerRoutineEachFrame());
flowScheduler.add(InstruktionerRoutineEnd());
flowScheduler.add(FixCrossRoutineBegin());
flowScheduler.add(FixCrossRoutineEachFrame());
flowScheduler.add(FixCrossRoutineEnd());
const restartpracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(restartpracticeLoopBegin(restartpracticeLoopScheduler));
flowScheduler.add(restartpracticeLoopScheduler);
flowScheduler.add(restartpracticeLoopEnd);
flowScheduler.add(FixCrossRoutineBegin());
flowScheduler.add(FixCrossRoutineEachFrame());
flowScheduler.add(FixCrossRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(FixCrossRoutineBegin());
flowScheduler.add(FixCrossRoutineEachFrame());
flowScheduler.add(FixCrossRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(FixCrossRoutineBegin());
flowScheduler.add(FixCrossRoutineEachFrame());
flowScheduler.add(FixCrossRoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(FixCrossRoutineBegin());
flowScheduler.add(FixCrossRoutineEachFrame());
flowScheduler.add(FixCrossRoutineEnd());
const trials_4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_4LoopBegin(trials_4LoopScheduler));
flowScheduler.add(trials_4LoopScheduler);
flowScheduler.add(trials_4LoopEnd);
flowScheduler.add(FixCrossRoutineBegin());
flowScheduler.add(FixCrossRoutineEachFrame());
flowScheduler.add(FixCrossRoutineEnd());
const trials_5LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_5LoopBegin(trials_5LoopScheduler));
flowScheduler.add(trials_5LoopScheduler);
flowScheduler.add(trials_5LoopEnd);
flowScheduler.add(FixCrossRoutineBegin());
flowScheduler.add(FixCrossRoutineEachFrame());
flowScheduler.add(FixCrossRoutineEnd());
const trials_6LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_6LoopBegin(trials_6LoopScheduler));
flowScheduler.add(trials_6LoopScheduler);
flowScheduler.add(trials_6LoopEnd);
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
    {'name': 'TMT-A_1_6greenlinestimulus14.png', 'path': 'TMT-A_1_6greenlinestimulus14.png'},
    {'name': 'TMT-A_1_4linestimulus8.png', 'path': 'TMT-A_1_4linestimulus8.png'},
    {'name': 'TMT-A_1_5linestimulus10.png', 'path': 'TMT-A_1_5linestimulus10.png'},
    {'name': 'TMT-A_1_2linestimulus12.png', 'path': 'TMT-A_1_2linestimulus12.png'},
    {'name': 'TMT-A_1_5redlinestimulus16.png', 'path': 'TMT-A_1_5redlinestimulus16.png'},
    {'name': 'TMT-A_1_3greenlinestimulus15.png', 'path': 'TMT-A_1_3greenlinestimulus15.png'},
    {'name': 'TMT-A_1_6greenlinestimulus16.png', 'path': 'TMT-A_1_6greenlinestimulus16.png'},
    {'name': 'TMT-A_1_6greenlinestimulus6.png', 'path': 'TMT-A_1_6greenlinestimulus6.png'},
    {'name': 'TMT-A_1_6redlinestimulus4.png', 'path': 'TMT-A_1_6redlinestimulus4.png'},
    {'name': 'TMT-A_1_6greenlinestimulus23.png', 'path': 'TMT-A_1_6greenlinestimulus23.png'},
    {'name': 'TMT-A_1_6redlinestimulus8.png', 'path': 'TMT-A_1_6redlinestimulus8.png'},
    {'name': 'TMT-A_1_1greenlinestimulus7.png', 'path': 'TMT-A_1_1greenlinestimulus7.png'},
    {'name': 'TMT-A_1_1linestimulus1.png', 'path': 'TMT-A_1_1linestimulus1.png'},
    {'name': 'TMT-A_1_3linestimulus18.png', 'path': 'TMT-A_1_3linestimulus18.png'},
    {'name': 'TMT-A_1_5redlinestimulus21.png', 'path': 'TMT-A_1_5redlinestimulus21.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus4.png', 'path': 'TMT-A_1_practicegreenlinestimulus4.png'},
    {'name': 'TMT-A_1_2linestimulus2.png', 'path': 'TMT-A_1_2linestimulus2.png'},
    {'name': 'TMT-A_1_4greenlinestimulus10.png', 'path': 'TMT-A_1_4greenlinestimulus10.png'},
    {'name': 'TMT-A_1_5redlinestimulus12.png', 'path': 'TMT-A_1_5redlinestimulus12.png'},
    {'name': 'TMT-A_1_6greenlinestimulus1.png', 'path': 'TMT-A_1_6greenlinestimulus1.png'},
    {'name': 'TMT-A_1_3redlinestimulus22.png', 'path': 'TMT-A_1_3redlinestimulus22.png'},
    {'name': 'TMT-A_1_5linestimulus6.png', 'path': 'TMT-A_1_5linestimulus6.png'},
    {'name': 'TMT-A_1_4redlinestimulus11.png', 'path': 'TMT-A_1_4redlinestimulus11.png'},
    {'name': 'TMT-A_1_5redlinestimulus1.png', 'path': 'TMT-A_1_5redlinestimulus1.png'},
    {'name': 'TMT-A_1_2linestimulus20.png', 'path': 'TMT-A_1_2linestimulus20.png'},
    {'name': 'TMT-A_1_5firstgreen.png', 'path': 'TMT-A_1_5firstgreen.png'},
    {'name': 'TMT-A_1_3linestimulus3.png', 'path': 'TMT-A_1_3linestimulus3.png'},
    {'name': 'TMT-A_1_3greenlinestimulus12.png', 'path': 'TMT-A_1_3greenlinestimulus12.png'},
    {'name': 'TMT-A_1_3redlinestimulus0.png', 'path': 'TMT-A_1_3redlinestimulus0.png'},
    {'name': 'TMT-A_1_4linestimulus7.png', 'path': 'TMT-A_1_4linestimulus7.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus5.png', 'path': 'TMT-A_1_practiceredlinestimulus5.png'},
    {'name': 'TMT-A_1_1linestimulus20.png', 'path': 'TMT-A_1_1linestimulus20.png'},
    {'name': 'TMT-A_1_4redlinestimulus14.png', 'path': 'TMT-A_1_4redlinestimulus14.png'},
    {'name': 'TMT-A_1_6linestimulus6.png', 'path': 'TMT-A_1_6linestimulus6.png'},
    {'name': 'TMT-A_1_6linestimulus9.png', 'path': 'TMT-A_1_6linestimulus9.png'},
    {'name': 'TMT-A_1_3redlinestimulus1.png', 'path': 'TMT-A_1_3redlinestimulus1.png'},
    {'name': 'TMT-A_1_4greenlinestimulus19.png', 'path': 'TMT-A_1_4greenlinestimulus19.png'},
    {'name': 'TMT-A_1_2greenlinestimulus3.png', 'path': 'TMT-A_1_2greenlinestimulus3.png'},
    {'name': 'TMT-A_1_practice.xlsx', 'path': 'TMT-A_1_practice.xlsx'},
    {'name': 'TMT-A_1_4linestimulus23.png', 'path': 'TMT-A_1_4linestimulus23.png'},
    {'name': 'TMT-A_1_2redlinestimulus14.png', 'path': 'TMT-A_1_2redlinestimulus14.png'},
    {'name': 'TMT-A_1_2greenlinestimulus6.png', 'path': 'TMT-A_1_2greenlinestimulus6.png'},
    {'name': 'TMT-A_1_2linestimulus11.png', 'path': 'TMT-A_1_2linestimulus11.png'},
    {'name': 'TMT-A_1_3greenlinestimulus5.png', 'path': 'TMT-A_1_3greenlinestimulus5.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus6.png', 'path': 'TMT-A_1_practiceredlinestimulus6.png'},
    {'name': 'TMT-A_1_1linestimulus9.png', 'path': 'TMT-A_1_1linestimulus9.png'},
    {'name': 'TMT-A_1_1.png', 'path': 'TMT-A_1_1.png'},
    {'name': 'TMT-A_1_2linestimulus21.png', 'path': 'TMT-A_1_2linestimulus21.png'},
    {'name': 'TMT-A_1_6greenlinestimulus11.png', 'path': 'TMT-A_1_6greenlinestimulus11.png'},
    {'name': 'TMT-A_1_5redlinestimulus8.png', 'path': 'TMT-A_1_5redlinestimulus8.png'},
    {'name': 'TMT-A_1_6linestimulus5.png', 'path': 'TMT-A_1_6linestimulus5.png'},
    {'name': 'TMT-A_1_3greenlinestimulus2.png', 'path': 'TMT-A_1_3greenlinestimulus2.png'},
    {'name': 'TMT-A_1_practicelinestimulus3.png', 'path': 'TMT-A_1_practicelinestimulus3.png'},
    {'name': 'TMT-A_1_2linestimulus22.png', 'path': 'TMT-A_1_2linestimulus22.png'},
    {'name': 'TMT-A_1_3redlinestimulus18.png', 'path': 'TMT-A_1_3redlinestimulus18.png'},
    {'name': 'TMT-A_1_4greenlinestimulus17.png', 'path': 'TMT-A_1_4greenlinestimulus17.png'},
    {'name': 'TMT-A_1_4greenlinestimulus23.png', 'path': 'TMT-A_1_4greenlinestimulus23.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus3.png', 'path': 'TMT-A_1_practicegreenlinestimulus3.png'},
    {'name': 'TMT-A_1_2redlinestimulus10.png', 'path': 'TMT-A_1_2redlinestimulus10.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus8.png', 'path': 'TMT-A_1_practiceredlinestimulus8.png'},
    {'name': 'TMT-A_1_1linestimulus17.png', 'path': 'TMT-A_1_1linestimulus17.png'},
    {'name': 'TMT-A_1_2redlinestimulus5.png', 'path': 'TMT-A_1_2redlinestimulus5.png'},
    {'name': 'TMT-A_1_1redlinestimulus13.png', 'path': 'TMT-A_1_1redlinestimulus13.png'},
    {'name': 'TMT-A_1_1redlinestimulus18.png', 'path': 'TMT-A_1_1redlinestimulus18.png'},
    {'name': 'TMT-A_1_3greenlinestimulus0.png', 'path': 'TMT-A_1_3greenlinestimulus0.png'},
    {'name': 'TMT-A_1_2greenlinestimulus23.png', 'path': 'TMT-A_1_2greenlinestimulus23.png'},
    {'name': 'TMT-A_1_2greenlinestimulus17.png', 'path': 'TMT-A_1_2greenlinestimulus17.png'},
    {'name': 'TMT-A_1_3redlinestimulus6.png', 'path': 'TMT-A_1_3redlinestimulus6.png'},
    {'name': 'TMT-A_1_1redlinestimulus3.png', 'path': 'TMT-A_1_1redlinestimulus3.png'},
    {'name': 'TMT-A_1_5linestimulus18.png', 'path': 'TMT-A_1_5linestimulus18.png'},
    {'name': 'TMT-A_1_2redlinestimulus6.png', 'path': 'TMT-A_1_2redlinestimulus6.png'},
    {'name': 'TMT-A_1_1redlinestimulus19.png', 'path': 'TMT-A_1_1redlinestimulus19.png'},
    {'name': 'TMT-A_1_4linestimulus20.png', 'path': 'TMT-A_1_4linestimulus20.png'},
    {'name': '../Instruktioner TMTA.png', 'path': '../Instruktioner TMTA.png'},
    {'name': 'TMT-A_1_4linestimulus1.png', 'path': 'TMT-A_1_4linestimulus1.png'},
    {'name': 'TMT-A_1_5firstred.png', 'path': 'TMT-A_1_5firstred.png'},
    {'name': 'TMT-A_1_1redlinestimulus9.png', 'path': 'TMT-A_1_1redlinestimulus9.png'},
    {'name': 'TMT-A_1_3redlinestimulus10.png', 'path': 'TMT-A_1_3redlinestimulus10.png'},
    {'name': 'TMT-A_1_practicelinestimulus5.png', 'path': 'TMT-A_1_practicelinestimulus5.png'},
    {'name': 'TMT-A_1_1greenlinestimulus13.png', 'path': 'TMT-A_1_1greenlinestimulus13.png'},
    {'name': 'TMT-A_1_1redlinestimulus11.png', 'path': 'TMT-A_1_1redlinestimulus11.png'},
    {'name': 'TMT-A_1_6greenlinestimulus0.png', 'path': 'TMT-A_1_6greenlinestimulus0.png'},
    {'name': 'TMT-A_1_4redlinestimulus21.png', 'path': 'TMT-A_1_4redlinestimulus21.png'},
    {'name': 'TMT-A_1_5redlinestimulus13.png', 'path': 'TMT-A_1_5redlinestimulus13.png'},
    {'name': 'TMT-A_1_6linestimulus19.png', 'path': 'TMT-A_1_6linestimulus19.png'},
    {'name': 'TMT-A_1_5linestimulus5.png', 'path': 'TMT-A_1_5linestimulus5.png'},
    {'name': 'TMT-A_1_5greenlinestimulus23.png', 'path': 'TMT-A_1_5greenlinestimulus23.png'},
    {'name': 'TMT-A_1_2greenlinestimulus16.png', 'path': 'TMT-A_1_2greenlinestimulus16.png'},
    {'name': 'TMT-A_1_6redlinestimulus19.png', 'path': 'TMT-A_1_6redlinestimulus19.png'},
    {'name': 'TMT-A_1_1linestimulus11.png', 'path': 'TMT-A_1_1linestimulus11.png'},
    {'name': 'TMT-A_1_1firstgreen.png', 'path': 'TMT-A_1_1firstgreen.png'},
    {'name': 'TMT-A_1_6redlinestimulus1.png', 'path': 'TMT-A_1_6redlinestimulus1.png'},
    {'name': 'TMT-A_1_5linestimulus2.png', 'path': 'TMT-A_1_5linestimulus2.png'},
    {'name': 'TMT-A_1_4greenlinestimulus2.png', 'path': 'TMT-A_1_4greenlinestimulus2.png'},
    {'name': 'TMT-A_1_2linestimulus15.png', 'path': 'TMT-A_1_2linestimulus15.png'},
    {'name': 'TMT-A_1_2redlinestimulus9.png', 'path': 'TMT-A_1_2redlinestimulus9.png'},
    {'name': 'TMT-A_1_6redlinestimulus2.png', 'path': 'TMT-A_1_6redlinestimulus2.png'},
    {'name': 'TMT-A_1_1linestimulus16.png', 'path': 'TMT-A_1_1linestimulus16.png'},
    {'name': 'TMT-A_1_4greenlinestimulus4.png', 'path': 'TMT-A_1_4greenlinestimulus4.png'},
    {'name': 'TMT-A_1_5linestimulus15.png', 'path': 'TMT-A_1_5linestimulus15.png'},
    {'name': 'TMT-A_1_6redlinestimulus10.png', 'path': 'TMT-A_1_6redlinestimulus10.png'},
    {'name': 'TMT-A_1_2linestimulus9.png', 'path': 'TMT-A_1_2linestimulus9.png'},
    {'name': 'TMT-A_1_4linestimulus11.png', 'path': 'TMT-A_1_4linestimulus11.png'},
    {'name': 'TMT-A_1_6redlinestimulus5.png', 'path': 'TMT-A_1_6redlinestimulus5.png'},
    {'name': 'TMT-A_1_4greenlinestimulus15.png', 'path': 'TMT-A_1_4greenlinestimulus15.png'},
    {'name': 'TMT-A_1_4greenlinestimulus22.png', 'path': 'TMT-A_1_4greenlinestimulus22.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus4.png', 'path': 'TMT-A_1_practiceredlinestimulus4.png'},
    {'name': 'TMT-A_1_5greenlinestimulus16.png', 'path': 'TMT-A_1_5greenlinestimulus16.png'},
    {'name': 'TMT-A_1_2redlinestimulus4.png', 'path': 'TMT-A_1_2redlinestimulus4.png'},
    {'name': 'TMT-A_1_6linestimulus1.png', 'path': 'TMT-A_1_6linestimulus1.png'},
    {'name': 'TMT-A_1_4redlinestimulus10.png', 'path': 'TMT-A_1_4redlinestimulus10.png'},
    {'name': 'TMT-A_1_practicelinestimulus0.png', 'path': 'TMT-A_1_practicelinestimulus0.png'},
    {'name': 'TMT-A_1_4redlinestimulus8.png', 'path': 'TMT-A_1_4redlinestimulus8.png'},
    {'name': 'TMT-A_1_practice.png', 'path': 'TMT-A_1_practice.png'},
    {'name': 'TMT-A_1_2linestimulus13.png', 'path': 'TMT-A_1_2linestimulus13.png'},
    {'name': 'TMT-A_1_1linestimulus14.png', 'path': 'TMT-A_1_1linestimulus14.png'},
    {'name': 'TMT-A_1_2firstgreen.png', 'path': 'TMT-A_1_2firstgreen.png'},
    {'name': 'TMT-A_1_5greenlinestimulus4.png', 'path': 'TMT-A_1_5greenlinestimulus4.png'},
    {'name': 'TMT-A_1_4greenlinestimulus8.png', 'path': 'TMT-A_1_4greenlinestimulus8.png'},
    {'name': 'TMT-A_1_4greenlinestimulus18.png', 'path': 'TMT-A_1_4greenlinestimulus18.png'},
    {'name': 'TMT-A_1_5redlinestimulus17.png', 'path': 'TMT-A_1_5redlinestimulus17.png'},
    {'name': 'TMT-A_1_6greenlinestimulus15.png', 'path': 'TMT-A_1_6greenlinestimulus15.png'},
    {'name': 'TMT-A_1_4linestimulus5.png', 'path': 'TMT-A_1_4linestimulus5.png'},
    {'name': 'TMT-A_1_3greenlinestimulus20.png', 'path': 'TMT-A_1_3greenlinestimulus20.png'},
    {'name': 'TMT-A_1_3redlinestimulus20.png', 'path': 'TMT-A_1_3redlinestimulus20.png'},
    {'name': 'TMT-A_1_6redlinestimulus12.png', 'path': 'TMT-A_1_6redlinestimulus12.png'},
    {'name': 'TMT-A_1_3redlinestimulus16.png', 'path': 'TMT-A_1_3redlinestimulus16.png'},
    {'name': 'TMT-A_1_practicelinestimulus6.png', 'path': 'TMT-A_1_practicelinestimulus6.png'},
    {'name': 'TMT-A_1_6redlinestimulus0.png', 'path': 'TMT-A_1_6redlinestimulus0.png'},
    {'name': 'TMT-A_1_4redlinestimulus7.png', 'path': 'TMT-A_1_4redlinestimulus7.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus6.png', 'path': 'TMT-A_1_practicegreenlinestimulus6.png'},
    {'name': 'TMT-A_1_4linestimulus4.png', 'path': 'TMT-A_1_4linestimulus4.png'},
    {'name': 'TMT-A_1_2greenlinestimulus8.png', 'path': 'TMT-A_1_2greenlinestimulus8.png'},
    {'name': 'TMT-A_1_2greenlinestimulus12.png', 'path': 'TMT-A_1_2greenlinestimulus12.png'},
    {'name': 'TMT-A_1_2redlinestimulus22.png', 'path': 'TMT-A_1_2redlinestimulus22.png'},
    {'name': 'TMT-A_1_5greenlinestimulus6.png', 'path': 'TMT-A_1_5greenlinestimulus6.png'},
    {'name': 'TMT-A_1_5redlinestimulus18.png', 'path': 'TMT-A_1_5redlinestimulus18.png'},
    {'name': 'TMT-A_1_3redlinestimulus7.png', 'path': 'TMT-A_1_3redlinestimulus7.png'},
    {'name': 'TMT-A_1_6greenlinestimulus13.png', 'path': 'TMT-A_1_6greenlinestimulus13.png'},
    {'name': 'TMT-A_1_1redlinestimulus0.png', 'path': 'TMT-A_1_1redlinestimulus0.png'},
    {'name': 'TMT-A_1_4redlinestimulus18.png', 'path': 'TMT-A_1_4redlinestimulus18.png'},
    {'name': 'TMT-A_1_4linestimulus22.png', 'path': 'TMT-A_1_4linestimulus22.png'},
    {'name': 'TMT-A_1_1greenlinestimulus8.png', 'path': 'TMT-A_1_1greenlinestimulus8.png'},
    {'name': 'TMT-A_1_2redlinestimulus13.png', 'path': 'TMT-A_1_2redlinestimulus13.png'},
    {'name': 'TMT-A_1_4greenlinestimulus0.png', 'path': 'TMT-A_1_4greenlinestimulus0.png'},
    {'name': 'TMT-A_1_5linestimulus0.png', 'path': 'TMT-A_1_5linestimulus0.png'},
    {'name': 'TMT-A_1_6redlinestimulus14.png', 'path': 'TMT-A_1_6redlinestimulus14.png'},
    {'name': 'TMT-A_1_6redlinestimulus13.png', 'path': 'TMT-A_1_6redlinestimulus13.png'},
    {'name': 'TMT-A_1_4redlinestimulus2.png', 'path': 'TMT-A_1_4redlinestimulus2.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus2.png', 'path': 'TMT-A_1_practiceredlinestimulus2.png'},
    {'name': 'TMT-A_1_6linestimulus17.png', 'path': 'TMT-A_1_6linestimulus17.png'},
    {'name': 'TMT-A_1_6greenlinestimulus20.png', 'path': 'TMT-A_1_6greenlinestimulus20.png'},
    {'name': 'TMT-A_1_5redlinestimulus7.png', 'path': 'TMT-A_1_5redlinestimulus7.png'},
    {'name': 'TMT-A_1_4firstgreen.png', 'path': 'TMT-A_1_4firstgreen.png'},
    {'name': 'TMT-A_1_3redlinestimulus19.png', 'path': 'TMT-A_1_3redlinestimulus19.png'},
    {'name': 'TMT-A_1_5linestimulus12.png', 'path': 'TMT-A_1_5linestimulus12.png'},
    {'name': 'TMT-A_1_4linestimulus19.png', 'path': 'TMT-A_1_4linestimulus19.png'},
    {'name': 'TMT-A_1_6linestimulus0.png', 'path': 'TMT-A_1_6linestimulus0.png'},
    {'name': 'TMT-A_1_3greenlinestimulus10.png', 'path': 'TMT-A_1_3greenlinestimulus10.png'},
    {'name': 'TMT-A_1_6greenlinestimulus2.png', 'path': 'TMT-A_1_6greenlinestimulus2.png'},
    {'name': 'TMT-A_1_4linestimulus17.png', 'path': 'TMT-A_1_4linestimulus17.png'},
    {'name': 'TMT-A_1_5linestimulus9.png', 'path': 'TMT-A_1_5linestimulus9.png'},
    {'name': 'TMT-A_1_3linestimulus2.png', 'path': 'TMT-A_1_3linestimulus2.png'},
    {'name': 'TMT-A_1_4greenlinestimulus16.png', 'path': 'TMT-A_1_4greenlinestimulus16.png'},
    {'name': 'TMT-A_1_1greenlinestimulus9.png', 'path': 'TMT-A_1_1greenlinestimulus9.png'},
    {'name': 'TMT-A_1_5greenlinestimulus20.png', 'path': 'TMT-A_1_5greenlinestimulus20.png'},
    {'name': 'TMT-A_1_3greenlinestimulus22.png', 'path': 'TMT-A_1_3greenlinestimulus22.png'},
    {'name': 'TMT-A_1_6greenlinestimulus9.png', 'path': 'TMT-A_1_6greenlinestimulus9.png'},
    {'name': 'TMT-A_1_5linestimulus3.png', 'path': 'TMT-A_1_5linestimulus3.png'},
    {'name': 'TMT-A_1_1.xlsx', 'path': 'TMT-A_1_1.xlsx'},
    {'name': 'TMT-A_1_6linestimulus16.png', 'path': 'TMT-A_1_6linestimulus16.png'},
    {'name': 'TMT-A_1_2greenlinestimulus18.png', 'path': 'TMT-A_1_2greenlinestimulus18.png'},
    {'name': 'TMT-A_1_4greenlinestimulus14.png', 'path': 'TMT-A_1_4greenlinestimulus14.png'},
    {'name': 'TMT-A_1_3greenlinestimulus21.png', 'path': 'TMT-A_1_3greenlinestimulus21.png'},
    {'name': 'TMT-A_1_5greenlinestimulus9.png', 'path': 'TMT-A_1_5greenlinestimulus9.png'},
    {'name': 'TMT-A_1_1greenlinestimulus1.png', 'path': 'TMT-A_1_1greenlinestimulus1.png'},
    {'name': 'TMT-A_1_3linestimulus14.png', 'path': 'TMT-A_1_3linestimulus14.png'},
    {'name': 'TMT-A_1_5redlinestimulus5.png', 'path': 'TMT-A_1_5redlinestimulus5.png'},
    {'name': 'TMT-A_1_1redlinestimulus22.png', 'path': 'TMT-A_1_1redlinestimulus22.png'},
    {'name': 'TMT-A_1_5greenlinestimulus17.png', 'path': 'TMT-A_1_5greenlinestimulus17.png'},
    {'name': 'TMT-A_1_6redlinestimulus16.png', 'path': 'TMT-A_1_6redlinestimulus16.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus0.png', 'path': 'TMT-A_1_practiceredlinestimulus0.png'},
    {'name': 'TMT-A_1_2redlinestimulus19.png', 'path': 'TMT-A_1_2redlinestimulus19.png'},
    {'name': 'TMT-A_1_6linestimulus3.png', 'path': 'TMT-A_1_6linestimulus3.png'},
    {'name': 'TMT-A_1_1redlinestimulus2.png', 'path': 'TMT-A_1_1redlinestimulus2.png'},
    {'name': 'TMT-A_1_1redlinestimulus15.png', 'path': 'TMT-A_1_1redlinestimulus15.png'},
    {'name': 'TMT-A_1_4linestimulus12.png', 'path': 'TMT-A_1_4linestimulus12.png'},
    {'name': 'TMT-A_1_5redlinestimulus4.png', 'path': 'TMT-A_1_5redlinestimulus4.png'},
    {'name': 'TMT-A_1_4redlinestimulus19.png', 'path': 'TMT-A_1_4redlinestimulus19.png'},
    {'name': 'TMT-A_1_3linestimulus11.png', 'path': 'TMT-A_1_3linestimulus11.png'},
    {'name': 'TMT-A_1_4greenlinestimulus12.png', 'path': 'TMT-A_1_4greenlinestimulus12.png'},
    {'name': 'TMT-A_1_3firstgreen.png', 'path': 'TMT-A_1_3firstgreen.png'},
    {'name': 'TMT-A_1_3greenlinestimulus7.png', 'path': 'TMT-A_1_3greenlinestimulus7.png'},
    {'name': 'TMT-A_1_2redlinestimulus8.png', 'path': 'TMT-A_1_2redlinestimulus8.png'},
    {'name': 'TMT-A_1_2linestimulus10.png', 'path': 'TMT-A_1_2linestimulus10.png'},
    {'name': 'TMT-A_1_5redlinestimulus3.png', 'path': 'TMT-A_1_5redlinestimulus3.png'},
    {'name': 'TMT-A_1_3greenlinestimulus3.png', 'path': 'TMT-A_1_3greenlinestimulus3.png'},
    {'name': 'TMT-A_1_5linestimulus16.png', 'path': 'TMT-A_1_5linestimulus16.png'},
    {'name': 'TMT-A_1_6redlinestimulus3.png', 'path': 'TMT-A_1_6redlinestimulus3.png'},
    {'name': 'TMT-A_1_4linestimulus6.png', 'path': 'TMT-A_1_4linestimulus6.png'},
    {'name': 'TMT-A_1_1greenlinestimulus10.png', 'path': 'TMT-A_1_1greenlinestimulus10.png'},
    {'name': 'TMT-A_1_5greenlinestimulus19.png', 'path': 'TMT-A_1_5greenlinestimulus19.png'},
    {'name': 'TMT-A_1_2redlinestimulus18.png', 'path': 'TMT-A_1_2redlinestimulus18.png'},
    {'name': 'TMT-A_1_2linestimulus7.png', 'path': 'TMT-A_1_2linestimulus7.png'},
    {'name': 'TMT-A_1_5greenlinestimulus2.png', 'path': 'TMT-A_1_5greenlinestimulus2.png'},
    {'name': 'TMT-A_1_2redlinestimulus7.png', 'path': 'TMT-A_1_2redlinestimulus7.png'},
    {'name': 'TMT-A_1_2linestimulus5.png', 'path': 'TMT-A_1_2linestimulus5.png'},
    {'name': 'TMT-A_1_1greenlinestimulus11.png', 'path': 'TMT-A_1_1greenlinestimulus11.png'},
    {'name': 'TMT-A_1_practicefirstred.png', 'path': 'TMT-A_1_practicefirstred.png'},
    {'name': 'TMT-A_1_practicelinestimulus9.png', 'path': 'TMT-A_1_practicelinestimulus9.png'},
    {'name': 'TMT-A_1_5redlinestimulus9.png', 'path': 'TMT-A_1_5redlinestimulus9.png'},
    {'name': 'TMT-A_1_5linestimulus23.png', 'path': 'TMT-A_1_5linestimulus23.png'},
    {'name': 'TMT-A_1_3redlinestimulus3.png', 'path': 'TMT-A_1_3redlinestimulus3.png'},
    {'name': 'TMT-A_1_3greenlinestimulus16.png', 'path': 'TMT-A_1_3greenlinestimulus16.png'},
    {'name': 'TMT-A_1_3greenlinestimulus23.png', 'path': 'TMT-A_1_3greenlinestimulus23.png'},
    {'name': 'TMT-A_1_6greenlinestimulus3.png', 'path': 'TMT-A_1_6greenlinestimulus3.png'},
    {'name': 'TMT-A_1_2greenlinestimulus20.png', 'path': 'TMT-A_1_2greenlinestimulus20.png'},
    {'name': 'TMT-A_1_6linestimulus8.png', 'path': 'TMT-A_1_6linestimulus8.png'},
    {'name': 'TMT-A_1_4redlinestimulus17.png', 'path': 'TMT-A_1_4redlinestimulus17.png'},
    {'name': 'TMT-A_1_5.xlsx', 'path': 'TMT-A_1_5.xlsx'},
    {'name': 'TMT-A_1_6.png', 'path': 'TMT-A_1_6.png'},
    {'name': 'TMT-A_1_6linestimulus22.png', 'path': 'TMT-A_1_6linestimulus22.png'},
    {'name': 'TMT-A_1_3greenlinestimulus9.png', 'path': 'TMT-A_1_3greenlinestimulus9.png'},
    {'name': 'TMT-A_1_5redlinestimulus19.png', 'path': 'TMT-A_1_5redlinestimulus19.png'},
    {'name': 'TMT-A_1_5greenlinestimulus18.png', 'path': 'TMT-A_1_5greenlinestimulus18.png'},
    {'name': 'TMT-A_1_1redlinestimulus10.png', 'path': 'TMT-A_1_1redlinestimulus10.png'},
    {'name': 'TMT-A_1_1redlinestimulus14.png', 'path': 'TMT-A_1_1redlinestimulus14.png'},
    {'name': 'TMT-A_1_6redlinestimulus21.png', 'path': 'TMT-A_1_6redlinestimulus21.png'},
    {'name': 'TMT-A_1_1greenlinestimulus14.png', 'path': 'TMT-A_1_1greenlinestimulus14.png'},
    {'name': 'TMT-A_1_2greenlinestimulus22.png', 'path': 'TMT-A_1_2greenlinestimulus22.png'},
    {'name': 'TMT-A_1_6redlinestimulus17.png', 'path': 'TMT-A_1_6redlinestimulus17.png'},
    {'name': 'TMT-A_1_3linestimulus17.png', 'path': 'TMT-A_1_3linestimulus17.png'},
    {'name': 'TMT-A_1_6linestimulus7.png', 'path': 'TMT-A_1_6linestimulus7.png'},
    {'name': 'TMT-A_1_4redlinestimulus23.png', 'path': 'TMT-A_1_4redlinestimulus23.png'},
    {'name': 'TMT-A_1_5redlinestimulus10.png', 'path': 'TMT-A_1_5redlinestimulus10.png'},
    {'name': 'TMT-A_1_2linestimulus6.png', 'path': 'TMT-A_1_2linestimulus6.png'},
    {'name': 'TMT-A_1_4linestimulus16.png', 'path': 'TMT-A_1_4linestimulus16.png'},
    {'name': 'TMT-A_1_1greenlinestimulus0.png', 'path': 'TMT-A_1_1greenlinestimulus0.png'},
    {'name': 'TMT-A_1_5linestimulus4.png', 'path': 'TMT-A_1_5linestimulus4.png'},
    {'name': 'TMT-A_1_5greenlinestimulus11.png', 'path': 'TMT-A_1_5greenlinestimulus11.png'},
    {'name': 'TMT-A_1_5greenlinestimulus21.png', 'path': 'TMT-A_1_5greenlinestimulus21.png'},
    {'name': 'TMT-A_1_2linestimulus1.png', 'path': 'TMT-A_1_2linestimulus1.png'},
    {'name': 'TMT-A_1_5linestimulus8.png', 'path': 'TMT-A_1_5linestimulus8.png'},
    {'name': 'TMT-A_1_5linestimulus14.png', 'path': 'TMT-A_1_5linestimulus14.png'},
    {'name': 'TMT-A_1_1linestimulus7.png', 'path': 'TMT-A_1_1linestimulus7.png'},
    {'name': 'TMT-A_1_6redlinestimulus6.png', 'path': 'TMT-A_1_6redlinestimulus6.png'},
    {'name': 'TMT-A_1_3redlinestimulus8.png', 'path': 'TMT-A_1_3redlinestimulus8.png'},
    {'name': 'TMT-A_1_4linestimulus2.png', 'path': 'TMT-A_1_4linestimulus2.png'},
    {'name': 'TMT-A_1_1linestimulus3.png', 'path': 'TMT-A_1_1linestimulus3.png'},
    {'name': 'TMT-A_1_4linestimulus0.png', 'path': 'TMT-A_1_4linestimulus0.png'},
    {'name': 'TMT-A_1_2redlinestimulus1.png', 'path': 'TMT-A_1_2redlinestimulus1.png'},
    {'name': 'TMT-A_1_3greenlinestimulus4.png', 'path': 'TMT-A_1_3greenlinestimulus4.png'},
    {'name': 'TMT-A_1_3greenlinestimulus13.png', 'path': 'TMT-A_1_3greenlinestimulus13.png'},
    {'name': 'TMT-A_1_6linestimulus4.png', 'path': 'TMT-A_1_6linestimulus4.png'},
    {'name': 'TMT-A_1_4redlinestimulus12.png', 'path': 'TMT-A_1_4redlinestimulus12.png'},
    {'name': 'TMT-A_1_practicefirstgreen.png', 'path': 'TMT-A_1_practicefirstgreen.png'},
    {'name': 'TMT-A_1_1linestimulus4.png', 'path': 'TMT-A_1_1linestimulus4.png'},
    {'name': 'TMT-A_1_1redlinestimulus16.png', 'path': 'TMT-A_1_1redlinestimulus16.png'},
    {'name': 'TMT-A_1_2.png', 'path': 'TMT-A_1_2.png'},
    {'name': 'TMT-A_1_1linestimulus10.png', 'path': 'TMT-A_1_1linestimulus10.png'},
    {'name': 'TMT-A_1_1greenlinestimulus18.png', 'path': 'TMT-A_1_1greenlinestimulus18.png'},
    {'name': 'TMT-A_1_1redlinestimulus20.png', 'path': 'TMT-A_1_1redlinestimulus20.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus3.png', 'path': 'TMT-A_1_practiceredlinestimulus3.png'},
    {'name': 'TMT-A_1_1greenlinestimulus23.png', 'path': 'TMT-A_1_1greenlinestimulus23.png'},
    {'name': 'TMT-A_1_6linestimulus15.png', 'path': 'TMT-A_1_6linestimulus15.png'},
    {'name': 'TMT-A_1_6redlinestimulus20.png', 'path': 'TMT-A_1_6redlinestimulus20.png'},
    {'name': 'TMT-A_1_6greenlinestimulus8.png', 'path': 'TMT-A_1_6greenlinestimulus8.png'},
    {'name': 'TMT-A_1_3redlinestimulus14.png', 'path': 'TMT-A_1_3redlinestimulus14.png'},
    {'name': 'TMT-A_1_1greenlinestimulus6.png', 'path': 'TMT-A_1_1greenlinestimulus6.png'},
    {'name': 'TMT-A_1_2greenlinestimulus14.png', 'path': 'TMT-A_1_2greenlinestimulus14.png'},
    {'name': 'TMT-A_1_2linestimulus8.png', 'path': 'TMT-A_1_2linestimulus8.png'},
    {'name': 'TMT-A_1_1redlinestimulus21.png', 'path': 'TMT-A_1_1redlinestimulus21.png'},
    {'name': 'TMT-A_1_6greenlinestimulus5.png', 'path': 'TMT-A_1_6greenlinestimulus5.png'},
    {'name': 'TMT-A_1_1greenlinestimulus19.png', 'path': 'TMT-A_1_1greenlinestimulus19.png'},
    {'name': 'TMT-A_1_3greenlinestimulus17.png', 'path': 'TMT-A_1_3greenlinestimulus17.png'},
    {'name': 'TMT-A_1_6redlinestimulus15.png', 'path': 'TMT-A_1_6redlinestimulus15.png'},
    {'name': 'TMT-A_1_4linestimulus18.png', 'path': 'TMT-A_1_4linestimulus18.png'},
    {'name': 'TMT-A_1_3redlinestimulus9.png', 'path': 'TMT-A_1_3redlinestimulus9.png'},
    {'name': 'TMT-A_1_6linestimulus23.png', 'path': 'TMT-A_1_6linestimulus23.png'},
    {'name': 'TMT-A_1_6redlinestimulus22.png', 'path': 'TMT-A_1_6redlinestimulus22.png'},
    {'name': 'TMT-A_1_1redlinestimulus4.png', 'path': 'TMT-A_1_1redlinestimulus4.png'},
    {'name': 'TMT-A_1_1linestimulus8.png', 'path': 'TMT-A_1_1linestimulus8.png'},
    {'name': 'TMT-A_1_6linestimulus21.png', 'path': 'TMT-A_1_6linestimulus21.png'},
    {'name': 'TMT-A_1_5linestimulus13.png', 'path': 'TMT-A_1_5linestimulus13.png'},
    {'name': 'TMT-A_1_4greenlinestimulus7.png', 'path': 'TMT-A_1_4greenlinestimulus7.png'},
    {'name': 'TMT-A_1_2redlinestimulus16.png', 'path': 'TMT-A_1_2redlinestimulus16.png'},
    {'name': 'TMT-A_1_3linestimulus1.png', 'path': 'TMT-A_1_3linestimulus1.png'},
    {'name': 'TMT-A_1_4.xlsx', 'path': 'TMT-A_1_4.xlsx'},
    {'name': 'TMT-A_1_3linestimulus21.png', 'path': 'TMT-A_1_3linestimulus21.png'},
    {'name': 'TMT-A_1_1linestimulus6.png', 'path': 'TMT-A_1_1linestimulus6.png'},
    {'name': 'TMT-A_1_5linestimulus17.png', 'path': 'TMT-A_1_5linestimulus17.png'},
    {'name': 'TMT-A_1_5linestimulus20.png', 'path': 'TMT-A_1_5linestimulus20.png'},
    {'name': 'TMT-A_1_2linestimulus19.png', 'path': 'TMT-A_1_2linestimulus19.png'},
    {'name': 'TMT-A_1_2redlinestimulus12.png', 'path': 'TMT-A_1_2redlinestimulus12.png'},
    {'name': 'TMT-A_1_2greenlinestimulus11.png', 'path': 'TMT-A_1_2greenlinestimulus11.png'},
    {'name': 'TMT-A_1_6redlinestimulus18.png', 'path': 'TMT-A_1_6redlinestimulus18.png'},
    {'name': 'TMT-A_1_4redlinestimulus13.png', 'path': 'TMT-A_1_4redlinestimulus13.png'},
    {'name': 'TMT-A_1_3.png', 'path': 'TMT-A_1_3.png'},
    {'name': 'TMT-A_1_6linestimulus13.png', 'path': 'TMT-A_1_6linestimulus13.png'},
    {'name': 'TMT-A_1_1redlinestimulus23.png', 'path': 'TMT-A_1_1redlinestimulus23.png'},
    {'name': 'TMT-A_1_2greenlinestimulus13.png', 'path': 'TMT-A_1_2greenlinestimulus13.png'},
    {'name': 'TMT-A_1_3greenlinestimulus1.png', 'path': 'TMT-A_1_3greenlinestimulus1.png'},
    {'name': 'TMT-A_1_5redlinestimulus15.png', 'path': 'TMT-A_1_5redlinestimulus15.png'},
    {'name': 'TMT-A_1_4redlinestimulus5.png', 'path': 'TMT-A_1_4redlinestimulus5.png'},
    {'name': 'TMT-A_1_2greenlinestimulus4.png', 'path': 'TMT-A_1_2greenlinestimulus4.png'},
    {'name': 'TMT-A_1_5linestimulus22.png', 'path': 'TMT-A_1_5linestimulus22.png'},
    {'name': 'TMT-A_1_5greenlinestimulus1.png', 'path': 'TMT-A_1_5greenlinestimulus1.png'},
    {'name': 'TMT-A_1_6linestimulus2.png', 'path': 'TMT-A_1_6linestimulus2.png'},
    {'name': 'TMT-A_1_3linestimulus4.png', 'path': 'TMT-A_1_3linestimulus4.png'},
    {'name': 'TMT-A_1_4redlinestimulus15.png', 'path': 'TMT-A_1_4redlinestimulus15.png'},
    {'name': 'TMT-A_1_2linestimulus14.png', 'path': 'TMT-A_1_2linestimulus14.png'},
    {'name': 'TMT-A_1_6linestimulus12.png', 'path': 'TMT-A_1_6linestimulus12.png'},
    {'name': 'TMT-A_1_1greenlinestimulus17.png', 'path': 'TMT-A_1_1greenlinestimulus17.png'},
    {'name': 'TMT-A_1_3linestimulus20.png', 'path': 'TMT-A_1_3linestimulus20.png'},
    {'name': 'TMT-A_1_4redlinestimulus20.png', 'path': 'TMT-A_1_4redlinestimulus20.png'},
    {'name': 'TMT-A_1_4linestimulus3.png', 'path': 'TMT-A_1_4linestimulus3.png'},
    {'name': 'TMT-A_1_2redlinestimulus21.png', 'path': 'TMT-A_1_2redlinestimulus21.png'},
    {'name': 'TMT-A_1_3redlinestimulus11.png', 'path': 'TMT-A_1_3redlinestimulus11.png'},
    {'name': 'TMT-A_1_4linestimulus10.png', 'path': 'TMT-A_1_4linestimulus10.png'},
    {'name': 'TMT-A_1_2greenlinestimulus21.png', 'path': 'TMT-A_1_2greenlinestimulus21.png'},
    {'name': 'TMT-A_1_2greenlinestimulus10.png', 'path': 'TMT-A_1_2greenlinestimulus10.png'},
    {'name': 'TMT-A_1_1linestimulus15.png', 'path': 'TMT-A_1_1linestimulus15.png'},
    {'name': 'TMT-A_1_1greenlinestimulus5.png', 'path': 'TMT-A_1_1greenlinestimulus5.png'},
    {'name': 'TMT-A_1_5linestimulus11.png', 'path': 'TMT-A_1_5linestimulus11.png'},
    {'name': 'TMT-A_1_2greenlinestimulus19.png', 'path': 'TMT-A_1_2greenlinestimulus19.png'},
    {'name': 'TMT-A_1_2redlinestimulus20.png', 'path': 'TMT-A_1_2redlinestimulus20.png'},
    {'name': 'TMT-A_1_2linestimulus18.png', 'path': 'TMT-A_1_2linestimulus18.png'},
    {'name': 'TMT-A_1_3redlinestimulus23.png', 'path': 'TMT-A_1_3redlinestimulus23.png'},
    {'name': 'TMT-A_1_2linestimulus17.png', 'path': 'TMT-A_1_2linestimulus17.png'},
    {'name': 'TMT-A_1_4redlinestimulus4.png', 'path': 'TMT-A_1_4redlinestimulus4.png'},
    {'name': 'TMT-A_1_1linestimulus22.png', 'path': 'TMT-A_1_1linestimulus22.png'},
    {'name': 'TMT-A_1_practicelinestimulus1.png', 'path': 'TMT-A_1_practicelinestimulus1.png'},
    {'name': 'TMT-A_1_1greenlinestimulus2.png', 'path': 'TMT-A_1_1greenlinestimulus2.png'},
    {'name': 'TMT-A_1_4linestimulus9.png', 'path': 'TMT-A_1_4linestimulus9.png'},
    {'name': 'TMT-A_1_1redlinestimulus7.png', 'path': 'TMT-A_1_1redlinestimulus7.png'},
    {'name': 'TMT-A_1_5redlinestimulus0.png', 'path': 'TMT-A_1_5redlinestimulus0.png'},
    {'name': 'TMT-A_1_4linestimulus14.png', 'path': 'TMT-A_1_4linestimulus14.png'},
    {'name': 'TMT-A_1_4redlinestimulus16.png', 'path': 'TMT-A_1_4redlinestimulus16.png'},
    {'name': 'TMT-A_1_4greenlinestimulus6.png', 'path': 'TMT-A_1_4greenlinestimulus6.png'},
    {'name': 'TMT-A_1_3greenlinestimulus11.png', 'path': 'TMT-A_1_3greenlinestimulus11.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus5.png', 'path': 'TMT-A_1_practicegreenlinestimulus5.png'},
    {'name': 'TMT-A_1_4linestimulus21.png', 'path': 'TMT-A_1_4linestimulus21.png'},
    {'name': 'TMT-A_1_5redlinestimulus20.png', 'path': 'TMT-A_1_5redlinestimulus20.png'},
    {'name': 'TMT-A_1_1redlinestimulus12.png', 'path': 'TMT-A_1_1redlinestimulus12.png'},
    {'name': 'TMT-A_1_1linestimulus21.png', 'path': 'TMT-A_1_1linestimulus21.png'},
    {'name': 'TMT-A_1_3greenlinestimulus6.png', 'path': 'TMT-A_1_3greenlinestimulus6.png'},
    {'name': 'TMT-A_1_6greenlinestimulus7.png', 'path': 'TMT-A_1_6greenlinestimulus7.png'},
    {'name': 'TMT-A_1_3linestimulus15.png', 'path': 'TMT-A_1_3linestimulus15.png'},
    {'name': 'TMT-A_1_3redlinestimulus2.png', 'path': 'TMT-A_1_3redlinestimulus2.png'},
    {'name': 'TMT-A_1_2greenlinestimulus5.png', 'path': 'TMT-A_1_2greenlinestimulus5.png'},
    {'name': 'TMT-A_1_4greenlinestimulus1.png', 'path': 'TMT-A_1_4greenlinestimulus1.png'},
    {'name': 'TMT-A_1_6greenlinestimulus17.png', 'path': 'TMT-A_1_6greenlinestimulus17.png'},
    {'name': 'TMT-A_1_1greenlinestimulus12.png', 'path': 'TMT-A_1_1greenlinestimulus12.png'},
    {'name': 'TMT-A_1_1redlinestimulus5.png', 'path': 'TMT-A_1_1redlinestimulus5.png'},
    {'name': 'TMT-A_1_2redlinestimulus11.png', 'path': 'TMT-A_1_2redlinestimulus11.png'},
    {'name': 'TMT-A_1_2.xlsx', 'path': 'TMT-A_1_2.xlsx'},
    {'name': 'TMT-A_1_5redlinestimulus14.png', 'path': 'TMT-A_1_5redlinestimulus14.png'},
    {'name': 'TMT-A_1_5greenlinestimulus10.png', 'path': 'TMT-A_1_5greenlinestimulus10.png'},
    {'name': 'TMT-A_1_1linestimulus12.png', 'path': 'TMT-A_1_1linestimulus12.png'},
    {'name': 'TMT-A_1_5linestimulus1.png', 'path': 'TMT-A_1_5linestimulus1.png'},
    {'name': 'TMT-A_1_2greenlinestimulus1.png', 'path': 'TMT-A_1_2greenlinestimulus1.png'},
    {'name': 'TMT-A_1_4linestimulus15.png', 'path': 'TMT-A_1_4linestimulus15.png'},
    {'name': 'TMT-A_1_1linestimulus0.png', 'path': 'TMT-A_1_1linestimulus0.png'},
    {'name': 'TMT-A_1_2linestimulus16.png', 'path': 'TMT-A_1_2linestimulus16.png'},
    {'name': 'TMT-A_1_1greenlinestimulus3.png', 'path': 'TMT-A_1_1greenlinestimulus3.png'},
    {'name': 'TMT-A_1_2linestimulus3.png', 'path': 'TMT-A_1_2linestimulus3.png'},
    {'name': 'TMT-A_1_practicelinestimulus10.png', 'path': 'TMT-A_1_practicelinestimulus10.png'},
    {'name': 'TMT-A_1_3greenlinestimulus8.png', 'path': 'TMT-A_1_3greenlinestimulus8.png'},
    {'name': 'TMT-A_1_5linestimulus7.png', 'path': 'TMT-A_1_5linestimulus7.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus10.png', 'path': 'TMT-A_1_practicegreenlinestimulus10.png'},
    {'name': 'TMT-A_1_6greenlinestimulus4.png', 'path': 'TMT-A_1_6greenlinestimulus4.png'},
    {'name': 'TMT-A_1_3linestimulus8.png', 'path': 'TMT-A_1_3linestimulus8.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus10.png', 'path': 'TMT-A_1_practiceredlinestimulus10.png'},
    {'name': 'TMT-A_1_1greenlinestimulus21.png', 'path': 'TMT-A_1_1greenlinestimulus21.png'},
    {'name': 'TMT-A_1_4linestimulus13.png', 'path': 'TMT-A_1_4linestimulus13.png'},
    {'name': 'TMT-A_1_1linestimulus23.png', 'path': 'TMT-A_1_1linestimulus23.png'},
    {'name': 'TMT-A_1_3redlinestimulus5.png', 'path': 'TMT-A_1_3redlinestimulus5.png'},
    {'name': 'TMT-A_1_6linestimulus10.png', 'path': 'TMT-A_1_6linestimulus10.png'},
    {'name': 'TMT-A_1_2linestimulus0.png', 'path': 'TMT-A_1_2linestimulus0.png'},
    {'name': 'TMT-A_1_6redlinestimulus9.png', 'path': 'TMT-A_1_6redlinestimulus9.png'},
    {'name': 'TMT-A_1_3linestimulus6.png', 'path': 'TMT-A_1_3linestimulus6.png'},
    {'name': 'TMT-A_1_1greenlinestimulus15.png', 'path': 'TMT-A_1_1greenlinestimulus15.png'},
    {'name': 'TMT-A_1_3linestimulus7.png', 'path': 'TMT-A_1_3linestimulus7.png'},
    {'name': 'TMT-A_1_6redlinestimulus11.png', 'path': 'TMT-A_1_6redlinestimulus11.png'},
    {'name': 'TMT-A_1_4greenlinestimulus5.png', 'path': 'TMT-A_1_4greenlinestimulus5.png'},
    {'name': 'TMT-A_1_6greenlinestimulus21.png', 'path': 'TMT-A_1_6greenlinestimulus21.png'},
    {'name': 'TMT-A_1_3linestimulus0.png', 'path': 'TMT-A_1_3linestimulus0.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus9.png', 'path': 'TMT-A_1_practicegreenlinestimulus9.png'},
    {'name': 'TMT-A_1_3linestimulus16.png', 'path': 'TMT-A_1_3linestimulus16.png'},
    {'name': 'TMT-A_1_1greenlinestimulus4.png', 'path': 'TMT-A_1_1greenlinestimulus4.png'},
    {'name': 'TMT-A_1_6linestimulus14.png', 'path': 'TMT-A_1_6linestimulus14.png'},
    {'name': 'TMT-A_1_2linestimulus4.png', 'path': 'TMT-A_1_2linestimulus4.png'},
    {'name': 'TMT-A_1_6greenlinestimulus18.png', 'path': 'TMT-A_1_6greenlinestimulus18.png'},
    {'name': 'TMT-A_1_1redlinestimulus17.png', 'path': 'TMT-A_1_1redlinestimulus17.png'},
    {'name': 'TMT-A_1_3linestimulus12.png', 'path': 'TMT-A_1_3linestimulus12.png'},
    {'name': 'TMT-A_1_1linestimulus13.png', 'path': 'TMT-A_1_1linestimulus13.png'},
    {'name': 'TMT-A_1_6.xlsx', 'path': 'TMT-A_1_6.xlsx'},
    {'name': 'TMT-A_1_2redlinestimulus2.png', 'path': 'TMT-A_1_2redlinestimulus2.png'},
    {'name': 'TMT-A_1_4redlinestimulus0.png', 'path': 'TMT-A_1_4redlinestimulus0.png'},
    {'name': 'TMT-A_1_practicelinestimulus8.png', 'path': 'TMT-A_1_practicelinestimulus8.png'},
    {'name': 'TMT-A_1_3redlinestimulus21.png', 'path': 'TMT-A_1_3redlinestimulus21.png'},
    {'name': 'TMT-A_1_1greenlinestimulus20.png', 'path': 'TMT-A_1_1greenlinestimulus20.png'},
    {'name': 'TMT-A_1_1linestimulus18.png', 'path': 'TMT-A_1_1linestimulus18.png'},
    {'name': 'TMT-A_1_3redlinestimulus15.png', 'path': 'TMT-A_1_3redlinestimulus15.png'},
    {'name': 'TMT-A_1_4greenlinestimulus13.png', 'path': 'TMT-A_1_4greenlinestimulus13.png'},
    {'name': 'TMT-A_1_3linestimulus5.png', 'path': 'TMT-A_1_3linestimulus5.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus8.png', 'path': 'TMT-A_1_practicegreenlinestimulus8.png'},
    {'name': 'TMT-A_1_5greenlinestimulus0.png', 'path': 'TMT-A_1_5greenlinestimulus0.png'},
    {'name': 'TMT-A_1_5greenlinestimulus15.png', 'path': 'TMT-A_1_5greenlinestimulus15.png'},
    {'name': 'TMT-A_1_6firstred.png', 'path': 'TMT-A_1_6firstred.png'},
    {'name': 'TMT-A_1_3firstred.png', 'path': 'TMT-A_1_3firstred.png'},
    {'name': 'TMT-A_1_5greenlinestimulus5.png', 'path': 'TMT-A_1_5greenlinestimulus5.png'},
    {'name': 'TMT-A_1_4greenlinestimulus9.png', 'path': 'TMT-A_1_4greenlinestimulus9.png'},
    {'name': 'TMT-A_1_6redlinestimulus23.png', 'path': 'TMT-A_1_6redlinestimulus23.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus7.png', 'path': 'TMT-A_1_practicegreenlinestimulus7.png'},
    {'name': 'TMT-A_1_1redlinestimulus8.png', 'path': 'TMT-A_1_1redlinestimulus8.png'},
    {'name': 'TMT-A_1_5greenlinestimulus7.png', 'path': 'TMT-A_1_5greenlinestimulus7.png'},
    {'name': 'TMT-A_1_3.xlsx', 'path': 'TMT-A_1_3.xlsx'},
    {'name': 'TMT-A_1_4.png', 'path': 'TMT-A_1_4.png'},
    {'name': 'TMT-A_1_3linestimulus9.png', 'path': 'TMT-A_1_3linestimulus9.png'},
    {'name': 'TMT-A_1_4redlinestimulus1.png', 'path': 'TMT-A_1_4redlinestimulus1.png'},
    {'name': 'TMT-A_1_3redlinestimulus4.png', 'path': 'TMT-A_1_3redlinestimulus4.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus1.png', 'path': 'TMT-A_1_practiceredlinestimulus1.png'},
    {'name': 'TMT-A_1_practicelinestimulus7.png', 'path': 'TMT-A_1_practicelinestimulus7.png'},
    {'name': 'TMT-A_1_2redlinestimulus23.png', 'path': 'TMT-A_1_2redlinestimulus23.png'},
    {'name': 'TMT-A_1_6linestimulus11.png', 'path': 'TMT-A_1_6linestimulus11.png'},
    {'name': 'TMT-A_1_2greenlinestimulus15.png', 'path': 'TMT-A_1_2greenlinestimulus15.png'},
    {'name': 'TMT-A_1_6greenlinestimulus19.png', 'path': 'TMT-A_1_6greenlinestimulus19.png'},
    {'name': 'TMT-A_1_3greenlinestimulus14.png', 'path': 'TMT-A_1_3greenlinestimulus14.png'},
    {'name': 'TMT-A_1_1linestimulus2.png', 'path': 'TMT-A_1_1linestimulus2.png'},
    {'name': 'TMT-A_1_practicelinestimulus2.png', 'path': 'TMT-A_1_practicelinestimulus2.png'},
    {'name': 'TMT-A_1_4redlinestimulus9.png', 'path': 'TMT-A_1_4redlinestimulus9.png'},
    {'name': 'TMT-A_1_1greenlinestimulus16.png', 'path': 'TMT-A_1_1greenlinestimulus16.png'},
    {'name': 'TMT-A_1_4greenlinestimulus21.png', 'path': 'TMT-A_1_4greenlinestimulus21.png'},
    {'name': 'TMT-A_1_4greenlinestimulus11.png', 'path': 'TMT-A_1_4greenlinestimulus11.png'},
    {'name': 'TMT-A_1_2redlinestimulus0.png', 'path': 'TMT-A_1_2redlinestimulus0.png'},
    {'name': 'TMT-A_1_5redlinestimulus23.png', 'path': 'TMT-A_1_5redlinestimulus23.png'},
    {'name': 'TMT-A_1_5redlinestimulus22.png', 'path': 'TMT-A_1_5redlinestimulus22.png'},
    {'name': 'TMT-A_1_1redlinestimulus6.png', 'path': 'TMT-A_1_1redlinestimulus6.png'},
    {'name': 'TMT-A_1_2greenlinestimulus9.png', 'path': 'TMT-A_1_2greenlinestimulus9.png'},
    {'name': 'TMT-A_1_4firstred.png', 'path': 'TMT-A_1_4firstred.png'},
    {'name': 'TMT-A_1_3redlinestimulus13.png', 'path': 'TMT-A_1_3redlinestimulus13.png'},
    {'name': 'TMT-A_1_2firstred.png', 'path': 'TMT-A_1_2firstred.png'},
    {'name': 'TMT-A_1_5linestimulus21.png', 'path': 'TMT-A_1_5linestimulus21.png'},
    {'name': 'TMT-A_1_2greenlinestimulus0.png', 'path': 'TMT-A_1_2greenlinestimulus0.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus7.png', 'path': 'TMT-A_1_practiceredlinestimulus7.png'},
    {'name': 'TMT-A_1_6linestimulus18.png', 'path': 'TMT-A_1_6linestimulus18.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus0.png', 'path': 'TMT-A_1_practicegreenlinestimulus0.png'},
    {'name': 'TMT-A_1_3linestimulus19.png', 'path': 'TMT-A_1_3linestimulus19.png'},
    {'name': 'TMT-A_1_5greenlinestimulus14.png', 'path': 'TMT-A_1_5greenlinestimulus14.png'},
    {'name': 'TMT-A_1_1greenlinestimulus22.png', 'path': 'TMT-A_1_1greenlinestimulus22.png'},
    {'name': 'TMT-A_1_4redlinestimulus3.png', 'path': 'TMT-A_1_4redlinestimulus3.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus2.png', 'path': 'TMT-A_1_practicegreenlinestimulus2.png'},
    {'name': 'TMT-A_1_practiceredlinestimulus9.png', 'path': 'TMT-A_1_practiceredlinestimulus9.png'},
    {'name': 'TMT-A_1_1linestimulus5.png', 'path': 'TMT-A_1_1linestimulus5.png'},
    {'name': 'TMT-A_1_6greenlinestimulus10.png', 'path': 'TMT-A_1_6greenlinestimulus10.png'},
    {'name': 'TMT-A_1_1redlinestimulus1.png', 'path': 'TMT-A_1_1redlinestimulus1.png'},
    {'name': '../Instructions TMTA.png', 'path': '../Instructions TMTA.png'},
    {'name': 'TMT-A_1_5greenlinestimulus3.png', 'path': 'TMT-A_1_5greenlinestimulus3.png'},
    {'name': 'TMT-A_1_5greenlinestimulus22.png', 'path': 'TMT-A_1_5greenlinestimulus22.png'},
    {'name': 'TMT-A_1_3linestimulus23.png', 'path': 'TMT-A_1_3linestimulus23.png'},
    {'name': 'TMT-A_1_6greenlinestimulus12.png', 'path': 'TMT-A_1_6greenlinestimulus12.png'},
    {'name': 'TMT-A_1_3linestimulus10.png', 'path': 'TMT-A_1_3linestimulus10.png'},
    {'name': 'TMT-A_1_5redlinestimulus11.png', 'path': 'TMT-A_1_5redlinestimulus11.png'},
    {'name': 'TMT-A_1_2redlinestimulus15.png', 'path': 'TMT-A_1_2redlinestimulus15.png'},
    {'name': 'TMT-A_1_2greenlinestimulus2.png', 'path': 'TMT-A_1_2greenlinestimulus2.png'},
    {'name': 'TMT-A_1_2redlinestimulus3.png', 'path': 'TMT-A_1_2redlinestimulus3.png'},
    {'name': 'TMT-A_1_2redlinestimulus17.png', 'path': 'TMT-A_1_2redlinestimulus17.png'},
    {'name': 'TMT-A_1_2linestimulus23.png', 'path': 'TMT-A_1_2linestimulus23.png'},
    {'name': 'TMT-A_1_3greenlinestimulus18.png', 'path': 'TMT-A_1_3greenlinestimulus18.png'},
    {'name': 'TMT-A_1_1linestimulus19.png', 'path': 'TMT-A_1_1linestimulus19.png'},
    {'name': 'TMT-A_1_3redlinestimulus12.png', 'path': 'TMT-A_1_3redlinestimulus12.png'},
    {'name': 'TMT-A_1_3greenlinestimulus19.png', 'path': 'TMT-A_1_3greenlinestimulus19.png'},
    {'name': 'TMT-A_1_5redlinestimulus2.png', 'path': 'TMT-A_1_5redlinestimulus2.png'},
    {'name': 'TMT-A_1_2greenlinestimulus7.png', 'path': 'TMT-A_1_2greenlinestimulus7.png'},
    {'name': 'TMT-A_1_3linestimulus22.png', 'path': 'TMT-A_1_3linestimulus22.png'},
    {'name': 'TMT-A_1_5greenlinestimulus13.png', 'path': 'TMT-A_1_5greenlinestimulus13.png'},
    {'name': 'TMT-A_1_6redlinestimulus7.png', 'path': 'TMT-A_1_6redlinestimulus7.png'},
    {'name': 'TMT-A_1_practicegreenlinestimulus1.png', 'path': 'TMT-A_1_practicegreenlinestimulus1.png'},
    {'name': 'TMT-A_1_5.png', 'path': 'TMT-A_1_5.png'},
    {'name': 'TMT-A_1_5greenlinestimulus8.png', 'path': 'TMT-A_1_5greenlinestimulus8.png'},
    {'name': 'TMT-A_1_4greenlinestimulus20.png', 'path': 'TMT-A_1_4greenlinestimulus20.png'},
    {'name': 'TMT-A_1_3linestimulus13.png', 'path': 'TMT-A_1_3linestimulus13.png'},
    {'name': 'TMT-A_1_5greenlinestimulus12.png', 'path': 'TMT-A_1_5greenlinestimulus12.png'},
    {'name': 'TMT-A_1_practicelinestimulus4.png', 'path': 'TMT-A_1_practicelinestimulus4.png'},
    {'name': 'TMT-A_1_6greenlinestimulus22.png', 'path': 'TMT-A_1_6greenlinestimulus22.png'},
    {'name': 'TMT-A_1_5linestimulus19.png', 'path': 'TMT-A_1_5linestimulus19.png'},
    {'name': 'TMT-A_1_6firstgreen.png', 'path': 'TMT-A_1_6firstgreen.png'},
    {'name': 'TMT-A_1_5redlinestimulus6.png', 'path': 'TMT-A_1_5redlinestimulus6.png'},
    {'name': 'TMT-A_1_1firstred.png', 'path': 'TMT-A_1_1firstred.png'},
    {'name': 'TMT-A_1_4greenlinestimulus3.png', 'path': 'TMT-A_1_4greenlinestimulus3.png'},
    {'name': 'TMT-A_1_4redlinestimulus22.png', 'path': 'TMT-A_1_4redlinestimulus22.png'},
    {'name': 'TMT-A_1_3redlinestimulus17.png', 'path': 'TMT-A_1_3redlinestimulus17.png'},
    {'name': 'TMT-A_1_4redlinestimulus6.png', 'path': 'TMT-A_1_4redlinestimulus6.png'},
    {'name': 'TMT-A_1_6linestimulus20.png', 'path': 'TMT-A_1_6linestimulus20.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
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
var InstruktionerClock;
var image_2;
var key_resp_6;
var FixCrossClock;
var polygon;
var PracticeTrialClock;
var Stim_practice;
var key_resp_practice;
var ReadySetGoClock;
var text_5;
var key_resp_5;
var trialClock;
var Stim;
var key_resp_2;
var msg;
var total_corr;
var total_all;
var msg2;
var rt;
var EndClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  Instruct = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Instruct', units : undefined, 
    image : 'C:/Users/emilo/OneDrive - Lund University/Experiment paradigms/TMT_PsychoPY_new/Instructions TMTA.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.28, 0.72],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruktioner"
  InstruktionerClock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'C:/Users/emilo/OneDrive - Lund University/Experiment paradigms/TMT_PsychoPY_new/Instruktioner TMTA.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.28, 0.72],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FixCross"
  FixCrossClock = new util.Clock();
  polygon = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon', 
    vertices: 'cross', size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "PracticeTrial"
  PracticeTrialClock = new util.Clock();
  Stim_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Stim_practice', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.777, 1],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_practice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ReadySetGo"
  ReadySetGoClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  Stim = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Stim', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1.777, 1],
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
    text: 'Time is up! \n\nWell done, you have finished the experiment.\n\n\n\nTiden är ute!\n\nBra jobbat, du har slutfört experimentet.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
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
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
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
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
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
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instructions'-------
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var InstruktionerComponents;
function InstruktionerRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Instruktioner'-------
    t = 0;
    InstruktionerClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    InstruktionerComponents = [];
    InstruktionerComponents.push(image_2);
    InstruktionerComponents.push(key_resp_6);
    
    for (const thisComponent of InstruktionerComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstruktionerRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Instruktioner'-------
    // get current time
    t = InstruktionerClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: [], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
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
    for (const thisComponent of InstruktionerComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstruktionerRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instruktioner'-------
    for (const thisComponent of InstruktionerComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "Instruktioner" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var FixCrossComponents;
function FixCrossRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'FixCross'-------
    t = 0;
    FixCrossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    FixCrossComponents = [];
    FixCrossComponents.push(polygon);
    
    for (const thisComponent of FixCrossComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function FixCrossRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'FixCross'-------
    // get current time
    t = FixCrossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    frameRemains = 0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
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
    for (const thisComponent of FixCrossComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FixCrossRoutineEnd() {
  return async function () {
    //------Ending Routine 'FixCross'-------
    for (const thisComponent of FixCrossComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var restartpractice;
var currentLoop;
function restartpracticeLoopBegin(restartpracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    restartpractice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 100, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'restartpractice'
    });
    psychoJS.experiment.addLoop(restartpractice); // add the loop to the experiment
    currentLoop = restartpractice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRestartpractice of restartpractice) {
      const snapshot = restartpractice.getSnapshot();
      restartpracticeLoopScheduler.add(importConditions(snapshot));
      const trials_practiceLoopScheduler = new Scheduler(psychoJS);
      restartpracticeLoopScheduler.add(trials_practiceLoopBegin(trials_practiceLoopScheduler, snapshot));
      restartpracticeLoopScheduler.add(trials_practiceLoopScheduler);
      restartpracticeLoopScheduler.add(trials_practiceLoopEnd);
      restartpracticeLoopScheduler.add(ReadySetGoRoutineBegin(snapshot));
      restartpracticeLoopScheduler.add(ReadySetGoRoutineEachFrame());
      restartpracticeLoopScheduler.add(ReadySetGoRoutineEnd());
      restartpracticeLoopScheduler.add(endLoopIteration(restartpracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_practice;
function trials_practiceLoopBegin(trials_practiceLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_practice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TMT-A_1_practice.xlsx',
      seed: undefined, name: 'trials_practice'
    });
    psychoJS.experiment.addLoop(trials_practice); // add the loop to the experiment
    currentLoop = trials_practice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrials_practice of trials_practice) {
      const snapshot = trials_practice.getSnapshot();
      trials_practiceLoopScheduler.add(importConditions(snapshot));
      trials_practiceLoopScheduler.add(PracticeTrialRoutineBegin(snapshot));
      trials_practiceLoopScheduler.add(PracticeTrialRoutineEachFrame());
      trials_practiceLoopScheduler.add(PracticeTrialRoutineEnd());
      trials_practiceLoopScheduler.add(endLoopIteration(trials_practiceLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_practiceLoopEnd() {
  psychoJS.experiment.removeLoop(trials_practice);

  return Scheduler.Event.NEXT;
}


async function restartpracticeLoopEnd() {
  psychoJS.experiment.removeLoop(restartpractice);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TMT-A_1_1.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      const snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd());
      trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TMT-A_1_2.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      const snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_2LoopScheduler.add(trialRoutineEachFrame());
      trials_2LoopScheduler.add(trialRoutineEnd());
      trials_2LoopScheduler.add(endLoopIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TMT-A_1_3.xlsx',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      const snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_3LoopScheduler.add(trialRoutineEachFrame());
      trials_3LoopScheduler.add(trialRoutineEnd());
      trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


var trials_4;
function trials_4LoopBegin(trials_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TMT-A_1_4.xlsx',
      seed: undefined, name: 'trials_4'
    });
    psychoJS.experiment.addLoop(trials_4); // add the loop to the experiment
    currentLoop = trials_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_4 of trials_4) {
      const snapshot = trials_4.getSnapshot();
      trials_4LoopScheduler.add(importConditions(snapshot));
      trials_4LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_4LoopScheduler.add(trialRoutineEachFrame());
      trials_4LoopScheduler.add(trialRoutineEnd());
      trials_4LoopScheduler.add(endLoopIteration(trials_4LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_4LoopEnd() {
  psychoJS.experiment.removeLoop(trials_4);

  return Scheduler.Event.NEXT;
}


var trials_5;
function trials_5LoopBegin(trials_5LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_5 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TMT-A_1_5.xlsx',
      seed: undefined, name: 'trials_5'
    });
    psychoJS.experiment.addLoop(trials_5); // add the loop to the experiment
    currentLoop = trials_5;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_5 of trials_5) {
      const snapshot = trials_5.getSnapshot();
      trials_5LoopScheduler.add(importConditions(snapshot));
      trials_5LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_5LoopScheduler.add(trialRoutineEachFrame());
      trials_5LoopScheduler.add(trialRoutineEnd());
      trials_5LoopScheduler.add(endLoopIteration(trials_5LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_5LoopEnd() {
  psychoJS.experiment.removeLoop(trials_5);

  return Scheduler.Event.NEXT;
}


var trials_6;
function trials_6LoopBegin(trials_6LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_6 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TMT-A_1_6.xlsx',
      seed: undefined, name: 'trials_6'
    });
    psychoJS.experiment.addLoop(trials_6); // add the loop to the experiment
    currentLoop = trials_6;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_6 of trials_6) {
      const snapshot = trials_6.getSnapshot();
      trials_6LoopScheduler.add(importConditions(snapshot));
      trials_6LoopScheduler.add(trialRoutineBegin(snapshot));
      trials_6LoopScheduler.add(trialRoutineEachFrame());
      trials_6LoopScheduler.add(trialRoutineEnd());
      trials_6LoopScheduler.add(endLoopIteration(trials_6LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_6LoopEnd() {
  psychoJS.experiment.removeLoop(trials_6);

  return Scheduler.Event.NEXT;
}


var _key_resp_practice_allKeys;
var PracticeTrialComponents;
function PracticeTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'PracticeTrial'-------
    t = 0;
    PracticeTrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Stim_practice.setImage(Correct_StimFile);
    key_resp_practice.keys = undefined;
    key_resp_practice.rt = undefined;
    _key_resp_practice_allKeys = [];
    if (key_resp_practice.corr) {
        Stim_practice.setImage(Correct_StimFile);
    }
    
    // keep track of which components have finished
    PracticeTrialComponents = [];
    PracticeTrialComponents.push(Stim_practice);
    PracticeTrialComponents.push(key_resp_practice);
    
    for (const thisComponent of PracticeTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PracticeTrialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'PracticeTrial'-------
    // get current time
    t = PracticeTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Stim_practice* updates
    if (t >= 0.0 && Stim_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Stim_practice.tStart = t;  // (not accounting for frame time here)
      Stim_practice.frameNStart = frameN;  // exact frame index
      
      Stim_practice.setAutoDraw(true);
    }

    
    // *key_resp_practice* updates
    if (t >= 0.0 && key_resp_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_practice.tStart = t;  // (not accounting for frame time here)
      key_resp_practice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_practice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_practice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_practice.clearEvents(); });
    }

    if (key_resp_practice.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_practice.getKeys({keyList: ['1', '2', '3', 'x'], waitRelease: false});
      _key_resp_practice_allKeys = _key_resp_practice_allKeys.concat(theseKeys);
      if (_key_resp_practice_allKeys.length > 0) {
        key_resp_practice.keys = _key_resp_practice_allKeys[_key_resp_practice_allKeys.length - 1].name;  // just the last key pressed
        key_resp_practice.rt = _key_resp_practice_allKeys[_key_resp_practice_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_practice.keys == corrAns) {
            key_resp_practice.corr = 1;
        } else {
            key_resp_practice.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    if (((currentLoop.thisN === 12) && (t >= 1))) {
        continueRoutine = false;
    }
    if (((key_resp_practice.keys.length > 0) && ([key_resp_practice.keys.slice((- 1))[0]] === corrAns))) {
        key_resp_practice.corr = 1;
        continueRoutine = false;
    } else {
        if (((key_resp_practice.keys.length > 0) && ([key_resp_practice.keys] !== corrAns))) {
            key_resp_practice.corr = 0;
            Stim_practice.setImage(False_StimFile);
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
    for (const thisComponent of PracticeTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeTrialRoutineEnd() {
  return async function () {
    //------Ending Routine 'PracticeTrial'-------
    for (const thisComponent of PracticeTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp_practice.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         key_resp_practice.corr = 1;  // correct non-response
      } else {
         key_resp_practice.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_practice.keys', key_resp_practice.keys);
    psychoJS.experiment.addData('key_resp_practice.corr', key_resp_practice.corr);
    if (typeof key_resp_practice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_practice.rt', key_resp_practice.rt);
        routineTimer.reset();
        }
    
    key_resp_practice.stop();
    // the Routine "PracticeTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var ReadySetGoComponents;
function ReadySetGoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'ReadySetGo'-------
    t = 0;
    ReadySetGoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text_5.setText('You have finished the practice. If you understood the task correctly please read on, otherwise ask the experiment leader or press X to restart the practice.\n\nFrom here on there will be 25 circles instead of 12. If you finish all circles you will see a white cross for a few seconds then you will get 25 new circles and start again from 1. The experiments will end automatically after three minutes. \n\nPress 1, 2 or 3  to start the experiment.\n\n\n\nDu har slutfört provomgången. Om du förstod uppgiften rätt, läs vidare, annars fråga experimentledaren eller tryck på X för att starta om provomgången.\n\nHärifrån kommer det att finnas 25 circlar istället för 12. Om du slutför alla circlar kommer du att se ett vitt kors i några sekunder, sedan får du 25 nya circlar och börjar om från 1. Experimenten avslutas automatiskt efter tre minuter.\n\nTryck på 1, 2 eller 3 för att starta experimentet.\n\n\n');
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    ReadySetGoComponents = [];
    ReadySetGoComponents.push(text_5);
    ReadySetGoComponents.push(key_resp_5);
    
    for (const thisComponent of ReadySetGoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ReadySetGoRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'ReadySetGo'-------
    // get current time
    t = ReadySetGoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['1', '2', '3', 'x', 'space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
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
    for (const thisComponent of ReadySetGoComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ReadySetGoRoutineEnd() {
  return async function () {
    //------Ending Routine 'ReadySetGo'-------
    for (const thisComponent of ReadySetGoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        }
    
    key_resp_5.stop();
    // the Routine "ReadySetGo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var startTime;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Stim.setImage(Correct_StimFile);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    if (key_resp_2.corr) {
        msg = "ring.wav";
        total_corr = (total_corr + 1);
        total_all = (total_all + 1);
        rt = key_resp.rt;
        Stim.setImage(Correct_StimFile);
    } else {
        msg = "buzzerwrong.wav";
        total_all = (total_all + 1);
        rt = key_resp.rt;
        Stim.setImage(False_StimFile);
    }
    if ((trials.thisN === 0)) {
        startTime = globalClock.getTime();
    }
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(Stim);
    trialComponents.push(key_resp_2);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
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
        key_resp_2.keys = _key_resp_2_allKeys.map((key) => key.name);  // storing all keys
        key_resp_2.rt = _key_resp_2_allKeys.map((key) => key.rt);
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
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp_2.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         key_resp_2.corr = 1;  // correct non-response
      } else {
         key_resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
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


var EndComponents;
function EndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
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
    
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEachFrame() {
  return async function () {
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
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd() {
  return async function () {
    //------Ending Routine 'End'-------
    for (const thisComponent of EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
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
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
