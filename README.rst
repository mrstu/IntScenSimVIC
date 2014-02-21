.. _readme-simulator:

#########################################################
Setup VIC model configuration and SGE jobs for $gcm/$scen 
#########################################################

************
Overview
************

* Historical run: initial state 10-year run; full run initialized to end state from initial state run
* Future runs: full run initialized to historical full run end state
* Run setup steps

    #. copy prior setup to new setup
    #. edit new setup 
    #. ./setup_vic_input_rcp85_CanESM2_2006_2100.bsh -- setup of global configuration and soil files
    #. ./run_vic_part.bsh  -- setup of SGE array job (consider chunk size for concurrent jobs)
    #. (cd rcp85/CanESM2/wus_full.1; qsub aj_vic.bsh.qsub)  -- start SGE array job (**scen**=rcp85; **gcm**=CanESM2; **sim_instance**=wus_full.1)

******
TODO:
******

* Describe VIC model setup files and approach
