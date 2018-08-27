
function initialize(box)

	dofile(box:get_config("${Path_Data}") .. "/plugins/stimulation/lua-stimulator-stim-codes.lua")

	number_of_trials = box:get_setting(2)
	first_class = _G[box:get_setting(3)]
	second_class = _G[box:get_setting(4)]
	baseline_duration = box:get_setting(5)
	wait_for_beep_duration = box:get_setting(6)
	wait_for_cue_duration = box:get_setting(7)
	display_cue_duration = box:get_setting(8)
	feedback_duration = box:get_setting(9)
	end_of_trial_min_duration = box:get_setting(10)
	end_of_trial_max_duration = box:get_setting(11)
	third_class = _G[box:get_setting(12)]
	fourth_class = _G[box:get_setting(13)]
	fifth_class = _G[box:get_setting(14)]
	
	number_of_cycles = math.floor(number_of_trials / 5)
	number_of_remaining = number_of_trials %5

end




function process(box)

	local t=0

	-- manages baseline

	box:send_stimulation(1, OVTK_StimulationId_ExperimentStart, t, 0)
	t = t + 5

	box:send_stimulation(1, OVTK_StimulationId_BaselineStart, t, 0)
	box:send_stimulation(1, OVTK_StimulationId_Beep, t, 0)
	t = t + baseline_duration

	box:send_stimulation(1, OVTK_StimulationId_BaselineStop, t, 0)
	box:send_stimulation(1, OVTK_StimulationId_Beep, t, 0)
	t = t + 5

	-- manages trials

	for i = 1, number_of_cycles do
		
		-- initializes random seed
		math.randomseed(os.time())

		-- fill the sequence table with predifined order
		sequence = {}
		for j = 1, 5 do
			table.insert(sequence, 1, first_class)
			table.insert(sequence, 1, second_class)
			table.insert(sequence, 1, third_class)
			table.insert(sequence, 1, fourth_class)
			table.insert(sequence, 1, fifth_class)
		
		end

		-- randomize the sequence
		for j = 1, 5 do
			a = math.random(1, 25)
			b = math.random(1, 25)
			swap = sequence[a]
			sequence[a] = sequence[b]
			sequence[b] = swap
		end
		
	
		for j = 1, 25 do
	


			box:send_stimulation(1, OVTK_GDF_Start_Of_Trial, t, 0)
			t = t + wait_for_cue_duration


			-- display cue

			box:send_stimulation(1, sequence[j], t, 0)
			t = t + display_cue_duration
			
			box:send_stimulation(1, OVTK_StimulationId_VisualStimulationStop, t, 0)
			t = t + 0.2
		
						

			
			box:send_stimulation(1, OVTK_StimulationId_Label_10, t, 0)		
			t = t + feedback_duration

			
			box:send_stimulation(1, OVTK_GDF_End_Of_Trial, t, 0)
			t = t + math.random(end_of_trial_min_duration, end_of_trial_max_duration)

		end
		
		for k = 1, 5 do
			box:send_stimulation(1, OVTK_GDF_Start_Of_Trial, t, 0)
			t = t + 0.1
			box:send_stimulation(1, OVTK_StimulationId_Label_11, t, 0)
			t = t + 0.1
			box:send_stimulation(1, OVTK_StimulationId_Label_10, t, 0)
			t = t + 5
			box:send_stimulation(1, OVTK_GDF_End_Of_Trial, t, 0)
			t = t + 0.2
		end
		t = t + 5
	end

	-- send end for completeness	
	box:send_stimulation(1, OVTK_GDF_End_Of_Session, t, 0)
	t = t + 5

	box:send_stimulation(1, OVTK_StimulationId_Train, t, 0)
	t = t + 1
	
	-- used to cause the acquisition scenario to stop
	box:send_stimulation(1, OVTK_StimulationId_ExperimentStop, t, 0)
	
end
