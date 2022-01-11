/******************** 
 * Tmtstop-B_1 Test *
 ********************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'TMTstop-B_1';  // from the Builder filename that created this script
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
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
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
    {'name': 'TMTstop-B_1_1linestimulus9.png', 'path': 'TMTstop-B_1_1linestimulus9.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus0.png', 'path': 'TMTstop-B_1_1redlinestimulus0.png'},
    {'name': '../Instruktioner TMTstopB.png', 'path': '../Instruktioner TMTstopB.png'},
    {'name': 'TMTstop-B_1_2linestimulus12.png', 'path': 'TMTstop-B_1_2linestimulus12.png'},
    {'name': 'TMTstop-B_1_1linestimulus4.png', 'path': 'TMTstop-B_1_1linestimulus4.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus2.png', 'path': 'TMTstop-B_1_2redlinestimulus2.png'},
    {'name': 'TMTstop-B_1_1linestimulus0.png', 'path': 'TMTstop-B_1_1linestimulus0.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus2.png', 'path': 'TMTstop-B_1_1greenlinestimulus2.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus14.png', 'path': 'TMTstop-B_1_2greenlinestimulus14.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus0.png', 'path': 'TMTstop-B_1_1greenlinestimulus0.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus1.png', 'path': 'TMTstop-B_1_2greenlinestimulus1.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus20.png', 'path': 'TMTstop-B_1_1redlinestimulus20.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus10.png', 'path': 'TMTstop-B_1_2redlinestimulus10.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus20.png', 'path': 'TMTstop-B_1_2redlinestimulus20.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus13.png', 'path': 'TMTstop-B_1_2redlinestimulus13.png'},
    {'name': 'TMTstop-B_1_1linestimulus19.png', 'path': 'TMTstop-B_1_1linestimulus19.png'},
    {'name': 'TMTstop-B_1_1linestimulus23.png', 'path': 'TMTstop-B_1_1linestimulus23.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus7.png', 'path': 'TMTstop-B_1_1greenlinestimulus7.png'},
    {'name': 'TMTstop-B_1_1linestimulus22.png', 'path': 'TMTstop-B_1_1linestimulus22.png'},
    {'name': 'TMTstop-B_1_2linestimulus15.png', 'path': 'TMTstop-B_1_2linestimulus15.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus6.png', 'path': 'TMTstop-B_1_1redlinestimulus6.png'},
    {'name': 'TMTstop-B_1_1.png', 'path': 'TMTstop-B_1_1.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus11.png', 'path': 'TMTstop-B_1_2redlinestimulus11.png'},
    {'name': 'TMTstop-B_1_2linestimulus19.png', 'path': 'TMTstop-B_1_2linestimulus19.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus16.png', 'path': 'TMTstop-B_1_1redlinestimulus16.png'},
    {'name': 'TMTstop-B_1_2linestimulus0.png', 'path': 'TMTstop-B_1_2linestimulus0.png'},
    {'name': 'TMTstop-B_1_2linestimulus14.png', 'path': 'TMTstop-B_1_2linestimulus14.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus12.png', 'path': 'TMTstop-B_1_1redlinestimulus12.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus15.png', 'path': 'TMTstop-B_1_1redlinestimulus15.png'},
    {'name': 'TMTstop-B_1_2linestimulus2.png', 'path': 'TMTstop-B_1_2linestimulus2.png'},
    {'name': 'TMTstop-B_1_2linestimulus10.png', 'path': 'TMTstop-B_1_2linestimulus10.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus13.png', 'path': 'TMTstop-B_1_2greenlinestimulus13.png'},
    {'name': 'TMTstop-B_1_1linestimulus17.png', 'path': 'TMTstop-B_1_1linestimulus17.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus0.png', 'path': 'TMTstop-B_1_2greenlinestimulus0.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus3.png', 'path': 'TMTstop-B_1_2redlinestimulus3.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus19.png', 'path': 'TMTstop-B_1_1redlinestimulus19.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus11.png', 'path': 'TMTstop-B_1_2greenlinestimulus11.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus22.png', 'path': 'TMTstop-B_1_2redlinestimulus22.png'},
    {'name': 'TMTstop-B_1_2firstgreen.png', 'path': 'TMTstop-B_1_2firstgreen.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus10.png', 'path': 'TMTstop-B_1_1redlinestimulus10.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus11.png', 'path': 'TMTstop-B_1_1greenlinestimulus11.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus13.png', 'path': 'TMTstop-B_1_1redlinestimulus13.png'},
    {'name': 'TMTstop-B_1_1linestimulus5.png', 'path': 'TMTstop-B_1_1linestimulus5.png'},
    {'name': 'TMTstop-B_1_1firstred.png', 'path': 'TMTstop-B_1_1firstred.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus20.png', 'path': 'TMTstop-B_1_1greenlinestimulus20.png'},
    {'name': 'TMTstop-B_1_1firstgreen.png', 'path': 'TMTstop-B_1_1firstgreen.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus19.png', 'path': 'TMTstop-B_1_1greenlinestimulus19.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus13.png', 'path': 'TMTstop-B_1_1greenlinestimulus13.png'},
    {'name': 'TMTstop-B_1_1linestimulus18.png', 'path': 'TMTstop-B_1_1linestimulus18.png'},
    {'name': 'TMTstop-B_1_1linestimulus12.png', 'path': 'TMTstop-B_1_1linestimulus12.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus12.png', 'path': 'TMTstop-B_1_1greenlinestimulus12.png'},
    {'name': 'TMTstop-B_1_2linestimulus13.png', 'path': 'TMTstop-B_1_2linestimulus13.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus1.png', 'path': 'TMTstop-B_1_2redlinestimulus1.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus4.png', 'path': 'TMTstop-B_1_2redlinestimulus4.png'},
    {'name': 'TMTstop-B_1_1.xlsx', 'path': 'TMTstop-B_1_1.xlsx'},
    {'name': 'TMTstop-B_1_1greenlinestimulus4.png', 'path': 'TMTstop-B_1_1greenlinestimulus4.png'},
    {'name': 'TMTstop-B_1_1linestimulus11.png', 'path': 'TMTstop-B_1_1linestimulus11.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus17.png', 'path': 'TMTstop-B_1_1greenlinestimulus17.png'},
    {'name': 'TMTstop-B_1_1linestimulus6.png', 'path': 'TMTstop-B_1_1linestimulus6.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus8.png', 'path': 'TMTstop-B_1_2redlinestimulus8.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus6.png', 'path': 'TMTstop-B_1_1greenlinestimulus6.png'},
    {'name': 'TMTstop-B_1_1linestimulus8.png', 'path': 'TMTstop-B_1_1linestimulus8.png'},
    {'name': 'TMTstop-B_1_1linestimulus1.png', 'path': 'TMTstop-B_1_1linestimulus1.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus5.png', 'path': 'TMTstop-B_1_2greenlinestimulus5.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus17.png', 'path': 'TMTstop-B_1_1redlinestimulus17.png'},
    {'name': 'TMTstop-B_1_2linestimulus8.png', 'path': 'TMTstop-B_1_2linestimulus8.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus14.png', 'path': 'TMTstop-B_1_1redlinestimulus14.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus19.png', 'path': 'TMTstop-B_1_2redlinestimulus19.png'},
    {'name': 'TMTstop-B_1_1linestimulus3.png', 'path': 'TMTstop-B_1_1linestimulus3.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus12.png', 'path': 'TMTstop-B_1_2redlinestimulus12.png'},
    {'name': 'TMTstop-B_1_2linestimulus5.png', 'path': 'TMTstop-B_1_2linestimulus5.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus0.png', 'path': 'TMTstop-B_1_2redlinestimulus0.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus6.png', 'path': 'TMTstop-B_1_2greenlinestimulus6.png'},
    {'name': 'TMTstop-B_1_1linestimulus20.png', 'path': 'TMTstop-B_1_1linestimulus20.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus21.png', 'path': 'TMTstop-B_1_1redlinestimulus21.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus5.png', 'path': 'TMTstop-B_1_1redlinestimulus5.png'},
    {'name': 'TMTstop-B_1_2linestimulus16.png', 'path': 'TMTstop-B_1_2linestimulus16.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus22.png', 'path': 'TMTstop-B_1_1greenlinestimulus22.png'},
    {'name': 'TMTstop-B_1_1linestimulus2.png', 'path': 'TMTstop-B_1_1linestimulus2.png'},
    {'name': 'TMTstop-B_1_2linestimulus4.png', 'path': 'TMTstop-B_1_2linestimulus4.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus15.png', 'path': 'TMTstop-B_1_1greenlinestimulus15.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus23.png', 'path': 'TMTstop-B_1_2redlinestimulus23.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus3.png', 'path': 'TMTstop-B_1_2greenlinestimulus3.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus16.png', 'path': 'TMTstop-B_1_1greenlinestimulus16.png'},
    {'name': 'TMTstop-B_1_2linestimulus17.png', 'path': 'TMTstop-B_1_2linestimulus17.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus21.png', 'path': 'TMTstop-B_1_2greenlinestimulus21.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus21.png', 'path': 'TMTstop-B_1_1greenlinestimulus21.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus19.png', 'path': 'TMTstop-B_1_2greenlinestimulus19.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus14.png', 'path': 'TMTstop-B_1_1greenlinestimulus14.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus8.png', 'path': 'TMTstop-B_1_2greenlinestimulus8.png'},
    {'name': 'TMTstop-B_1_2linestimulus23.png', 'path': 'TMTstop-B_1_2linestimulus23.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus7.png', 'path': 'TMTstop-B_1_2redlinestimulus7.png'},
    {'name': 'TMTstop-B_1_2linestimulus21.png', 'path': 'TMTstop-B_1_2linestimulus21.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus8.png', 'path': 'TMTstop-B_1_1greenlinestimulus8.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus9.png', 'path': 'TMTstop-B_1_1redlinestimulus9.png'},
    {'name': 'TMTstop-B_1_2linestimulus1.png', 'path': 'TMTstop-B_1_2linestimulus1.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus4.png', 'path': 'TMTstop-B_1_2greenlinestimulus4.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus14.png', 'path': 'TMTstop-B_1_2redlinestimulus14.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus5.png', 'path': 'TMTstop-B_1_2redlinestimulus5.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus15.png', 'path': 'TMTstop-B_1_2redlinestimulus15.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus7.png', 'path': 'TMTstop-B_1_1redlinestimulus7.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus8.png', 'path': 'TMTstop-B_1_1redlinestimulus8.png'},
    {'name': 'TMTstop-B_1_1linestimulus10.png', 'path': 'TMTstop-B_1_1linestimulus10.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus22.png', 'path': 'TMTstop-B_1_2greenlinestimulus22.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus12.png', 'path': 'TMTstop-B_1_2greenlinestimulus12.png'},
    {'name': 'TMTstop-B_1_2linestimulus18.png', 'path': 'TMTstop-B_1_2linestimulus18.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus18.png', 'path': 'TMTstop-B_1_1redlinestimulus18.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus9.png', 'path': 'TMTstop-B_1_2redlinestimulus9.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus16.png', 'path': 'TMTstop-B_1_2greenlinestimulus16.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus9.png', 'path': 'TMTstop-B_1_2greenlinestimulus9.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus15.png', 'path': 'TMTstop-B_1_2greenlinestimulus15.png'},
    {'name': 'TMTstop-B_1_2linestimulus11.png', 'path': 'TMTstop-B_1_2linestimulus11.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus23.png', 'path': 'TMTstop-B_1_1greenlinestimulus23.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus6.png', 'path': 'TMTstop-B_1_2redlinestimulus6.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus4.png', 'path': 'TMTstop-B_1_1redlinestimulus4.png'},
    {'name': 'TMTstop-B_1_2linestimulus9.png', 'path': 'TMTstop-B_1_2linestimulus9.png'},
    {'name': 'TMTstop-B_1_2.png', 'path': 'TMTstop-B_1_2.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus20.png', 'path': 'TMTstop-B_1_2greenlinestimulus20.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus17.png', 'path': 'TMTstop-B_1_2redlinestimulus17.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus16.png', 'path': 'TMTstop-B_1_2redlinestimulus16.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus10.png', 'path': 'TMTstop-B_1_1greenlinestimulus10.png'},
    {'name': 'TMTstop-B_1_2linestimulus3.png', 'path': 'TMTstop-B_1_2linestimulus3.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus11.png', 'path': 'TMTstop-B_1_1redlinestimulus11.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus3.png', 'path': 'TMTstop-B_1_1redlinestimulus3.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus21.png', 'path': 'TMTstop-B_1_2redlinestimulus21.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus2.png', 'path': 'TMTstop-B_1_1redlinestimulus2.png'},
    {'name': 'TMTstop-B_1_1linestimulus21.png', 'path': 'TMTstop-B_1_1linestimulus21.png'},
    {'name': 'TMTstop-B_1_2.xlsx', 'path': 'TMTstop-B_1_2.xlsx'},
    {'name': 'TMTstop-B_1_2firstred.png', 'path': 'TMTstop-B_1_2firstred.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus9.png', 'path': 'TMTstop-B_1_1greenlinestimulus9.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus23.png', 'path': 'TMTstop-B_1_2greenlinestimulus23.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus18.png', 'path': 'TMTstop-B_1_2greenlinestimulus18.png'},
    {'name': 'TMTstop-B_1_1linestimulus7.png', 'path': 'TMTstop-B_1_1linestimulus7.png'},
    {'name': 'TMTstop-B_1_2redlinestimulus18.png', 'path': 'TMTstop-B_1_2redlinestimulus18.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus1.png', 'path': 'TMTstop-B_1_1redlinestimulus1.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus5.png', 'path': 'TMTstop-B_1_1greenlinestimulus5.png'},
    {'name': 'TMTstop-B_1_1linestimulus15.png', 'path': 'TMTstop-B_1_1linestimulus15.png'},
    {'name': 'TMTstop-B_1_1linestimulus14.png', 'path': 'TMTstop-B_1_1linestimulus14.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus18.png', 'path': 'TMTstop-B_1_1greenlinestimulus18.png'},
    {'name': 'TMTstop-B_1_2linestimulus22.png', 'path': 'TMTstop-B_1_2linestimulus22.png'},
    {'name': 'TMTstop-B_1_1linestimulus16.png', 'path': 'TMTstop-B_1_1linestimulus16.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus23.png', 'path': 'TMTstop-B_1_1redlinestimulus23.png'},
    {'name': 'TMTstop-B_1_2linestimulus7.png', 'path': 'TMTstop-B_1_2linestimulus7.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus3.png', 'path': 'TMTstop-B_1_1greenlinestimulus3.png'},
    {'name': 'TMTstop-B_1_1greenlinestimulus1.png', 'path': 'TMTstop-B_1_1greenlinestimulus1.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus2.png', 'path': 'TMTstop-B_1_2greenlinestimulus2.png'},
    {'name': 'TMTstop-B_1_2linestimulus6.png', 'path': 'TMTstop-B_1_2linestimulus6.png'},
    {'name': 'TMTstop-B_1_1linestimulus13.png', 'path': 'TMTstop-B_1_1linestimulus13.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus10.png', 'path': 'TMTstop-B_1_2greenlinestimulus10.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus7.png', 'path': 'TMTstop-B_1_2greenlinestimulus7.png'},
    {'name': 'TMTstop-B_1_2greenlinestimulus17.png', 'path': 'TMTstop-B_1_2greenlinestimulus17.png'},
    {'name': 'TMTstop-B_1_2linestimulus20.png', 'path': 'TMTstop-B_1_2linestimulus20.png'},
    {'name': 'TMTstop-B_1_1redlinestimulus22.png', 'path': 'TMTstop-B_1_1redlinestimulus22.png'}
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
var text_2;
var trialClock;
var Stim;
var key_resp_2;
var msg;
var total_corr;
var total_all;
var msg2;
var rt;
var FixCrossClock;
var polygon;
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
    image : 'C:/Users/emilo/OneDrive - Lund University/Experiment paradigms/TMT_PsychoPY_new/Instruktioner TMTstopB.png', mask : undefined,
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
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Time is up! \n\nWell done, you have finished the experiment.',
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
    InstructionsComponents.push(text_2);
    
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


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'TMTstop-B_1_1.xlsx',
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
      trialList: 'TMTstop-B_1_2.xlsx',
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
        }
    
    key_resp_2.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
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
